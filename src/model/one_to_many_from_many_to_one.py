# -----------------------------------------------------------
# Связь один к одному через много к одному
# -----------------------------------------------------------
from src import db


# класс Parent
class Passport(db.Model):
    __tablename__ = 'passports'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    person = db.relationship('Person', back_populates='passport')


# класс Child
class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    passport = db.relationship('Passport', back_populates='person', uselist=False)
