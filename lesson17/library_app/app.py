from flask import Flask
from flask import (
    request,
    render_template,
    redirect,
    url_for
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lesson17.library_app.db import DBRepository

app = Flask(__name__)

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()
repo = DBRepository(session=session)


@app.get("/")
def home():
    return render_template('home.html')


@app.get("/menu")
def menu():
    return render_template('menu.html')


@app.get("/books")
def show_all_books():
    books = repo.show_all_books()
    if books:
        return render_template('books.html', books=books)
    return redirect(url_for("get_404"))


@app.route("/books/new", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        return render_template(
            "add_book.html"
        )
    elif request.method == "POST":
        name = request.form["name"]
        author_id = request.form["author_id"]
        repo.add_book(name, author_id)
        return redirect(
            url_for("show_all_books")
        )
    return redirect(url_for("get_404"))


@app.route("/books/update_book", methods=["GET", "POST"])
def update_book():
    if request.method == "GET":
        return render_template(
            "update_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book_name = request.form["book_name"]
        repo.update_book(book, book_name)
        return redirect(
            url_for("show_all_books")
        )
    return redirect(url_for("get_404"))


@app.route("/books/delete_book", methods=["GET", "POST"])
def delete_book():
    if request.method == "GET":
        return render_template(
            "delete_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        repo.delete_book(book)
        return redirect(
            url_for("show_all_books")
        )
    return redirect(url_for("get_404"))


@app.get("/show_authors")
def show_authors():
    authors = repo.show_authors()
    if authors:
        return render_template('authors.html', authors=authors)
    return redirect(url_for("get_404"))


@app.route("/authors/new", methods=["GET", "POST"])
def add_author():
    if request.method == "GET":
        return render_template(
            "add_author.html"
        )
    elif request.method == "POST":
        author_name = request.form["author_name"]
        repo.add_author(author_name)
        return redirect(
            url_for("show_authors")
        )
    return redirect(url_for("get_404"))


@app.route("/books/find_book", methods=["GET", "POST"])
def find_book():
    if request.method == "GET":
        return render_template(
            "find_book.html"
        )
    elif request.method == "POST":
        book_name = request.form["book_name"]
        books = repo.find_book(book_name)
        return render_template(
            "solo_book.html",
            books=books
        )
    return redirect(url_for("get_404"))


@app.get("/404")
def get_404():
    return "<h1>Page not found</h1>", 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
