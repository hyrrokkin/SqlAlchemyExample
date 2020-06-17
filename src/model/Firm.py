from random import randint

from src import db


class Firm(db.Model):
    __tablename__ = 'firms'

    id = db.Column(
        db.Integer,
        name="id",
        primary_key=True
    )

    name = db.Column(db.String)
    budget = db.Column(db.Integer)
    firm_type = db.Column(db.String)

    def __repr__(self):
        return '%s budget = %d type = %s' % (self.name, self.budget, self.firm_type)

    @staticmethod
    def insert_firms():
        for i in range(0, 50):
            firm = Firm(name=('firm_%d' % (i + 1)), budget=randint(1000, 1000000))

            if i % 6 == 1 or i % 6 == 3 or i % 6 == 5:
                firm.firm_type = 'ООО'
            elif i % 6 == 2 or i % 6 == 4:
                firm.firm_type = 'ОАО'
            else:
                firm.firm_type = 'ЗАО'

            db.session.add(firm)
        db.session.commit()