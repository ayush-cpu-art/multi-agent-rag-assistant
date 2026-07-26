from app.rag.vectorstore import VectorStore

db = VectorStore()

info = db.client.get_collection("documents")

print(info)