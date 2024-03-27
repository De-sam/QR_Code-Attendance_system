from ..utils import db
from datetime import datetime
from .users import User
from .company import Company

# Define association table for the many-to-many relationship between User and Location
user_location_association = db.Table('user_location_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.UserID'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.LocationID'), primary_key=True)
)

class Location(db.Model):

    __tablename__ = 'location'
    LocationID = db.Column(db.Integer(), primary_key=True)
    CompanyID = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    users = db.relationship('User', secondary=user_location_association, backref='locations')
    Company = db.relationship('company', backref='location')
    LocationName= db.Column(db.String(45), nullable=False, )
    Country= db.Column(db.String(50), nullable=False, unique=True)
    Address= db.Column(db.String(50), nullable=False, unique=True)
    State= db.Column(db.float(), nullable=False)
    City= db.Column(db.float(), default=False)
    Long= db.Column(db.float(), nullable=False)
    Lat= db.Column(db.float(), default=False)
    Alias= db.Column(db.string(), default=True)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
     return f"< CompanyID='{self.CompanyID}',LocationID='{self.LocationID}',LocationNme='{self.LocationName}',companyalias='{self.Alias}', address='{self.Address}', name='{self.Name}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()