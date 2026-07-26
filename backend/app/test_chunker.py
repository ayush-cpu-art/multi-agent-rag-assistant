from app.rag.loader import DocumentLoader
from rag.chunker import TextChunker

# Replace this with your uploaded PDF name
text = DocumentLoader.load_document("rag/uploads/sample.pdf")

chunks = TextChunker.chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])