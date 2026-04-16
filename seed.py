from sqlalchemy.orm import sessionmaker
from app.db.database import engine
from app.models.models import Book


Session = sessionmaker(bind=engine)


def seed_books():
    session = Session()

    books = [
        Book(
            title="Clean Code",
            author="Robert C. Martin",
            genre="Programming",
            year=2008,
            rating=4.7,
        ),
        Book(
            title="The Pragmatic Programmer",
            author="Andrew Hunt",
            genre="Programming",
            year=1999,
            rating=4.6,
        ),
        Book(
            title="Atomic Habits",
            author="James Clear",
            genre="Self-help",
            year=2018,
            rating=4.8,
        ),
        Book(
            title="1984", author="George Orwell", genre="Fiction", year=1949, rating=4.5
        ),
        Book(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            genre="Fiction",
            year=1960,
            rating=4.6,
        ),
        Book(
            title="Sapiens",
            author="Yuval Noah Harari",
            genre="History",
            year=2011,
            rating=4.7,
        ),
        Book(
            title="Deep Work",
            author="Cal Newport",
            genre="Productivity",
            year=2016,
            rating=4.5,
        ),
        Book(
            title="Python Crash Course",
            author="Eric Matthes",
            genre="Programming",
            year=2015,
            rating=4.6,
        ),
        Book(
            title="Rich Dad Poor Dad",
            author="Robert Kiyosaki",
            genre="Finance",
            year=1997,
            rating=4.4,
        ),
        Book(
            title="The Alchemist",
            author="Paulo Coelho",
            genre="Fiction",
            year=1988,
            rating=4.3,
        ),
    ]

    session.add_all(books)
    session.commit()
    session.close()

    print("✅ Books seeded successfully!")


if __name__ == "__main__":
    seed_books()
