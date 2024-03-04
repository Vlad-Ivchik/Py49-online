from flask import (
    redirect,
    render_template,
    request,
    url_for,
)

from app import db
from books import books_blueprint
from books.models import Book


@books_blueprint.route("", methods=["GET", "POST"])
def show_all_books():
    books = db.session.execute(db.select(Book)).scalars().fetchall()
    if books:
        return render_template(
            "books.html",
            books=books)
    return redirect(url_for("get_404"))


@books_blueprint.route("/new", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        return render_template(
            "add_book.html"
        )
    elif request.method == "POST":
        name = request.form["name"]
        author_id = request.form["author_id"]
        book = Book(name=name, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books.show_all_books"))
    return redirect(url_for("get_404"))


@books_blueprint.route("/update_book", methods=["GET", "POST"])
def update_book():
    if request.method == "GET":
        return render_template(
            "update_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book_name = request.form["book_name"]
        books = db.session.query(Book).filter(Book.name.ilike(book)).all()
        if books:
            for book in books:
                book.name = book_name
        db.session.commit()
        return redirect(url_for("books.show_all_books"))
    return redirect(url_for("get_404"))


@books_blueprint.route("/delete_book", methods=["GET", "POST"])
def delete_book():
    if request.method == "GET":
        return render_template(
            "delete_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        deleted_book = db.session.query(Book).filter(Book.name == book).first()
        db.session.delete(deleted_book)
        db.session.commit()
        return redirect(url_for("books.show_all_books"))
    return redirect(url_for("get_404"))


@books_blueprint.route("/find_book", methods=["GET", "POST"])
def find_book():
    if request.method == "GET":
        return render_template(
            "find_book.html"
        )
    elif request.method == "POST":
        book_name = request.form["book_name"]
        book = db.session.query(Book).filter(Book.name.ilike(f"%{book_name}%")).all()
        return render_template(
            "solo_book.html",
            books=book
        )
    return redirect(url_for("get_404"))


@books_blueprint.get("/404")
def get_404():
    return "<h1>Page not found</h1>", 404
