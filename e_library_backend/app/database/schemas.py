from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum

class UserRole(str, Enum):
    reader = "reader"
    author = "author"
    admin = "admin"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class BookStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    cover_url: Optional[str]
    file_url: Optional[str]
    author_id: int
    status: BookStatus
    admin_comment: Optional[str]
    class Config:
        orm_mode = True
