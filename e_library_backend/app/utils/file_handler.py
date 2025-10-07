import os
from fastapi import UploadFile
from uuid import uuid4
from typing import Literal

STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
COVERS_DIR = os.path.join(STATIC_DIR, 'covers')
PDFS_DIR = os.path.join(STATIC_DIR, 'pdfs')

os.makedirs(COVERS_DIR, exist_ok=True)
os.makedirs(PDFS_DIR, exist_ok=True)

def save_file(file: UploadFile, file_type: Literal['cover', 'pdf']) -> str:
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{ext}"
    if file_type == 'cover':
        path = os.path.join(COVERS_DIR, filename)
        url = f"/static/covers/{filename}"
    else:
        path = os.path.join(PDFS_DIR, filename)
        url = f"/static/pdfs/{filename}"
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())
    return url
