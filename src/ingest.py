from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

DATA_PATH = "../data/pdfs"
DB_PATH = "db"

print("Loading PDFs...")
loader = PyPDFDirectoryLoader(DATA_PATH)
docs = loader.load()
print("Pages:", len(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
chunks = splitter.split_documents(docs)
print("Chunks:", len(chunks))

emb = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

db = FAISS.from_documents(chunks, emb)
db.save_local(DB_PATH)

print("Vector DB saved to:", DB_PATH)

