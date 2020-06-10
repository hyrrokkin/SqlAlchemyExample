# -----------------------------------------------------------
# Связь один ко многим однонаправленная связь
# -----------------------------------------------------------
from src import db


# класс Parent
class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    pupils = db.relationship('Pupil')


# класс Child
class Pupil(db.Model):
    __tablename__ = 'pupils'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    school_id = db.Column(
        db.Integer,
        db.ForeignKey('schools.id')
    )
