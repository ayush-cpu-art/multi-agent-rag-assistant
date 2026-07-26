from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.graph.workflow import graph

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "history": request.history,
            "plan": "",
            "rewritten_query": "",
            "documents": [],
            "context": "",
            "answer": "",
            "sources": []
        }
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )