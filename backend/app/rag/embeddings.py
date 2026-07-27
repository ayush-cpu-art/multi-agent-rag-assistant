from fastembed import TextEmbedding


class EmbeddingGenerator:

    def __init__(self):

        self.model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def generate_embeddings(self, chunks):

        embeddings = list(
            self.model.embed(chunks)
        )

        print("\n" + "=" * 60)
        print("🧠 EMBEDDINGS GENERATED")
        print("=" * 60)
        print(f"Chunks : {len(chunks)}")
        print(f"Embedding Dimension : {len(embeddings[0])}")
        print("=" * 60 + "\n")

        return embeddings