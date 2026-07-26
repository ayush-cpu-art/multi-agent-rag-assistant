from fastapi import APIRouter, HTTPException

from app.rag.vectorstore import VectorStore

router = APIRouter()


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):

    try:

        vectorstore = VectorStore()

        deleted = vectorstore.delete_document(
            document_id
        )

        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Document not found."
            )

        return {

            "success": True,

            "message": "Document deleted successfully."

        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )