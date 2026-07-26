from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.documents import router as document_router
from app.api.delete_document import router as delete_router
from app.api.chunk import router as chunk_router


app = FastAPI(
    title="Multi-Agent RAG Assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===========================
# API Routes
# ===========================

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(document_router)
app.include_router(delete_router)
app.include_router(chunk_router)


# ===========================
# Health Check
# ===========================

@app.get("/")
def root():

    return {
        "message": "🚀 Multi-Agent RAG Backend Running"
    }