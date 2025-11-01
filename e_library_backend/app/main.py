from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from e_library_backend.app.routes import auth, author, admin, books
from e_library_backend.app.database.connection import Base, engine
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Library API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(author.router, prefix="/author", tags=["Author"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(books.router, prefix="/books", tags=["Books"])


@app.get("/")
def read_root():
   return {"message": "Welcome to the E-Library API"}