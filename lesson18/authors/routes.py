from flask import (
    redirect,
    render_template,
    request,
    url_for,
)

from app import db
from authors import authors_blueprint
from authors.models import Author


@authors_blueprint.route("", methods=["GET", "POST"])
def show_authors():
    authors = db.session.execute(db.select(Author)).scalars().fetchall()
    if authors:
        return render_template("authors.html", authors=authors)
    return redirect(url_for("get_404"))


@authors_blueprint.route("/new", methods=["GET", "POST"])
def add_author():
    if request.method == "GET":
        return render_template("add_author.html")
    elif request.method == "POST":
        author_name = request.form["author_name"]
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for("authors.show_authors"))
    return redirect(url_for("get_404"))


@authors_blueprint.get("/404")
def get_404():
    return "<h1>Page not found</h1>", 404
