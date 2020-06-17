# -----------------------------------------------------------
# Связь многие ко многим через association table
# -----------------------------------------------------------
from src import db


ticket_table = db.Table(
    'ticket',
    db.Model.metadata,
    db.Column('people_id', db.Integer, db.ForeignKey('peoples.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True)
)


# Parent
class People(db.Model):
    __tablename__ = 'peoples'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    films = db.relationship('Film', secondary=ticket_table, backref='peoples')


# Child
class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )
