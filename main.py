from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Book:
    title = str
    course_code = str
    condition = str
    price = float

def get_books (user_code = str, books=[Book], sort_form = str) -> list[str]:
    new_book_list = []
    for book in books:
        if book.course_code == user_code:
            new_book_list.append(book)
            if sort_form == "title":
                new_book_list.sort(book.title)
            if sort_form == "price":
                new_book_list.sort(book.price)
    return new_book_list