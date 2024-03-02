from flask import render_template

from flask import Flask

from flask import request

app = Flask(__name__)
books = []




@app.route("/", methods=["GET", "POST"])
def index():
    print(request.form)
    return render_template(
        "index.html"
    )



@app.route("/sell")
def sellpage():
    return render_template(
        ""
    )

@app.route("/results")
def results():
    return render_template(
        ""
    )