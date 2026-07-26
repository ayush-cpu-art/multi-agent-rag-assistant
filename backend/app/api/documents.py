from collections import defaultdict

from fastapi import APIRouter, HTTPException

from app.rag.vectorstore import VectorStore

router = APIRouter()


@router.get("/documents")
def get_documents():

    try:

        vectorstore = VectorStore()

        points, _ = vectorstore.client.scroll(
            collection_name=vectorstore.collection_name,
            limit=1000,
            with_vectors=False
        )

        document_map = defaultdict(int)

        for point in points:

            payload = point.payload or {}

            document_name = payload.get(
                "document",
                "Unknown Document"
            )

            document_map[document_name] += 1

        documents = []

        for name in sorted(document_map.keys()):

            documents.append({

                "name": name,

                "chunks": document_map[name]

            })

        print("\n" + "=" * 60)
        print("📂 DOCUMENT LIST")
        print("=" * 60)

        for doc in documents:
            print(f"{doc['name']}  |  {doc['chunks']} chunks")

        print("=" * 60 + "\n")

        return {
            "total_documents": len(documents),
            "documents": documents
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )