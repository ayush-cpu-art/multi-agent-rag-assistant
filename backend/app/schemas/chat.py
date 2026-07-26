from typing import List
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str
    history: List[ChatMessage] = []


class ChatResponse(BaseModel):
    answer: str
    sources: List[str] = []