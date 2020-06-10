# -----------------------------------------------------------
# Связь многие к одному однонаправленная связь
# -----------------------------------------------------------
from src import db


# класс Parent
class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book = db.relationship('Book')


# класс Child
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )
