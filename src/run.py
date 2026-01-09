from graph import app

print("PDF RAG Assistant (LangGraph + MCP-style Tools)")
print("Type 'exit' to quit.\n")

while True:
    q = input("Ask: ")
    if q.lower() == "exit":
        break

    out = app.invoke({"question": q})
    print("\nANSWER:\n", out["final"], "\n")

