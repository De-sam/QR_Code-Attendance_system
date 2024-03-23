from ..utils import db
from datetime import datetime

class Admins(db.Model):
    __tablename__ = 'admins'
    AdminID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), unique=True, nullable= False )
    Email = db.Column(db.String(255), unique=True, nullable=False)
    PasswordHash = db.Column(db.string(120), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        return f"<Admin= '{self.Username}', email= '{self.Email}>"
       

    def save(self):
        db.session.add(self)
        db.session.commit()