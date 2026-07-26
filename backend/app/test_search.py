from app.rag.retriever import Retriever

retriever = Retriever()

query = "What dataset is used?"

print(f"Query: {query}")

results = retriever.client.query_points(
    collection_name="documents",
    query=retriever.model.encode(query).tolist(),
    limit=5
)

print("\nRAW RESULT:")
print(results)

if hasattr(results, "points"):
    print("\nPoints:", len(results.points))
    for i, point in enumerate(results.points):
        print(f"\nPoint {i+1}")
        print("Score:", point.score)
        print("Payload:", point.payload)
else:
    print("No points attribute found.")