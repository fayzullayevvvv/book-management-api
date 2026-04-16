from typing import Generator

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.models.models import Base


url = URL.create(
    drivername="postgresql+psycopg2",
    host=settings.db_host,
    port=settings.db_port,
    username=settings.db_user,
    password=settings.db_pass,
    database=settings.db_name,
)
engine = create_engine(url)
SessionLocal = sessionmaker(engine)


def create_tables():
    Base.metadata.create_all(bind=engine)


def drop_tables():
    Base.metadata.drop_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
