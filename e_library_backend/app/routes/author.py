from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from e_library_backend.app.database.connection import SessionLocal
from e_library_backend.app.database import schemas, models
from e_library_backend.app.utils.file_handler import save_file
from e_library_backend.app.utils.jwt_helper import get_current_user
from fastapi import status

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/upload-book', response_model=schemas.BookOut)
def upload_book(
    title: str,
    description: str,
    cover: UploadFile = File(...),
    pdf: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_data: dict = Depends(get_current_user)
):
    user = db.query(models.User).filter(models.User.email == user_data["sub"]).first()
    if user.role != models.UserRole.author:
        raise HTTPException(status_code=403, detail="Only authors can upload books.")
    cover_url = save_file(cover, 'cover')
    file_url = save_file(pdf, 'pdf')
    book = models.Book(
        title=title,
        description=description,
        cover_url=cover_url,
        file_url=file_url,
        author_id=user.id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
