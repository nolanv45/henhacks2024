from flask import render_template, Flask, url_for, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField

from dataclasses import dataclass

@dataclass
class Book:
    title:str
    course_code:str
    condition:str
    price:float
    owner_email:str



class SellForm(FlaskForm):
    title = StringField('Title')
    course_code = StringField('Course Code')
    condition = StringField('Condition')
    price = FloatField('Price')
    email = StringField('Email')
    submit = SubmitField('Submit')








app = Flask(__name__)
app.config['SECRET_KEY'] = 'theawesomekey'


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
    books_for_sale = search_request
    return render_template("results.html", books=books_for_sale)



def sell_data_dictionary(dictionary) -> tuple:
    new_list = []
    for key in dictionary:
        new_list.append(dictionary[key])
    print(tuple(new_list))
    return tuple(new_list)





@app.route("/sell", methods=['GET', 'POST'])
def sellpage():
    form = SellForm()
    if form.is_submitted():
        result = request.form
        sell_data_dictionary(result)
        return render_template("index.html", result=result)
    return render_template("sell.html", form=form)