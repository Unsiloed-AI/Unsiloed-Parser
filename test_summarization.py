#!/usr/bin/env python3
"""
Test script for reading order preservation in document chunking.

This script tests the enhanced reading order functionality for multi-column documents
in both JSON and Markdown formats.
"""

import sys
import os
import json
import tempfile

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Unsiloed.services.chunking import process_document_chunking
from Unsiloed.utils.chunking import analyze_reading_order_for_text, detect_multi_column_layout


def test_markdown_reading_order():
    """Test reading order analysis for Markdown documents."""
    print("Testing Markdown reading order analysis...")

    # Sample markdown with multi-section structure
    markdown_content = """# Document Title

## Section 1: Introduction

This is the first section with some content.

### Subsection 1.1

More content in subsection 1.1.

## Section 2: Main Content

This is the second section.

- List item 1
- List item 2
- List item 3

### Subsection 2.1

Content in subsection 2.1.

## Section 3: Conclusion

Final section with conclusion.
"""

    segments = analyze_reading_order_for_text(markdown_content, "markdown")

    print(f"Found {len(segments)} segments:")
    for i, segment in enumerate(segments):
        print(f"  {i}: {segment['element_type']} - '{segment['content'][:50]}...' (confidence: {segment['metadata']['confidence']})")

    # Test chunking
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(markdown_content)
        temp_file = f.name

    try:
        result = process_document_chunking(temp_file, "markdown", "paragraph")
        print(f"Created {result['total_chunks']} chunks")

        for i, chunk in enumerate(result['chunks'][:3]):  # Show first 3 chunks
            print(f"  Chunk {i}: {chunk['metadata']['strategy']} - reading_order_index: {chunk['metadata'].get('reading_order_index', 'N/A')}")
            print(f"    Text: '{chunk['text'][:60]}...'")

    finally:
        os.unlink(temp_file)

    return True


def test_json_reading_order():
    """Test reading order analysis for JSON documents."""
    print("\nTesting JSON reading order analysis...")

    # Sample JSON with nested structure
    json_content = {
        "document": {
            "title": "Sample Document",
            "metadata": {
                "author": "Test Author",
                "version": "1.0"
            },
            "sections": [
                {
                    "title": "Introduction",
                    "content": "This is the introduction section."
                },
                {
                    "title": "Main Content",
                    "content": "This is the main content section."
                }
            ],
            "conclusion": "This is the conclusion."
        }
    }

    json_text = json.dumps(json_content, indent=2)
    segments = analyze_reading_order_for_text(json_text, "json")

    print(f"Found {len(segments)} segments:")
    for i, segment in enumerate(segments[:5]):  # Show first 5 segments
        print(f"  {i}: {segment['element_type']} - '{segment['content'][:50]}...' (confidence: {segment['metadata']['confidence']})")

    # Test chunking
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write(json_text)
        temp_file = f.name

    try:
        result = process_document_chunking(temp_file, "json", "paragraph")
        print(f"Created {result['total_chunks']} chunks")

        for i, chunk in enumerate(result['chunks'][:3]):  # Show first 3 chunks
            print(f"  Chunk {i}: {chunk['metadata']['strategy']} - reading_order_index: {chunk['metadata'].get('reading_order_index', 'N/A')}")
            print(f"    Text: '{chunk['text'][:60]}...'")

    finally:
        os.unlink(temp_file)

    return True


def test_multi_column_detection():
    """Test multi-column layout detection."""
    print("\nTesting multi-column layout detection...")

    # Sample elements that would indicate multi-column layout
    elements = [
        {'center_x': 100, 'center_y': 100, 'bbox': [50, 80, 150, 120]},
        {'center_x': 400, 'center_y': 100, 'bbox': [350, 80, 450, 120]},
        {'center_x': 100, 'center_y': 200, 'bbox': [50, 180, 150, 220]},
        {'center_x': 400, 'center_y': 200, 'bbox': [350, 180, 450, 220]},
        {'center_x': 100, 'center_y': 300, 'bbox': [50, 280, 150, 320]},
        {'center_x': 400, 'center_y': 300, 'bbox': [350, 280, 450, 320]},
    ]

    is_multi_column = detect_multi_column_layout(elements, 600, 400)
    print(f"Multi-column layout detected: {is_multi_column}")

    # Test single column layout
    single_column_elements = [
        {'center_x': 100, 'center_y': 100, 'bbox': [50, 80, 150, 120]},
        {'center_x': 100, 'center_y': 200, 'bbox': [50, 180, 150, 220]},
        {'center_x': 100, 'center_y': 300, 'bbox': [50, 280, 150, 320]},
    ]

    is_single_column = detect_multi_column_layout(single_column_elements, 600, 400)
    print(f"Single-column layout detected: {is_single_column}")

    return True


def main():
    """Run all tests."""
    print("Testing Enhanced Reading Order Functionality")
    print("=" * 50)

    try:
        test_markdown_reading_order()
        test_json_reading_order()
        test_multi_column_detection()

        print("\n" + "=" * 50)
        print("All tests completed successfully!")

    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
