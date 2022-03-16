from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Tiltle 1', 'author': 'Auther 1'},
    'book_2': {'title': 'Tiltle 2', 'author': 'Auther 2'},
    'book_3': {'title': 'Tiltle 3', 'author': 'Auther 3'},
    'book_4': {'title': 'Tiltle 4', 'author': 'Auther 4'},
    'book_5': {'title': 'Tiltle 5', 'author': 'Auther 5'},
}


@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}


@app.get("/books/{book_title}")
async def read_books(book_title):
    return {"book_title": book_title}

