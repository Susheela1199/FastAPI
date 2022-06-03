from typing import Optional
from fastapi import FastAPI

#pip install fastapi
#pip install uvicorn[standard]
#uvicorn pythonscriptname:app --reload

# uvicorn sampleapi:app --reload
# http://127.0.0.1:8000/openapi.json - 
# http://127.0.0.1:8000/docs - this give the documentation of ur api automatically using swagger ui. for fast api swagger ui is inbuilt

#for any rest api there is a standard given by openapi

# 1. we have a definite url path eg: 127.0.0.1:8000/assignment - this is the url path
# 2 types of parameters: path parameters(we define the parameters inside the path), 
# query parameters(we dont query the variable inside the path)
#when we go for path parameter, there wont be any ?

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

# @app.get("/")
# async def simple_api():
#     return {"FastAPI : This is first api"}

@app.get("/{book_name}")
async def read_book(book_name:str):
     return BOOKS[book_name]

@app.get("/books/mybook")
async def read_all_books(skip_book: Optional[str]=None):
    if skip_book:
        new_book = BOOKS.copy()
        del new_book[skip_book]
        return new_book
    else:
        return BOOKS

# put is used to add value into the database
@app.put("/{book_name}")
async def add_book_temp(book_name : str, book_title: str, book_author: str):
    book_info= {"title":book_title,"author":book_author}
    BOOKS[book_name] = book_info
    return book_info