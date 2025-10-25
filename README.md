<!-- 
SEO Meta Description: 
unsiloed-parser - Open-source Python library for intelligent document chunking and parsing. 
Transform PDFs, DOCX, images, and web content into LLM-ready chunks using semantic AI, 
YOLO segmentation, and OCR. Perfect for RAG pipelines, AI chatbots, and workflow automation.
Keywords: document chunker, AI RAG tools, Python LLM preprocessing, semantic chunking, 
PDF parser, OCR extraction, document AI, text chunking library
-->

<p align="center">
  <img src="https://github.com/user-attachments/assets/f9964a81-0b78-4880-8f83-6b9fb0407aea" alt="Unsiloed Parser Logo - AI-Powered Document Chunking and Parsing Tool for LLM and RAG Applications" width="200">
</p>


<div align="center">

# Unsiloed Parser

### AI-Powered Document Processing for LLMs

**Transform unstructured data into structured LLM assets for RAG and automation.**

<p align="center">
  <img src="https://img.shields.io/pypi/v/unsiloed-parser?style=flat-square" alt="PyPI Version">
  <img src="https://img.shields.io/pypi/pyversions/unsiloed-parser?style=flat-square" alt="Python Version 3.8+">
  <img src="https://img.shields.io/github/license/Unsiloed-AI/Unsiloed-Parser?style=flat-square" alt="Apache 2.0 License">
  <img src="https://img.shields.io/github/stars/Unsiloed-AI/Unsiloed-Parser?style=flat-square" alt="GitHub Stars">
</p>

**unsiloed-parser** is an open-source Python library for **intelligent 
document chunking** and **AI-powered text extraction**. 


Perfect for building **RAG pipelines**, AI chatbots, knowledge bases, 
and automated document processing workflows.

**🔑 Keywords:** 
`semantic chunking` · `AI RAG tools` · `Python LLM preprocessing` · 
`PDF parser` · `OCR library` · `document AI`

---

### 🚀 Quick Links

<p align="center">
  <a href="https://www.unsiloed-ai.com/">
    <img src="https://img.shields.io/badge/Try%20It%20Out-Live%20Demo-FF6B6B?style=for-the-badge&logo=rocket&logoColor=white" alt="Try Unsiloed Parser Live Demo - Interactive Document Chunking Tool">
  </a>
  <a href="#-connect-with-us">
    <img src="https://img.shields.io/badge/Contact%20Us-Get%20In%20Touch-4ECDC4?style=for-the-badge&logo=mail&logoColor=white" alt="Contact Unsiloed AI Team - Get Support for Document Processing">
  </a>
</p>

---

</div>

##  Table of Contents

- [Document Chunking](#document-chunking)
- [Local LLM Model Support](#local-llm-model-support)
- [LaTeX Support](#latex-support)
- [Multi-lingual Support](#multi-lingual-support)
- [Extended File Format Support](#extended-file-format-support)
- [Configuration](#configuration)
- [Constraints & Limitations](#constraints--limitations)
- [Request Parameters](#request-parameters)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
  - [Supported File Types](#supported-file-types)
  - [Chunking Strategies](#chunking-strategies)
  - [Credential Options](#credential-options)
- [Development Setup](#development-setup)
- [Contributing](#contributing)
- [License](#license)
- [Community and Support](#community-and-support)
- [Connect with Us](#-connect-with-us)

---

## ✨ Features

### 📄 Document Chunking

**Supported File Types:** PDF, DOCX, PPTX, HTML, Markdown, 
Images, Webpages

**Chunking Strategies:**
  - **Fixed Size** : Splits text into chunks of specified size 
    with optional overlap
  - **Page-based** : Splits PDF by pages (PDF only, falls back 
    to paragraph for other file types)
  - **Semantic** : Uses YOLO for segmentation and VLM + OCR for 
    intelligent extraction of text, images, and tables — followed 
    by **semantic grouping** for clean, contextual output
  - **Paragraph** : Splits text by paragraphs
  - **Heading** : Splits text by identified headings
  - **Hierarchical** : Advanced multi-level chunking with 
    parent-child relationships

### 🤖 Local LLM Model Support

- **Modular LLM Selection**: Choose from multiple LLM providers 
  and models
- **Local Model Integration**: Support for locally hosted models 
  (Ollama)
- **Provider Options**: OpenAI, Anthropic, Google, Cohere, and 
  custom endpoints
- **Model Flexibility**: Switch between different models for 
  different chunking strategies

### 🔢 LaTeX Support

- **Mathematical Equations**: Full LaTeX rendering and processing
- **Scientific Documents**: Optimized for academic and technical 
  papers
- **Formula Extraction**: Intelligent extraction and preservation 
  of mathematical formulas
- **Equation Chunking**: Maintains mathematical context across 
  chunks

### 🌍 Multi-lingual Support

- **Language Detection**: Automatic language identification
- **Parameterized Processing**: Language-specific chunking 
  strategies
- **Unicode Support**: Full support for non-Latin scripts
- **Localized Chunking**: Language-aware paragraph and sentence 
  boundaries

### 📁 Extended File Format Support

- **Images** : JPG, PNG, TIFF, BMP with **OCR capabilities**
- **Webpages** : Direct URL processing with content extraction
- **Spreadsheets** : Excel, CSV with structured data extraction

## ⚙️ Configuration

### Environmental Variables
- `OPENAI_API_KEY`: Your OpenAI API key for **semantic chunking**

## ⚠️ Constraints & Limitations

### File Handling
- Temporary files are created during processing and deleted 
  afterward
- Files are processed in-memory where possible

### Text Processing
- Long text (>25,000 characters) is automatically split and 
  processed in parallel for **semantic chunking**
- Maximum token limit of 4000 for OpenAI responses


## 🔧 Request Parameters

### Document Chunking Endpoint

- `document_file`: The document file to process 
  (PDF, DOCX, PPTX)
- `strategy`: Chunking strategy to use (default: **"semantic"**)
  - Options: "fixed", "page", "semantic", "paragraph", "heading"
- `chunk_size`: Size of chunks for **fixed strategy** in 
  characters (default: 1000)
- `overlap`: Overlap size for **fixed strategy** in characters 
  (default: 100)

## 📦 Installation

[![PyPI version](https://badge.fury.io/py/unsiloed-parser.svg)](https://badge.fury.io/py/unsiloed-parser)

### Using pip

💡 **Tip:** We recommend installing in a virtual environment for 
project isolation.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install unsiloed-parser
pip install unsiloed-parser
```

### Requirements

unsiloed-parser requires Python 3.8 or higher and has the following dependencies:

**Core Dependencies:**
- `openai` - OpenAI API integration
- `PyPDF2` - PDF processing
- `python-docx` - Word document processing
- `python-pptx` - PowerPoint processing
- `Pillow` - Image processing
- `pytesseract` - OCR capabilities
- `aiohttp` - Async HTTP client
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `validators` - URL validation

**AI & ML:**
- `ultralytics` - YOLO model integration
- `opencv-python-headless` - Computer vision
- `numpy` - Numerical computing

**Utilities:**
- `python-dotenv` - Environment variable management
- `markdown` - Markdown processing
- `lxml` - XML/HTML parsing
- `html2text` - HTML to text conversion
- `pdf2image` - PDF to image conversion

## 🔐 Environment Setup

Before using unsiloed-parser, set up your **OpenAI API key** for 
semantic chunking:

### Using environment variables
```bash
# Linux/macOS
export OPENAI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

### Using a .env file
Create a `.env` file in your project directory:
```bash
OPENAI_API_KEY=your-api-key-here
```

Then in your Python code:
```python
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env
```

## 💻 Usage

### Example 1: Semantic Chunking (Default) 🧠

```python
import os
import Unsiloed

result = Unsiloed.process_sync({
    "filePath": "./test.pdf",
    "credentials": {
        "apiKey": os.environ.get("OPENAI_API_KEY")
    },
    "strategy": "semantic",
    "chunkSize": 1000,
    "overlap": 100
})

print(result)
```

**Example Output:**
```json
{
  "chunks": [
    {
      "content": "Introduction to Machine Learning\n\nMachine learning is a subset of artificial intelligence...",
      "metadata": {
        "type": "text",
        "page": 1,
        "position": 0
      }
    },
    {
      "content": "[Image: Neural Network Diagram]",
      "metadata": {
        "type": "image",
        "page": 1,
        "position": 1
      }
    },
    {
      "content": "Table: Model Comparison\n| Model | Accuracy | Speed |\n| ----- | -------- | ----- |\n| CNN   | 95%      | Fast  |",
      "metadata": {
        "type": "table",
        "page": 2,
        "position": 0
      }
    }
  ],
  "metadata": {
    "total_chunks": 3,
    "file_type": "pdf",
    "processing_time": 2.5
  }
}
```

### Example 2: Processing HTML Files 🌐

```python
import Unsiloed

html_result = Unsiloed.process_sync({
    "filePath": "./webpage.html",
    "credentials": {
        "apiKey": os.environ.get("OPENAI_API_KEY")
    },
    "strategy": "paragraph"
})
```

### Example 3: Processing Markdown Files 📝

```python
import Unsiloed

markdown_result = Unsiloed.process_sync({
    "filePath": "./README.md",
    "credentials": {
        "apiKey": os.environ.get("OPENAI_API_KEY")
    },
    "strategy": "heading"
})
```

### Example 4: Processing Website URLs 🔗

```python
import Unsiloed

url_result = Unsiloed.process_sync({
    "filePath": "https://example.com",
    "credentials": {
        "apiKey": os.environ.get("OPENAI_API_KEY")
    },
    "strategy": "paragraph"
})
```

### Example 5: Using Async Version ⚡

```python
import asyncio
import Unsiloed

async def async_processing():
    result = await Unsiloed.process({
        "filePath": "./test.pdf",
        "credentials": {
            "apiKey": os.environ.get("OPENAI_API_KEY")
        },
        "strategy": "semantic"
    })
    return result

# Run async processing
async_result = asyncio.run(async_processing())
```

### Example 6: Error Handling 🛡️

```python
import Unsiloed
import os

try:
    result = Unsiloed.process_sync({
        "filePath": "./document.pdf",
        "credentials": {
            "apiKey": os.environ.get("OPENAI_API_KEY")
        },
        "strategy": "semantic"
    })
    print(f"Successfully processed {len(result['chunks'])} chunks")
    
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    
except ValueError as e:
    print(f"Error: Invalid configuration - {e}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

### 📂 Supported File Types

Transform any document format into **LLM-ready chunks** with 
**intelligent parsing** and **extraction**.

| File Type | Extensions | Supported Strategies | Key Features | Use Cases |
|-----------|-----------|---------------------|--------------|-----------|
| **PDF Documents** | `.pdf` | All strategies (semantic, fixed, page, paragraph, heading, hierarchical) | PDF chunking for RAG, page-level extraction, text and image parsing | Research papers, reports, ebooks, invoices |
| **Word Documents** | `.docx` | All except page-based | Document parsing, style-aware chunking, table extraction | Business documents, contracts, articles |
| **PowerPoint** | `.pptx` | All except page-based | Slide-by-slide processing, text and image extraction | Presentations, training materials, pitch decks |
| **HTML Files** | `.html`, `.htm` | All except page-based | Web content extraction, semantic HTML parsing | Web pages, documentation, blog posts |
| **Markdown** | `.md`, `.markdown` | All except page-based | Heading-based structure, code block preservation | Technical docs, READMEs, wikis |
| **Web URLs** | `http://`, `https://` | All except page-based | Live webpage scraping, dynamic content extraction | Real-time content processing, web monitoring |
| **Images** | `.jpg`, `.png`, `.tiff`, `.bmp` | Semantic, fixed, paragraph | OCR for images, handwriting recognition, visual text extraction | Scanned documents, photos, screenshots |
| **Spreadsheets** | `.xlsx`, `.csv` | Semantic, fixed, paragraph | Structured data extraction, table parsing, cell-level analysis | Data tables, reports, inventories |

**SEO Keywords:** PDF chunking for RAG, OCR for images, document parsing for LLM, semantic document chunking, AI-powered text extraction, webpage to text conversion, DOCX parsing, structured data extraction

### 🎯 Chunking Strategies

Choose the optimal strategy for your **document processing needs** 
and **RAG pipeline**.

| Strategy | Best For | How It Works | API Key Required | Output Format |
|----------|----------|--------------|------------------|---------------|
| **Semantic** | RAG pipelines, AI applications, context-aware chunking | Uses YOLO segmentation + VLM + OCR to intelligently identify and group related content (text, images, tables) | ✅ Yes (OpenAI) | Structured chunks with semantic context, metadata, and type classification |
| **Fixed** | Token-limited LLMs, consistent chunk sizes, embeddings | Splits text into uniform chunks with configurable size and overlap | ❌ No | Fixed-size text chunks with character/word count control |
| **Page** | PDF documents, page-level processing | Extracts content page-by-page, preserving document structure | ❌ No | One chunk per page with page numbers |
| **Paragraph** | Natural text breaks, readability | Splits on paragraph boundaries using natural language structure | ❌ No | Paragraph-level chunks maintaining context |
| **Heading** | Hierarchical documents, documentation | Organizes content by heading structure (H1, H2, H3, etc.) | ❌ No | Section-based chunks with heading hierarchy |
| **Hierarchical** | Complex documents, parent-child relationships | Advanced multi-level chunking with nested structure and relationships | ❌ No | Nested chunks with parent-child metadata |

**💡 Performance Tips:**
- Use **semantic**  for best RAG results and AI-powered content 
  understanding
- Use **fixed**  for consistent embedding sizes and token 
  management
- Use **heading**  for technical documentation and structured 
  content
- Use **hierarchical**  for complex documents requiring context 
  preservation

###  Credential Options

You can provide credentials in **three ways**:

1. **In the options** (recommended):
```python
result = Unsiloed.process_sync({
    "filePath": "./test.pdf",
    "credentials": {
        "apiKey": "your-openai-api-key"
    },
    "strategy": "semantic"
})
```

2. **Environment variable**:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

3. **Using .env file**:
```bash
OPENAI_API_KEY=your-openai-api-key
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- git

### Setting Up Local Development Environment

1. Clone the repository:
```bash
git clone https://github.com/Unsiloed-AI/Unsiloed-Parser.git
cd Unsiloed-Parser
```

2. Create a virtual environment:
```bash
# Using venv
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
# Create a .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

5. Run the FastAPI server locally (if applicable):
```bash
uvicorn Unsiloed.app:app --reload
```

6. Access the API documentation:
Open your browser and go to `http://localhost:8000/docs`

## 🤝 Contributing

We welcome contributions to **unsiloed-parser**! 

Here's how you can help:

### Setting Up Development Environment

1. Fork the repository and clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/Unsiloed-Parser.git
cd Unsiloed-Parser
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
```

### Making Changes

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and write tests if applicable

3. Commit your changes:
```bash
git commit -m "Add your meaningful commit message here"
```

4. Push to your fork:
```bash
git push origin feature/your-feature-name
```

5. Create a Pull Request from your fork to the main repository

### Code Style and Standards

- We follow PEP 8 for Python code style
- Use type hints where appropriate
- Document functions and classes with docstrings
- Write tests for new features

## 📄 License

This project is licensed under the **Apache-2.0 License** - see 
the [LICENSE](LICENSE) file for details.

## 🌟 Community and Support

### Join the Community

- **GitHub Discussions** 💬: For questions, ideas, and discussions
- **Issues** 🐛: For bug reports and feature requests
- **Pull Requests** 🔧: For contributing to the codebase

### Staying Updated

- **Star** ⭐ the repository to show support
- **Watch** 👀 for notification on new releases

</div>

---

## 📞 Connect with Us

<div align="center">

### Ready to Transform Your Data? Let's Connect! 🚀

<p align="center">
  <img src="https://img.shields.io/badge/We're%20Here%20to%20Help-Let's%20Chat-brightgreen?style=for-the-badge" alt="Unsiloed AI Support - We're Here to Help with Your Document Processing Needs">
</p>

</div>

<table align="center">
<tr>
<td align="center" width="33%">

### 📧 Email Us
**Get in touch directly**

[hello@unsiloed-ai.com](mailto:hello@unsiloed-ai.com)

<a href="mailto:hello@unsiloed-ai.com">
<img src="https://img.shields.io/badge/Send%20Email-hello@unsiloed--ai.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Unsiloed AI - Get Support for Document Chunking and RAG Solutions">
</a>

</td>
<td align="center" width="33%">

### 📅 Schedule a Call
**Book a discovery session**

[Schedule with our team](https://calendly.com/aman-unsiloed-ai/unsiloed-ai-discovery-call)

<a href="https://calendly.com/aman-unsiloed-ai/unsiloed-ai-discovery-call">
<img src="https://img.shields.io/badge/Book%20a%20Call-Calendly-00A2FF?style=for-the-badge&logo=calendly&logoColor=white" alt="Schedule a Call with Unsiloed AI - Book Discovery Session for Document Processing Solutions">
</a>

</td>
<td align="center" width="33%">

### 🌐 Visit Our Website
**Explore more features**

[www.unsiloed-ai.com](https://www.unsiloed-ai.com/)

<a href="https://www.unsiloed-ai.com/">
<img src="https://img.shields.io/badge/Visit%20Website-unsiloed--ai.com-FF6B6B?style=for-the-badge&logo=web&logoColor=white" alt="Visit Unsiloed AI Website - Learn More About Document Processing and RAG Solutions">
</a>

</td>
</tr>
</table>

<div align="center">


<p align="center">
  <strong>Made with ❤️ by the Unsiloed AI Team</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20for-Developers-blue?style=flat-square" alt="Built for Python Developers and Data Scientists">
  <img src="https://img.shields.io/badge/Open%20Source-Apache--2.0-green?style=flat-square" alt="Open Source Apache 2.0 License - Free Document Chunking Library">
  <img src="https://img.shields.io/badge/AI%20Powered-GPT--4-orange?style=flat-square" alt="AI Powered by GPT-4 and YOLO for Intelligent Document Processing">
</p>


</div>
