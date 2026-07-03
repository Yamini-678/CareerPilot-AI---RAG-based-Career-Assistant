from fastapi import APIRouter
from pydantic import BaseModel 
from app.rag.retriever import retrieve_chunks
from app.llm.gemini import get_gemini_response

router = APIRouter()

class ResumeRequest(BaseModel):
    question: str


@router.post('/ask_resume')
def ask_resume(request: ResumeRequest):

    context = retrieve_chunks(request.question)

    prompt = f""" 
You are an AI Resume Assistant.

Use ONLY the resume context below to answer

Resume Context:
{context}

Question:
{request.question}
"""
    
    answer = get_gemini_response(prompt)

    return {
        "answer" : answer,
        "context" : context
    }