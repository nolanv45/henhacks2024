from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Book:
    title:str
    course_code:str
    condition:str
    price:float
    owner_email:str

def get_books (user_code:str, books: [Book]) -> [Book]:
    # makes a new list of the books that correspond with the course code entered
    new_book_list = []
    for book in books:
        if book.course_code == user_code:
            new_book_list.append(book)
    return new_book_list

def submit (user_owner_email = str, user_title = str, user_condition = str, user_course_code = str, user_price = float) -> Book:
    # submits the user's information into a book that then can be appended to the overall book list
    return Book(user_title, user_course_code, user_condition, user_price, user_owner_email) 

assert_equal (get_books("CISC106", [Book("Computer Science Textbook","CISC106","New",63.99, "ryansven@udel.edu"),
                      Book("Computer Science Journal","CISC106","Used",1.99,"ryansven@udel.edu"),
                      Book("Computer Science Book","CISC108", "New",103.99,"ryansven@udel.edu")]), 
                      [Book("Computer Science Textbook","CISC106","New",63.99,"ryansven@udel.edu"),
                      Book("Computer Science Journal","CISC106","Used",1.99,"ryansven@udel.edu")])