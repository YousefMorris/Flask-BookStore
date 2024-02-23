from flask import render_template, request, redirect, url_for
from myapp.models import Book, db
# you write view functions
from myapp.books import book_blueprint


@book_blueprint.route("", endpoint="index")
def home():
    books = Book.get_all_objects()
    # render data to the template
    return render_template("books/index.html", books=books)


@book_blueprint.route("/show/<int:id>", endpoint="show")
def show_book(id):
    book = Book.get_book_by_id(id)
    if book:
        return render_template("books/show.html", books=book)


@book_blueprint.route("/add", methods=["GET", "POST"], endpoint="create")
def add_book():
    if request.method == "POST":
        book = Book.save_book(request.form,request.files)
        return redirect("/")
        # return redirect(book.show_url)
    return render_template("books/create.html")


@book_blueprint.route("/update/<int:id>", endpoint="edit", methods=["GET", "POST"])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        Book.update_book(book,request.form,request.files)
        return redirect("/")
    else:
        if book:
            return render_template("books/edit.html", book=book)
    return render_template("error/error404.html")


@book_blueprint.route("/delete/<int:id>", endpoint="delete", methods=["GET"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book:
        Book.delete_book_by_id(id)
        return redirect("/")
    error = "Book Not Found"
    return render_template("error/error404.html", error=error)


@book_blueprint.errorhandler(404)
def get_404(error):
    return render_template("error/error404.html", error=error)
