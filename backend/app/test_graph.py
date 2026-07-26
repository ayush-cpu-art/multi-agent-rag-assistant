from app.graph.workflow import graph

result = graph.invoke(
    {
        "question": "What dataset is used?",
        "context": "",
        "chunks": [],
        "answer": ""
    }
)

print("\n")
print("=" * 60)
print(result["answer"])