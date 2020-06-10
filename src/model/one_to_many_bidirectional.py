# -----------------------------------------------------------
# Связь один ко многим двунаправленная связь
# -----------------------------------------------------------
from src import db


# класс Parent
class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    photos = db.relationship(
        'Photo',
        back_populates='album'
    )


# класс Child
class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    album_id = db.Column(
        db.Integer,
        db.ForeignKey('albums.id'),
        name="album_id",
        nullable=False
    )

    album = db.relationship(
        'Album',
        back_populates='photos',
    )
