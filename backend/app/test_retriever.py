from app.rag.retriever import Retriever

retriever = Retriever()

query = input("Ask a question: ")

results = retriever.retrieve(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"\n------ Chunk {i} ------\n")
    print(chunk)