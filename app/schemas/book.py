from typing import Optional

from pydantic import BaseModel


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int
    rating: float


class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    rating: float


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
