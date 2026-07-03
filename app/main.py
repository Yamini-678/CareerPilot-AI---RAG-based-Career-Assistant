from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from app.routes.resume_chat import router as resume_router
from app.routes.career import router as career_router


app = FastAPI(title = "Career Agent")

app.include_router(upload_router)

app.include_router(resume_router)

app.include_router(career_router)

@app.get('/')
def home():
    return {"status" : "Career Agent running!"}

