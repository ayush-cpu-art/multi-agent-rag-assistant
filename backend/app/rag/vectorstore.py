import uuid

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    PointIdsList,
)

from app.core.qdrant import client


class VectorStore:

    def __init__(self):

        self.client = client
        self.collection_name = "documents"

        self.create_collection()

    def create_collection(self):

        collections = self.client.get_collections().collections

        names = [
            collection.name
            for collection in collections
        ]

        if self.collection_name not in names:

            self.client.create_collection(

                collection_name=self.collection_name,

                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )

            )

            print("✅ Qdrant collection created.")

        else:

            print("✅ Using existing Qdrant collection.")

    def add_documents(
        self,
        chunks,
        embeddings,
        document_name
    ):

        document_id = (
            document_name
            .lower()
            .replace(".pdf", "")
            .replace(".docx", "")
            .replace(".txt", "")
            .split("(")[0]
            .strip()
        )

        self.delete_document(document_id)

        points = []

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            points.append(

                PointStruct(

                    id=str(uuid.uuid4()),

                    vector=embedding.tolist(),

                    payload={

                        "text": chunk,

                        "document": document_name,

                        "document_id": document_id,

                        "chunk_id": index + 1

                    }

                )

            )

        self.client.upsert(

            collection_name=self.collection_name,

            points=points

        )

        print("\n" + "=" * 60)
        print("📦 DOCUMENT STORED")
        print("=" * 60)
        print("Document :", document_name)
        print("Document ID :", document_id)
        print("Chunks :", len(points))
        print("=" * 60 + "\n")

    def delete_document(
        self,
        document_id
    ):

        print("\n" + "=" * 60)
        print("🗑 DELETE DOCUMENT")
        print("=" * 60)
        print("Searching :", document_id)

        points, _ = self.client.scroll(

            collection_name=self.collection_name,

            limit=10000,

            with_payload=True,

            with_vectors=False

        )

        point_ids = []

        print("\nStored Documents")

        for point in points:

            payload = point.payload or {}

            print(payload)

            if payload.get("document_id") == document_id:

                point_ids.append(point.id)

        if len(point_ids) == 0:

            print("❌ Document not found.")

            return False

        self.client.delete(

            collection_name=self.collection_name,

            points_selector=PointIdsList(
                points=point_ids
            )

        )

        print(f"✅ Deleted {len(point_ids)} chunks.")

        return True

    def get_documents(self):

        points, _ = self.client.scroll(

            collection_name=self.collection_name,

            limit=10000,

            with_payload=True,

            with_vectors=False

        )

        documents = {}

        for point in points:

            payload = point.payload or {}

            name = payload.get(
                "document",
                "Unknown"
            )

            if name not in documents:

                documents[name] = 1

            else:

                documents[name] += 1

        return documents

    def collection_info(self):

        print(

            self.client.get_collection(
                self.collection_name
            )

        )