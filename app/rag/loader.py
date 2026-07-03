from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text(file_path : str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == '.pdf':
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    
    elif suffix == '.docx':
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    
    else:
        raise ValueError("Unsupported File Type")