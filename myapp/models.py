import os
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime
from werkzeug.utils import secure_filename

db = SQLAlchemy()
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    no_of_pages = db.Column(db.Integer)
    price = db.Column(db.Integer)
    image = db.Column(db.String, default="book.png")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __str__(self):
        return f"{self.id}/{self.title}"

    @property
    def image_url(self):
        return url_for("static", filename=f"bookImages/{self.image}")

    @property
    def show_url(self):
        return url_for("book.show", id=self.id)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def delete_book_by_id(cls, id):
        book = cls.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return "Done"

    @classmethod
    def save_book(cls, request_data,request_files):  # immutable dict
        book = cls(**request_data)
        book.no_of_pages = int(book.no_of_pages)
        book.price = int(book.price)
        image = request_files["image"]
        if image:
            image_name = secure_filename(image.filename)
            image.save(os.path.join("C:\\Users\\Youssef\\PycharmProjects\\BookStore\\myapp\\static\\bookImages\\", image_name))
            book.image = image_name
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def update_book(cls,book, request_data,request_files):  # immutable dict
        book_obj = cls(**request_data)
        book.title = book_obj.title
        book.no_of_pages = int(book_obj.no_of_pages)
        book.price = int(book_obj.price)
        image = request_files["image"]
        if image:
            image_name = secure_filename(image.filename)
            image.save(os.path.join("C:\\Users\\Youssef\\PycharmProjects\\BookStore\\myapp\\static\\bookImages\\", image_name))
            book.image = image_name
        db.session.commit()
        return book
