import os

from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.embeddings import EmbeddingGenerator
from app.rag.vectorstore import VectorStore


class DocumentIngestor:

    def __init__(self):

        self.embedder = EmbeddingGenerator()
        self.vectorstore = VectorStore()

    def ingest(self, file_path):

        text = DocumentLoader.load_document(file_path)

        chunks = TextChunker.chunk_text(text)

        embeddings = self.embedder.generate_embeddings(chunks)
        self.vectorstore.add_documents(
            chunks=chunks,
            embeddings=embeddings,
            document_name=os.path.basename(file_path)
        )

        print("\n" + "=" * 60)
        print("✅ DOCUMENT INGESTION COMPLETE")
        print("=" * 60)
        print(f"Document   : {os.path.basename(file_path)}")
        print(f"Characters : {len(text)}")
        print(f"Chunks     : {len(chunks)}")
        print(f"Embeddings : {len(embeddings)}")
        print("=" * 60 + "\n")

        return chunks, embeddings