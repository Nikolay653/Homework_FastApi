from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates
from api.models.book import Book
from api.myutils import my_books

book_router = APIRouter(tags=["api"])
templates = Jinja2Templates(directory="templates")


# Получение списка книг
@book_router.get(
    "/books/",
    summary="Получение всех книг",
    description="Возвращаем все записи из файла с контактами",
)
async def get_books():
    return {"books": my_books}


# Создание новой книги
@book_router.post(
    "/book/add",
    summary="Добавление новой книги",
    description="Добавление новой книги и запись в файл",
)
async def add_movie(book: Book):
    my_books.append(book)
    return {"book": book, "status": "added"}


@book_router.delete(
    "/delete-book-id",
    summary="Удаление книги",
    description="Удаляет запись книги по id",
)
async def delete_contact(book_id: int):
    for i, bok in enumerate(my_books):
        if book_id == bok.id_:
            my_books.pop(i)

    return {"message": "Удалено успешно"}
