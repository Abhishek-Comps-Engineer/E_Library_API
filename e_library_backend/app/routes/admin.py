from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from e_library_backend.app.database.connection import SessionLocal
from e_library_backend.app.database import models, schemas
from e_library_backend.app.utils.jwt_helper import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/pending-books', response_model=list[schemas.BookOut])
def get_pending_books(db: Session = Depends(get_db), user_data: dict = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.email == user_data["sub"]).first()
    if user.role != models.UserRole.admin:
        raise HTTPException(status_code=403, detail="Only admins can view pending books.")
    books = db.query(models.Book).filter(models.Book.status == models.BookStatus.pending).all()
    return books

@router.post('/review-book/{book_id}')
def review_book(book_id: int, approve: bool, comment: str = "", db: Session = Depends(get_db), user_data: dict = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.email == user_data["sub"]).first()
    if user.role != models.UserRole.admin:
        raise HTTPException(status_code=403, detail="Only admins can review books.")
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    book.status = models.BookStatus.approved if approve else models.BookStatus.rejected
    book.admin_comment = comment
    db.commit()
    return {"detail": "Book reviewed."}
