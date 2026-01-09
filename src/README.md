# 🧠 Source Code Overview

This folder contains all Python modules required to run the PDF-based RAG assistant using LangGraph and MCP-style tools.

Each file is responsible for a specific part of the pipeline, following a modular and agent-oriented design.

---

## 📂 Files Description

### 🔹 `ingest.py`

Builds the vector database from PDF documents.

**Functions:**
- Loads PDFs from `data/pdfs/`
- Splits text into chunks
- Generates embeddings using sentence transformers
- Stores embeddings in FAISS vector database (`db/`)

Run this first after adding or changing PDFs:

```bash
python src/ingest.py

