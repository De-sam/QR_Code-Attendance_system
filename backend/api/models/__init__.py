from ..utils import db
from datetime import datetime
from sqlalchemy import Enum


class Admins(db.Model):
    __tablename__ = 'admins'
    AdminID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    PasswordHash = db.Column(db.string(120), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Admin= '{self.Username}', email= '{self.Email}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

class AttendanceReport(db.Model):
    __tablename__ = 'attendancereport'
    ReportID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    Date = db.Column(db.Date)
    ClockInTime = db.Column(db.Time)
    ClockOutTime = db.Column(db.Time)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        return f"<AttendanceReport Date='{self.Date}', Username='{self.user.username}', TimeIn='{self.ClockInTime}', TimeOut='{self.ClockOutTime}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class ClockingEvent(db.Model):
    __tablename__ = 'clocking_event'
    EventID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'))
    QRCodeID = db.Column(db.Integer, db.ForeignKey('qrcode.QRCodeID'))
    Timestamp = db.Column(db.DateTime)
    EventType = db.Column(Enum('Clock_In', 'Clock_Out'))
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    User = db.relationship('Users', backref='clocking_events', lazy=True)
    QRCode = db.relationship('QRCode', backref='clocking_events', lazy=True)

    def __repr__(self):
        return f"<ClockingEvent(EventID='{self.EventID}', UserID='{self.UserID}', QRCodeID='{self.QRCodeID}', Timestamp='{self.Timestamp}, EventType='{self.EventType}')>"


    def save(self):
        db.session.add(self)
        db.session.commit()


class Company(db.Model):

    __tablename__ = 'Company'
    CompanyID = db.Column(db.int())
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


class QRCode(db.Model):
    __tablename__ = 'qrcode'
    QRCodeID = db.Column(db.Integer, primary_key=True)
    QRCodeData = db.Column(db.String(255))
    ExpiryDate = db.Column(db.Date)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<QRCode(QRCodeID={self.QRCodeID}, QRCodeData='{self.QRCodeData}', ExpiryDate='{self.ExpiryDate}')>"


    def save(self):
        db.session.add(self)
        db.session.commit()


class Roles(db.Model):
    __tablename__ = 'roles'
    RoleID = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(255), unique=True)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



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