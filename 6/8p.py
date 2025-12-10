import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, Field


app = FastAPI()


class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=200,
                       description="Название книги")
    author: str = Field(..., min_length=2, max_length=100,
                        description="Автор книги")
    year: int = Field(..., ge=1000, le=2100,
                      description="Год издания")


books = []


@app.post(
    "/add",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Книга успешно добавлена"}
    }
)
def add_book(book: Book):
    books.append(book)
    return {
        "message": "Книга добавлена",
        "book": book.dict(),
    }


@app.get("/books")
def get_books():
    return {"books": books}


uvicorn.run(app)
