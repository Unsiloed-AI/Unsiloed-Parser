#!/usr/bin/env python3
"""
Example script demonstrating the agentic RAG retrieval system
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import Unsiloed

def main():
    """Example of using the agentic RAG system"""

    # Set up OpenAI API key (you should use environment variable in production)
    os.environ["OPENAI_API_KEY"] = "your-api-key-here"

    # Initialize RAG system
    rag = Unsiloed.services.rag.RAGSystem()

    # Add some example documents (you would typically add your own documents)
    documents = [
        "./README.md",  # Use the README as an example document
    ]

    print("Loading documents into RAG system...")
    success = rag.add_documents_from_files(documents, strategy="semantic")

    if not success:
        print("Failed to load documents")
        return

    print("Documents loaded successfully!")

    # Example queries demonstrating different capabilities

    # Simple query
    print("\n=== Simple Query ===")
    result = rag.query("What are the main features of Unsiloed?")
    print(f"Found {result['total_results']} results")
    if result['results']:
        print("Top result:", result['results'][0]['content'][:200] + "...")

    # Multi-hop query
    print("\n=== Multi-hop Query ===")
    result = rag.query("How do I install and configure Unsiloed for document processing?", max_hops=3)
    print(f"Multi-hop search completed in {result['total_steps']} steps")
    print(f"Found {result['total_results']} total results")
    if result['results']:
        print("Top result:", result['results'][0]['content'][:200] + "...")

    # Negation query
    print("\n=== Negation Query ===")
    result = rag.query("What are the features of Unsiloed that are not related to file processing?")
    print(f"Found {result['total_results']} results")
    if result['results']:
        print("Top result:", result['results'][0]['content'][:200] + "...")

    # Using the convenience function
    print("\n=== Convenience Function ===")
    # This would work if you have documents available
    # result = Unsiloed.services.rag.rag_query(
    #     "What is the main purpose of Unsiloed?",
    #     documents=["./README.md"],
    #     max_hops=2
    # )

    print("RAG system demonstration completed!")

if __name__ == "__main__":
    main()
