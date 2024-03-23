from ..utils import db
from datetime import datetime


class Location(db.Model):

    __tablename__ = 'location'
    LocationIdID = db.Column(db.Integer(), primary_key=True)
    Name= db.Column(db.String(45), nullable=False, unique=True)
    Address= db.Column(db.String(50), nullable=False, unique=True)
    Long= db.Column(db.Text(), nullable=False)
    Lat= db.Column(db.Boolean(), default=False)
    Alias= db.Column(db.Boolean(), default=True)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
     return f"<User username='{self.Username}', email='{self.Email}', active='{self.IsActive}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()