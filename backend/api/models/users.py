from ..utils import db
from datetime import datetime
from .company import Company
from .location import Location

user_location_association = db.Table('user_location_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.UserID'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.LocationID'), primary_key=True)
)

class User(db.Model):

    __tablename__ = 'user'
    UserID = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(45), nullable=False, unique=True)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    UserImage = db.Column(db.String(20), nullable=False , default="default.jpg")
    PasswordHash = db.Column(db.Text(), nullable=False)
    Company = db.Column(db.Integer, db.ForeignKey('company'))
    AttendanceReport= db.Column(db.Integer, db.ForeignKey('attendancereport', backref='user'))
    IsStaff = db.Column(db.Boolean(), default=False)
    IsActive = db.Column(db.Boolean(), default=True)
    IsAdmin = db.Column(db.Boolean, default=False)
    AdminID = db.Column(db.Integer, db.ForeignKey('admins.AdminID'))
    RoleID = db.Column(db.Integer, db.ForeignKey('roles.RoleID'))
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
     return f"<User username='{self.Username}', email='{self.Email}', active='{self.IsActive}', UserImage='{self.UserImage}'>"


    def save(self):
        db.session.add(self)
        db.session.commit()