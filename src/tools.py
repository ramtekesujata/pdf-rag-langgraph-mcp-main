from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DB_PATH = "db"

emb = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

db = FAISS.load_local(DB_PATH, emb, allow_dangerous_deserialization=True)

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DB_PATH = "db"

emb = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

db = FAISS.load_local(DB_PATH, emb, allow_dangerous_deserialization=True)

def search_docs(query: str) -> str:
    docs_scores = db.similarity_search_with_score(query, k=5)

    # FAISS: lower score = better match
    good = []
    for d, score in docs_scores:
        if score < 0.8:   # 🔥 strict relevance threshold
            good.append(d.page_content)

    if len(good) >= 2:
        return "\n\n".join(good)

    if len(good) == 1:
        return good[0]

    return "NO_CONTEXT"

