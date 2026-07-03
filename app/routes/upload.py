from fastapi import APIRouter, UploadFile , File
from app.rag.loader import extract_text
from app.rag.vector_store import create_vector_store
import shutil
import os

router = APIRouter()

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok = True)

@router.post('/upload')
async def upload_file(file : UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path , 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)

    chunks = create_vector_store(text)

    return {
        "filename" : file.filename,
        "characters" : len(text),
        "chunks" : chunks,
        "message" : "Vector db created successfully"
    }