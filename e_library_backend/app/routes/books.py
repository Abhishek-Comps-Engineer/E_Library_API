from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from e_library_backend.app.database.connection import SessionLocal
from e_library_backend.app.database import models, schemas
from e_library_backend.app.utils.jwt_helper import get_current_user
from fastapi.responses import FileResponse
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/', response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db), user_data: dict = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.email == user_data["sub"]).first()
    if user.role == models.UserRole.reader:
        books = db.query(models.Book).filter(models.Book.status == models.BookStatus.approved).all()
    else:
        books = db.query(models.Book).all()
    return books

@router.get('/download/{book_id}')
def download_book(book_id: int, db: Session = Depends(get_db), user_data: dict = Depends(get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book or book.status != models.BookStatus.approved:
        raise HTTPException(status_code=404, detail="Book not available.")
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'pdfs', os.path.basename(book.file_url))
    return FileResponse(file_path, media_type='application/pdf', filename=os.path.basename(file_path))
