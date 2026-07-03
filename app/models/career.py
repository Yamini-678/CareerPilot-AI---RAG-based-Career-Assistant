from pydantic import BaseModel

class CareerRequest(BaseModel):
    type : str
    goal : str
    current_skills : str
    duration : str | None = None