# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    """Data required to create a book."""

    title: str
    author: str
    publication_year: int = Field(..., ge=1000, le=9999)


class Book(BookCreate):
    """Book data returned by the API."""

    id: int


books: list[Book] = []
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    """Return all books."""
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    """Return one book by ID."""
    # TODO: Find the book and raise HTTPException(status_code=404) if missing.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_data: BookCreate) -> Book:
    """Create and return a book."""
    global next_book_id

    # TODO: Create a Book with the next ID, save it, and return it.
    raise NotImplementedError


# Run with: uvicorn starter-code:app --reload
