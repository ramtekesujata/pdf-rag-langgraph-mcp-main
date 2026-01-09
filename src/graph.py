from langgraph.graph import StateGraph, END
from typing import TypedDict

from nodes import retrieve_node, answer_node, cite_node

class RAGState(TypedDict):
    question: str
    context: str
    answer: str
    final: str

g = StateGraph(RAGState)

g.add_node("retrieve", retrieve_node)
g.add_node("answer", answer_node)
g.add_node("cite", cite_node)

g.set_entry_point("retrieve")
g.add_edge("retrieve", "answer")
g.add_edge("answer", "cite")
g.add_edge("cite", END)

app = g.compile()

