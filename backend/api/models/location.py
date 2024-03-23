from ..utils import db
from datetime import datetime


class Location(db.Model):

    __tablename__ = 'location'
    LocationIdID = db.Column(db.Integer(), primary_key=True)
    Name= db.Column(db.String(45), nullable=False, unique=True)
    Address= db.Column(db.String(50), nullable=False, unique=True)
    Long= db.Column(db.float(), nullable=False)
    Lat= db.Column(db.float(), default=False)
    Alias= db.Column(db.string(), default=True)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
     return f"<company alias='{self.Alias}', address='{self.Address}', name='{self.Name}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()