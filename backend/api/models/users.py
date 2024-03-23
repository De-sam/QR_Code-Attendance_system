from ..utils import db
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'
    UserID = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(45), nullable=False, unique=True)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    Password_hash = db.Column(db.Text(), nullable=False)
    IsStaff = db.Column(db.Boolean(), default=False)
    IsActive = db.Column(db.Boolean(), default=True)
    IsAdmin = db.Column(db.Boolean, default=False)
    AdminID = db.Column(db.Integer, db.ForeignKey('admins.AdminID'))
    RoleID = db.Column(db.Integer, db.ForeignKey('roles.RoleID'))
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
     return f"<User username='{self.Username}', email='{self.Email}', active='{self.IsActive}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()