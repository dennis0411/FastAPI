from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(gt=-1, lt=101)
    class Config:
        schema_extra = {
            "example": {
                "id": "5772c21f-1183-411d-b32d-0b3b83a9f9a7",
                "title": "Harry Potter",
                "author": "J.K.",
                "description": "magic",
                "rating": 100
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted.'


def create_books_no_api():
    book_1 = Book(id="50cdda97-3683-4b89-8a9d-bc2fd7aa20ab",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="0cec8adc-faaf-4904-9093-521d4a134370",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="39906564-9857-4912-b7e5-7f08f08d052c",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
