# My RAG Workshop

A simple Python project demonstrating **Retrieval-Augmented Generation (RAG)** using LangChain, Hugging Face embeddings, and Chroma.

## Features
- Convert text documents into embeddings with `all-MiniLM-L6-v2`.
- Store embeddings in a Chroma vector database.
- Perform semantic search with top-K results.
- Auto-load existing database or create a new one.

## Requirements
```bash

pip install langchain langchain-huggingface langchain-community chromadb sentence-transformers

