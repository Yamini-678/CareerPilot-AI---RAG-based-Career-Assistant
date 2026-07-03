from fastapi import APIRouter
from app.models.chat_models import ChatRequest , ChatResponse
from app.services.chat_services import chat_with_llm


router = APIRouter()

@router.post("/chat" , response_model = ChatResponse)
def chat(request : ChatRequest):
    response = chat_with_llm(
        request.session_id,
        request.message
    )
    return ChatResponse(response = response)