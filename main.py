from dataclasses import dataclass



@dataclass
class Book:
    title = str
    course_code = str
    condition = str

@dataclass
class Class:
    name: str
    course_code = str

def get_books (user_book=Book, books=[Book]) -> list[str]:
    new_book_list = []
    for book in books:
        if user_book.course_code == book.course_code:
            new_book_list.append(user_book)
    return new_book_list

