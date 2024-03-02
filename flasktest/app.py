from flask import render_template, Flask, url_for, render_template, request, redirect


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
        return redirect(url_for("sellpage", search_request=search))
    else:
        return render_template(
        "index.html"
    )



@app.route("/<search_request>")
def sellpage(search_request):

    return f"<h1>{search_request}</h1>"

@app.route("/results")
def results():
    return render_template("", entries=searchedItem)