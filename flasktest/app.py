from flask import render_template, Flask, url_for, render_template, request, redirect
import sqlite3

from dataclasses import dataclass

@dataclass
class Book:
    title:str
    course_code:str
    condition:str
    price:float
    owner_email:str



app = Flask(__name__)

def get_books (user_code:str, books: [Book]) -> [Book]:
    # makes a new list of the books that correspond with the course code entered
    new_book_list = []
    for book in books:
        if book.course_code == user_code:
            new_book_list.append(book)
    return new_book_list





@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form["search_bar"]
        return redirect(url_for("results", search_request=search))
    else:
        return render_template(
        "index.html"
    )



@app.route("/<search_request>")
def results(search_request):
    books_for_sale = get_books(search_request)
    return render_template("results.html", books_for_sale=books_for_sale)

@app.route("/sell")
def sellpage():
    return render_template("")