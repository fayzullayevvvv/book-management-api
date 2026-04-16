from fastapi import FastAPI

from app.api.v1.endpoints.book import router as book_router
from app.db.database import create_tables, drop_tables


# drop_tables()
# create_tables()


app = FastAPI(title="Book Management")
app.include_router(book_router)


@app.get("/")
async def health_check():
    return {"message": "ok"}
