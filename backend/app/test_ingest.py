from rag.ingest import DocumentIngestor

chunks = DocumentIngestor.ingest("rag/uploads/Assignment-4(23-24 July).pdf")   # Replace with your PDF name

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])