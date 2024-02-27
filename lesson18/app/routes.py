from flask import render_template

from app import app


@app.route("/")
def home():
    return render_template("home/home.html")


@app.route("/menu")
def menu():
    return render_template("home/menu.html")


@app.get("/404")
def get_404():
    return "<h1>Page not found</h1>", 404
