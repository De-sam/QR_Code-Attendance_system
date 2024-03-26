from ..utils import db
from datetime import datetime
from location import Location


class Company(db.Model):

    __tablename__ = 'Comapny'
    CompanyID = db.column(db.int()) 
    CompanyName = db.Column(db.string, nuallable =False , unique=True ) 
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    Location = db.relationship('location', backref='company', lazy=True)
    Users = db.relationship('user', backref='company', lazy=True)

    def __repr__(self):
     return f"<company alias='{self.Alias}', address='{self.Address}', name='{self.Name}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()