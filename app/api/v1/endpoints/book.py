from typing import List, Annotated

from fastapi import APIRouter, status, Depends, Path, Body, Query
from sqlalchemy.orm import Session

from app.schemas.book import BookResponse, BookCreate, BookUpdate
from app.db.database import get_db
from app.services.book_service import BookService


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def get_all_books_view(db: Annotated[Session, Depends(get_db)]):
    service = BookService(db)
    return service.get_all_books()


@router.get(
    "/search", response_model=List[BookResponse], status_code=status.HTTP_200_OK
)
def search_book_view(
    db: Annotated[Session, Depends(get_db)],
    search: str = Query(..., min_length=1, description="Search by title or author"),
):
    service = BookService(db)
    return service.search_books(search)


@router.get(
    "/filter", response_model=List[BookResponse], status_code=status.HTTP_200_OK
)
def filter_books_view(
    db: Annotated[Session, Depends(get_db)],
    min: int | None = Query(None),
    max: int | None = Query(None),
):
    service = BookService(db)
    return service.filter_books(min, max)


@router.get("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_one_book_view(
    book_id: Annotated[int, Path()], db: Annotated[Session, Depends(get_db)]
):
    service = BookService(db)
    return service.get_book_by_id(book_id)


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book_view(
    data: Annotated[BookCreate, Body()], db: Annotated[Session, Depends(get_db)]
):
    service = BookService(db)
    return service.create_book(data)


@router.put("/{book_id}", response_model=BookResponse)
def update_book_view(
    book_id: Annotated[int, Path()],
    data: BookUpdate,
    db: Annotated[Session, Depends(get_db)],
):
    service = BookService(db)
    return service.update_book(book_id, data)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_view(
    book_id: Annotated[int, Path()], db: Annotated[Session, Depends(get_db)]
):
    service = BookService(db)
    return service.delete_book(book_id)
