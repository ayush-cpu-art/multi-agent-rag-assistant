from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:

    @staticmethod
    def chunk_text(text: str):

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,
            chunk_overlap=150,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],

            length_function=len

        )

        chunks = splitter.split_text(text)

        # Remove empty chunks
        chunks = [
            chunk.strip()
            for chunk in chunks
            if chunk.strip()
        ]

        print("\n" + "=" * 60)
        print("📚 CHUNKING COMPLETE")
        print("=" * 60)
        print(f"Total Chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):
            print(f"\n----- Chunk {i+1} -----")
            print(chunk[:300])

        print("=" * 60 + "\n")

        return chunks