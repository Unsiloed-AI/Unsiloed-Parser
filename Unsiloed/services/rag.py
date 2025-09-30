"""
Agentic RAG Retrieval System
Handles multi-hop queries and negation queries effectively
"""

import json
import os
import numpy as np
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from Unsiloed.services.chunking import process_document_chunking
from Unsiloed.utils.openai import get_openai_client

@dataclass
class QueryResult:
    """Result from a query operation"""
    content: str
    score: float
    metadata: Dict[str, Any]
    chunk_id: str

@dataclass
class MultiHopStep:
    """Represents a single step in a multi-hop query"""
    query: str
    retrieved_docs: List[QueryResult]
    reasoning: str
    next_queries: List[str]

class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = []
        self.client = get_openai_client()

    def add_chunks(self, chunks: List[Dict[str, Any]]):
        self.chunks.extend(chunks)

        texts = [chunk.get('text', '') for chunk in chunks]
        if texts:
            response = self.client.embeddings.create(
                input=texts,
                model="text-embedding-3-small"
            )

            for embedding_data in response.data:
                self.embeddings.append(embedding_data.embedding)

    def search(self, query: str, top_k: int = 5) -> List[QueryResult]:
        if not self.chunks or not self.embeddings:
            return []

        response = self.client.embeddings.create(
            input=[query],
            model="text-embedding-3-small"
        )
        query_embedding = response.data[0].embedding

        similarities = []
        for i, chunk_embedding in enumerate(self.embeddings):
            similarity = np.dot(query_embedding, chunk_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(chunk_embedding)
            )
            similarities.append((similarity, i))

        similarities.sort(reverse=True)
        results = []
        for similarity, idx in similarities[:top_k]:
            chunk = self.chunks[idx]
            results.append(QueryResult(
                content=chunk.get('text', ''),
                score=similarity,
                metadata=chunk.get('metadata', {}),
                chunk_id=chunk.get('id', str(idx))
            ))

        return results

class QueryAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.client = get_openai_client()

    def add_documents(self, documents: List[Dict[str, Any]]):
        self.vector_store.add_chunks(documents)

    def _decompose_query(self, query: str) -> List[str]:
        prompt = f"""
        Break down this complex query into 2-3 simpler sub-queries that can be answered independently:

        Query: {query}

        Return only the sub-queries as a JSON array, no explanation needed.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3
        )

        try:
            sub_queries = json.loads(response.choices[0].message.content)
            return sub_queries if isinstance(sub_queries, list) else []
        except:
            return [q.strip() for q in query.replace(' and ', '\n').replace(' or ', '\n').split('\n') if q.strip()]

    def _handle_negation(self, query: str, results: List[QueryResult]) -> List[QueryResult]:
        negation_words = ['not', 'without', 'except', 'excluding', 'avoid']

        has_negation = any(word in query.lower() for word in negation_words)

        if not has_negation:
            return results

        return results

    def _multi_hop_search(self, query: str, max_hops: int = 3) -> List[MultiHopStep]:
        steps = []
        current_queries = [query]

        for hop in range(max_hops):
            hop_results = []

            for sub_query in current_queries:
                results = self.vector_store.search(sub_query, top_k=3)

                filtered_results = self._handle_negation(sub_query, results)

                hop_results.extend(filtered_results)

                if results:
                    next_query_prompt = f"""
                    Based on this query: "{sub_query}"
                    And these retrieved results: {[r.content[:100] + '...' for r in results[:2]]}

                    What follow-up questions should I ask to get more complete information?
                    Return 1-2 specific follow-up queries as a JSON array.
                    """

                    try:
                        response = self.client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[{"role": "user", "content": next_query_prompt}],
                            max_tokens=150,
                            temperature=0.3
                        )

                        next_queries = json.loads(response.choices[0].message.content)
                        if isinstance(next_queries, list):
                            current_queries.extend(next_queries[:2])
                    except:
                        pass

            if hop_results:
                steps.append(MultiHopStep(
                    query=query,
                    retrieved_docs=hop_results[:5],
                    reasoning=f"Completed hop {hop + 1} of multi-hop search",
                    next_queries=current_queries[:3]
                ))

            current_queries = list(set(current_queries))[:3]

            if len(current_queries) <= 1 and hop > 0:
                break

        return steps

    def query(self, query: str, max_hops: int = 3) -> Dict[str, Any]:
        if not self.vector_store.chunks:
            return {"error": "No documents loaded. Add documents first using add_documents()."}

        steps = self._multi_hop_search(query, max_hops)

        all_results = []
        for step in steps:
            all_results.extend(step.retrieved_docs)

        unique_results = []
        for result in all_results:
            is_duplicate = False
            for existing in unique_results:
                if self._calculate_similarity(result.content, existing.content) > 0.9:
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_results.append(result)

        unique_results.sort(key=lambda x: x.score, reverse=True)

        return {
            "query": query,
            "results": [
                {
                    "content": r.content,
                    "score": r.score,
                    "metadata": r.metadata,
                    "chunk_id": r.chunk_id
                } for r in unique_results[:10]
            ],
            "total_steps": len(steps),
            "total_results": len(unique_results)
        }

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())

        if not words1 or not words2:
            return 0.0

        intersection = words1.intersection(words2)
        union = words1.union(words2)

        return len(intersection) / len(union) if union else 0.0

class RAGSystem:
    def __init__(self):
        self.query_agent = QueryAgent()

    def add_documents_from_files(self, file_paths: List[str], strategy: str = "semantic") -> bool:
        try:
            for file_path in file_paths:
                result = process_document_chunking(file_path, "auto", strategy, 1000, 100)

                if result and 'chunks' in result:
                    chunks = []
                    for chunk in result['chunks']:
                        chunks.append({
                            'text': chunk.get('content', ''),
                            'metadata': {
                                'source': file_path,
                                'page': chunk.get('page', 0),
                                'chunk_type': chunk.get('type', 'unknown')
                            },
                            'id': chunk.get('id', f"chunk_{len(chunks)}")
                        })

                    self.query_agent.add_documents(chunks)

            return True
        except Exception as e:
            print(f"Error adding documents: {e}")
            return False

    def query(self, query: str, max_hops: int = 3) -> Dict[str, Any]:
        return self.query_agent.query(query, max_hops)

def rag_query(query: str, documents: List[str] = None, max_hops: int = 3) -> Dict[str, Any]:
    rag = RAGSystem()

    if documents:
        rag.add_documents_from_files(documents)

    return rag.query(query, max_hops)
