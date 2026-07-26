from app.rag.loader import DocumentLoader

text = DocumentLoader.load_document("rag/uploads/Assignment-4(23-24 July).pdf")

print(text[:1000])