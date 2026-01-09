# 📄 PDF RAG Assistant using LangGraph and MCP-style Tools

This project implements a **Retrieval-Augmented Generation (RAG)** system for answering questions from PDF documents using a structured, tool-driven workflow built with **LangGraph** and **MCP-style tools**.

The assistant retrieves answers **strictly from the provided PDFs** and clearly indicates when the information is **not present in the documents**.

---

## 🚀 Features

- 📚 PDF document ingestion and chunking  
- 🔎 Vector-based semantic search using FAISS  
- 🧠 LangGraph workflow for multi-step reasoning  
- 🛠️ MCP-style retrieval exposed as a tool interface  
- 📌 Source-aware, extractive-style answers  

---

## 🧩 Tech Stack

- **LangChain** — PDF loading, chunking, embeddings  
- **FAISS** — Local vector database  
- **LangGraph** — Workflow orchestration  
- **Python** — Core implementation  

---

## 🔁 Workflow

```text
User Question
   ↓
Retrieve Node (MCP-style retrieval tool)
   ↓
Draft Answer Node (extractive summarization)
   ↓
Cite Sources Node
   ↓
Final Answer
```

---

## 📁 Project Structure

```text
data/pdfs/        → Place all PDF documents here
src/ingest.py     → Build / update vector database from PDFs
src/tools.py      → MCP-style retrieval tool
src/nodes.py      → LangGraph processing nodes
src/graph.py      → LangGraph workflow definition
src/run.py        → Interactive Q&A application
```

---

## ⚙️ Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ramtekesujata/pdf-rag-langgraph-mcp-main.git
cd pdf-rag-langgraph-mcp-main
```

---

### 2️⃣ Install Dependencies

Using **Conda**:

```bash
conda env create -f environment.yml
conda activate pdf-rag
```

Using **pip**:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### ✅ First-Time Setup or After Adding New PDFs

Whenever you **run the project for the first time** or **add new PDF files**, you must build the vector database:

```bash
python3 src/ingest.py
```

This step:

- Loads PDFs from `data/pdfs/`
- Splits them into chunks
- Creates embeddings
- Stores them in the FAISS vector database

---

### ✅ Start the Question–Answer Assistant

After ingestion is complete:

```bash
python3 src/run.py
```

Then type your questions in the terminal to query the PDFs.

---

### 🔁 When Do You Need to Run `ingest.py` Again?

| Situation                  | What to Run                                         |
|---------------------------|-----------------------------------------------------|
| First time running project | `python3 src/ingest.py` → then `python3 src/run.py` |
| Added or updated PDFs      | `python3 src/ingest.py` → then `python3 src/run.py` |
| Only asking new questions  | Only `python3 src/run.py`                           |

---

## ⚠️ Notes

- The assistant does **not hallucinate** beyond the content of the PDFs.
- If relevant information is not found, it will clearly report that.
- Ingestion time depends on the size and number of PDFs.

---

## 📌 Future Improvements

- Web-based UI using Streamlit or Gradio
- Metadata-based filtering
- Hybrid keyword + semantic retrieval
- Highlighted citations in answers

---

## 📜 License

This project is intended for educational and research purposes.

