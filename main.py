from dataclasses import dataclass
from bakery import assert_equal
import sqlite3


@dataclass
class Book:
    title:str
    course_code:str
    condition:str
    price:float
    owner_email:str

def get_books (user_code:str, books: list[Book]) -> list[Book]:
    # makes a new list of the books that correspond with the course code entered
    new_book_list = []
    for book in books:
        if book.course_code == user_code:
            new_book_list.append(book)
    return new_book_list

def submit_book (user_title = str, user_course_code = str, user_condition = str, user_price = float, user_owner_email = str):
    # submits the user's information into a book that then can be appended to the overall book list
    new_book_data = [(user_title,user_course_code,user_condition,user_price,user_owner_email)]
    return new_book_data

def remove_book (user_title = str, user_course_code = str, user_condition = str, user_price = float, user_owner_email = str):
    removing_book_data = [(user_title,user_course_code,user_condition,user_price,user_owner_email)]
    return removing_book_data

assert_equal (get_books("CISC106", [Book("Computer Science Textbook","CISC106","New",63.99, "ryansven@udel.edu"),
                      Book("Computer Science Journal","CISC106","Used",1.99,"ryansven@udel.edu"),
                      Book("Computer Science Book","CISC108", "New",103.99,"ryansven@udel.edu")]), 
                      [Book("Computer Science Textbook","CISC106","New",63.99,"ryansven@udel.edu"),
                      Book("Computer Science Journal","CISC106","Used",1.99,"ryansven@udel.edu")])

con = sqlite3.connect("books_for_sale.db")
cur = con.cursor()

user_data = ("CISC106: Textbook", "CISC106", "New", 100.00, "ryansven@udel.edu")
new_book_data = submit_book(*user_data)
removing_book_data = remove_book (*user_data)

cur.execute('''CREATE TABLE IF NOT EXISTS books
                    (title TEXT, course_code TEXT, condition TEXT, price REAL, owner_email TEXT)''')

#cur.executemany('''INSERT INTO books (title, course_code, condition, price, owner_email) VALUES (?, ?, ?, ?, ?)''', new_book_data)

#cur.executemany('''DELETE FROM books (title, course_code, condition, price, owener_email) WHERE (?, ?, ?, ?, ?)''', removing_book_data)

con.commit()

