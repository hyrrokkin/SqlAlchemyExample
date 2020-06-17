# -----------------------------------------------------------
# Связь многие ко многим через класс
# -----------------------------------------------------------
from src import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)

    song = db.relationship('Song', back_populates='users')
    user = db.relationship('User', back_populates='songs')

    price = db.Column(db.Integer)


# Parent
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    songs = db.relationship('Purchase', back_populates='user')


# Child
class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    users = db.relationship('Purchase', back_populates='song')
