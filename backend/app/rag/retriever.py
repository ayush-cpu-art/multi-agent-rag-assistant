import re

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
)

from app.core.qdrant import client


class Retriever:

    def __init__(self):

        from sentence_transformers import SentenceTransformer

        self.collection_name = "documents"

        self.client = client

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def extract_document_ids(self, query: str):

        matches = re.findall(
            r"assignment\s*-?\s*(\d+)",
            query,
            re.IGNORECASE
        )

        document_ids = []

        for number in matches:

            document_ids.append(
                f"assignment-{number}"
            )

        return list(set(document_ids))

    def retrieve(self, query, limit=8):

        print("\n" + "=" * 60)
        print("🔎 RETRIEVER")
        print("=" * 60)
        print("Query :", query)

        query_vector = self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()

        document_ids = self.extract_document_ids(query)

        search_filter = None

        if document_ids:

            print("\n📄 Searching Documents:")

            for doc in document_ids:
                print("•", doc)

            search_filter = Filter(

                should=[

                    FieldCondition(
                        key="document_id",
                        match=MatchValue(
                            value=doc
                        )
                    )

                    for doc in document_ids

                ]

            )

        else:

            print("\n🌍 Searching all uploaded documents")

        results = self.client.query_points(

            collection_name=self.collection_name,

            query=query_vector,

            query_filter=search_filter,

            limit=limit

        )

        if (
            not hasattr(results, "points")
            or len(results.points) == 0
        ):

            print("❌ No matching chunks found.")

            return []

        documents = []

        print(f"\n✅ Retrieved {len(results.points)} chunks\n")

        for point in results.points:

            payload = point.payload or {}

            documents.append({

                "text": payload.get(
                    "text",
                    ""
                ),

                "document": payload.get(
                    "document",
                    "Unknown"
                ),

                "document_id": payload.get(
                    "document_id",
                    ""
                ),

                "chunk_id": payload.get(
                    "chunk_id",
                    0
                ),

                "score": round(
                    point.score,
                    4
                )

            })

        return documents