from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unsiloed-parser",
    version="0.1.4",
    author="Unsiloed AI",
    author_email="hello@unsiloed-ai.com",
    description="Unsiloed Parser: Open-source Python library for advanced document chunking. Transform PDFs, DOCX, images, and more into LLM-ready chunks using semantic AI, YOLO segmentation, and OCR for RAG pipelines and workflow automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Unsiloed-AI/Unsiloed-Parser",
    packages=find_packages(include=["Unsiloed", "Unsiloed.*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "uvicorn",
        "fastapi",
        "python-multipart",
        "python-dotenv",
        "pdf2image",
        "Pillow",
        "PyPDF2",
        "python-docx",
        "python-pptx",
        "openai",
        "numpy",
        "opencv-python-headless",
        "requests",
        "ultralytics",
        "pytesseract",
        "beautifulsoup4",
        "markdown",
        "lxml",
        "html2text",
        "aiohttp",
        "validators",
        "huggingface-hub",
    ],
    entry_points={
        "console_scripts": [
            "Unsiloed=Unsiloed.cli:main",
        ],
    },
) 