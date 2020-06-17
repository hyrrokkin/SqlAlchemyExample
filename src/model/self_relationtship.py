from src import db


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    company_name = db.Column(db.String(50))

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey('companies.id')
    )

    parent = db.relationship(
        'Company',
        remote_side='Company.id',
        backref=db.backref('children')
    )


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    label = db.Column(db.String)

    child_id = db.Column(
        db.Integer,
        db.ForeignKey('tags.id'),
        name='child_tag_id'
    )

    children = db.relationship(
        'Tag',
        remote_side=[id],
        uselist=True,
        backref='parent'
    )
