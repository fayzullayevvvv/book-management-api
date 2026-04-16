from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.models import Book
from app.schemas.book import BookCreate, BookUpdate


class BookService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_books(self) -> List[Book]:
        return self.db.query(Book).all()

    def get_book_by_id(self, id: int) -> Book:
        book = self.db.query(Book).filter(Book.id == id).first()

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )

        return book

    def create_book(self, data: BookCreate):
        new_book = Book(
            title=data.title,
            author=data.author,
            genre=data.genre,
            year=data.year,
            rating=data.rating,
        )

        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)

        return new_book

    def update_book(self, book_id: int, data: BookUpdate):
        book = self.db.query(Book).filter(Book.id == book_id).first()

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )

        update_data = data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(book, key, value)

        self.db.commit()
        self.db.refresh(book)

        return book

    def delete_book(self, book_id: int):
        book = self.db.query(Book).filter(Book.id == book_id).first()

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
            )

        self.db.delete(book)
        self.db.commit()

        return {"message": "Book deleted successfully"}

    def search_books(self, search: str):
        return (
            self.db.query(Book)
            .filter(
                or_(Book.title.ilike(f"%{search}%"), Book.author.ilike(f"%{search}%"))
            )
            .all()
        )

    def filter_books(self, min_year: int | None, max_year: int | None):
        query = self.db.query(Book)

        if min_year is not None:
            query = query.filter(Book.year >= min_year)

        if max_year is not None:
            query = query.filter(Book.year <= max_year)

        return query.all()
