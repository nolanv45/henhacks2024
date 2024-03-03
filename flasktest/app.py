from flask import render_template, Flask, url_for, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
import sqlite3
from dataclasses import dataclass

@dataclass
class Book:
    title:str
    course_code:str
    condition:str
    price:float
    owner_email:str


#created a sellform through flask to get data from multiple fields back from html
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




#acts as the homepage
@app.route("/")
def index():
    return render_template("index.html")


#about the project information page
@app.route("/about")
def about():
    return render_template("about.html")






#helper function used to turn dictionary response from sell page
#into tuple to be stored in database
def sell_data_dictionary(dictionary) -> tuple:
    new_list = []
    for key in dictionary:
        new_list.append(dictionary[key])
    return tuple(new_list)



#sell page which puts book information from fields into database
@app.route("/sell", methods=['GET', 'POST'])
def sell():
    form = SellForm()
    if form.is_submitted():
        result = sell_data_dictionary(request.form)
        print(result)
        connection = sqlite3.connect("bookdirectory.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books
                    (title TEXT, course_code TEXT, condition TEXT, price REAL, owner_email TEXT, submit TEXT)''')
        cursor.executemany('''INSERT INTO books (title, course_code, condition, price, owner_email, submit) VALUES (?, ?, ?, ?, ?, ?)''', (result,))
        connection.commit()
        for row in cursor.execute ('''SELECT course_code, title, price, condition, owner_email FROM books'''):
            print(row)
        connection.close()
        return redirect(url_for("index"))
    return render_template("sell.html", form=form)


def results_helper(search):
        connection = sqlite3.connect("bookdirectory.db")
        cursor = connection.cursor()
        
        resultlist = []
        for row in cursor.execute ('''SELECT course_code, title, price, condition, owner_email FROM books'''):
            if search in row:
                resultlist.append(row)
        return resultlist


@app.route("/buy", methods=['GET','POST'])
def buy():
    if request.method == "POST":
        search = request.form["search_bar"]
        results = results_helper(search)
        return render_template("results.html", books = results)
    else:
        return render_template("buy.html")
  



            




"""def submit_book (user_title = str, user_course_code = str, user_condition = str, user_price = float, user_owner_email = str):
    # submits the user's information into a book that then can be appended to the overall book list
    new_book_data = [(user_title,user_course_code,user_condition,user_price,user_owner_email)]
    return new_book_data
"""




"""
con = sqlite3.connect("books_for_sale.db",)
cur = con.cursor()

user_data = ("CISC106: Textbook", "CISC106", "New", 100.00, "ryansven@udel.edu")
new_book_data = submit_book(*user_data)




cur.executemany('''INSERT INTO books (title, course_code, condition, price, owner_email) VALUES (?, ?, ?, ?, ?)''', new_book_data)

#cur.executemany('''DELETE FROM books (title, course_code, condition, price, owener_email) WHERE (?, ?, ?, ?, ?)''', removing_book_data)

con.commit()


"""