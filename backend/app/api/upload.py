import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.rag.ingest import DocumentIngestor

router = APIRouter()

UPLOAD_DIR = "app/rag/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are allowed."
        )

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingestor = DocumentIngestor()
    chunks, embeddings = ingestor.ingest(filepath)

    return {
        "filename": file.filename,
        "chunks_created": len(chunks),
        "embeddings_created": len(embeddings),
        "message": "Document uploaded and processed successfully."
    }