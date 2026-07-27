class EmbeddingGenerator:

    def __init__(self):

        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate_embeddings(self, chunks):

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        print("\n" + "=" * 60)
        print("🧠 EMBEDDINGS GENERATED")
        print("=" * 60)
        print(f"Chunks : {len(chunks)}")
        print(f"Embedding Dimension : {embeddings.shape[1]}")
        print("=" * 60 + "\n")

        return embeddings