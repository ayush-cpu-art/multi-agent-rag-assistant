from fastapi import APIRouter, HTTPException

from app.rag.vectorstore import VectorStore

router = APIRouter()


@router.get("/documents/{document_name}/chunk/{chunk_id}")
def get_chunk(document_name: str, chunk_id: int):

    try:

        vectorstore = VectorStore()

        points, _ = vectorstore.client.scroll(

            collection_name=vectorstore.collection_name,

            limit=10000,

            with_payload=True,

            with_vectors=False

        )

        for point in points:

            payload = point.payload or {}

            if (

                payload.get("document") == document_name

                and

                payload.get("chunk_id") == chunk_id

            ):

                return {

                    "document": document_name,

                    "chunk_id": chunk_id,

                    "text": payload.get("text", "")

                }

        raise HTTPException(

            status_code=404,

            detail="Chunk not found."

        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )