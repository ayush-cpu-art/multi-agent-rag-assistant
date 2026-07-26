from app.rag.vectorstore import VectorStore

db = VectorStore()

collections = db.client.get_collections()
print("\nCollections:")
print(collections.collections)

info = db.client.get_collection("documents")

print("\nCollection Info:")
print(info)

count = db.client.count(
    collection_name="documents",
    exact=True
)

print("\nTotal Vectors Stored:")
print(count.count)