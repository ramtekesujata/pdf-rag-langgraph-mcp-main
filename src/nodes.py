import re
from tools import search_docs

def retrieve_node(state):
    ctx = search_docs(state["question"])
    return {"context": ctx}

import re
from tools import search_docs

def retrieve_node(state):
    ctx = search_docs(state["question"])
    return {"context": ctx}

def answer_node(state):

    if state["context"] == "NO_CONTEXT":
        return {
            "answer": "❗ No answer found in the provided PDF documents."
        }

    ctx = state["context"]

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', ctx)

    # Take first 6 relevant sentences only
    summary = sentences[:6]

    answer = "Answer based on the PDFs:\n\n" + "\n".join(summary)
    return {"answer": answer}

def cite_node(state):
    if "No answer found" in state["answer"]:
        return {"final": state["answer"]}

    return {
        "final": state["answer"] + "\n\nSources: Uploaded PDF documents"
    }

