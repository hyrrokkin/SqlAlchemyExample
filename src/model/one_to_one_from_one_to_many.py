# -----------------------------------------------------------
# Связь один к одному через один ко многим
# -----------------------------------------------------------
from src import db


# класс Parent
class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    profile = db.relationship('Profile', back_populates='account', uselist=False)


# класс Child
class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    account = db.relationship('Account', back_populates='profile')
