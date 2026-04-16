from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float

from app.db.base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    genre: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)
