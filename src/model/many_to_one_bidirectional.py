# -----------------------------------------------------------
# Связь многие к одному двунаправленная связь
# -----------------------------------------------------------
from src import db


# класс Parent
class Detail(db.Model):
    __tablename__ = 'details'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))
    machine = db.relationship('Machine', back_populates='details')


# класс Child
class Machine(db.Model):
    __tablename__ = 'machines'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    details = db.relationship('Detail', back_populates='machine')