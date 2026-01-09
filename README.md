
# PDF RAG Assistant using LangGraph and MCP-style Tools

This project implements a simple Retrieval-Augmented Generation (RAG) system over PDF documents using:

- LangChain (document loading, embeddings, vector store)
- FAISS (local vector database)
- LangGraph (workflow orchestration)
- MCP-style tools (retrieval exposed as tool interface)

The system answers questions strictly from uploaded PDFs and explicitly reports when an answer is not found.

---

## Workflow

User Question  
→ LangGraph Retrieve Node (calls MCP-style retrieval tool)  
→ Draft Answer Node (extractive summarization)  
→ Cite Sources Node  
→ Final Answer

---

## 📁 Project Structure

- `data/pdfs/` — Place all PDF documents here  
- `src/ingest.py` — Build the vector database from PDFs  
- `src/tools.py` — MCP-style retrieval tool  
- `src/nodes.py` — LangGraph processing nodes  
- `src/graph.py` — LangGraph workflow definition  
- `src/run.py` — Interactive Q&A application  
