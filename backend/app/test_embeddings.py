from app.rag.ingest import DocumentIngestor

PDF_PATH = "app/rag/uploads/Assignment-4(23-24 July).pdf"   

pipeline = DocumentIngestor()

chunks, embeddings = pipeline.ingest(PDF_PATH)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")
print(f"Dimension: {len(embeddings[0])}")