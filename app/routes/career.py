from fastapi import APIRouter
from app.models.career import CareerRequest
from app.services.career_service import career_agent

router = APIRouter()

@router.post('/career')
def career(request : CareerRequest):
    response = career_agent(request)

    return {
        "response" : response
    }

