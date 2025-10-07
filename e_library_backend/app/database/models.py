from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from e_library_backend.app.database.connection import Base
import enum

class UserRole(str, enum.Enum):
    reader = "reader"
    author = "author"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.reader)
    books = relationship("Book", back_populates="author")

class BookStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    cover_url = Column(String)
    file_url = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(BookStatus), default=BookStatus.pending)
    admin_comment = Column(Text)
    author = relationship("User", back_populates="books")
