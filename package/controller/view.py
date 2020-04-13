from package.base.app import webapp, viewBp
from datetime import datetime
from flask import render_template
@viewBp.route("/")
def home():
    return render_template("../resources/templates/home.html")

@viewBp.route("/about/")
def about():
    return render_template("about.html")

@viewBp.route("/contact/")
def contact():
    return render_template("contact.html")

@viewBp.route("/hello/")
@viewBp.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@viewBp.route("/api/data")
def get_data():
    return webapp.send_static_file("data.json")