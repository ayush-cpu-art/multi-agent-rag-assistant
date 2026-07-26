from app.rag.ingest import DocumentIngestor

# Replace with your uploaded PDF filename
PDF_PATH = "rag/uploads/Assignment-4(23-24 July).pdf"

pipeline = DocumentIngestor()

chunks, embeddings = pipeline.ingest(PDF_PATH)

print("=" * 50)
print("Document processed successfully!")
print("=" * 50)

print(f"Total Chunks      : {len(chunks)}")
print(f"Total Embeddings  : {len(embeddings)}")
print(f"Embedding Size    : {len(embeddings[0])}")

print("\nFirst Chunk:\n")
print(chunks[0][:500])