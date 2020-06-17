from sqlalchemy import func

from src import app, db
from src.model.Firm import Firm

if __name__ == '__main__':
    #Firm.insert_firms()
    # app.run()

    print(Firm.query.first())
    print(db.session.query(Firm).first())

    print(Firm.query.all())
    print(db.session.query(Firm).all())

    print(Firm.query.get(5))
    print(db.session.query(Firm).get(5))

    print(Firm.query.limit(5).all())
    print(db.session.query(Firm).limit(5).all())

    print(Firm.query.limit(5).offset(5).all())
    print(db.session.query(Firm).limit(5).offset(5).all())

    print(Firm.query.order_by(Firm.budget).all())
    print(db.session.query(Firm).order_by(Firm.budget).all())

    print(Firm.query.order_by(Firm.budget.desc()).all())
    print(db.session.query(Firm).order_by(Firm.budget.desc()).all())

    print(db.session.query(Firm.firm_type, func.count(Firm.firm_type)).group_by(Firm.firm_type).all())
