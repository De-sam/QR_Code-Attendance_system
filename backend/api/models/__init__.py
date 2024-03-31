from ..utils import db
from datetime import datetime
from sqlalchemy import Enum


class Admins(db.Model):

    __tablename__ = 'admins'

    AdminID = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(120), nullable=False)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Admin= '{self.Username}', email= '{self.Email}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Roles(db.Model):

    __tablename__ = 'roles'

    RoleID = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(255), unique=True)
    Users = db.relationship('User', backref='Role', lazy=True)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(db.Model):

    __tablename__ = 'users'

    UserID = db.Column(db.Integer(), primary_key=True)
    Username = db.Column(db.String(50), nullable=False, unique=True)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    UserImage = db.Column(db.Text(), nullable=True, default="default.jpg")
    PasswordHash = db.Column(db.Text(), nullable=False)
    CompanyID = db.Column(db.Integer(), db.ForeignKey('companies.CompanyID'))
    RoleID = db.Column(db.Integer(), db.ForeignKey('roles.RoleID'))
    AttendanceReports = db.relationship('AttendanceReport', backref='User', lazy=True)
    ClockingEvents = db.relationship('ClockingEvent', backref='User', lazy=True)
    IsStaff = db.Column(db.Boolean(), default=False)
    IsActive = db.Column(db.Boolean(), default=True)
    IsAdmin = db.Column(db.Boolean(), default=False)
    AdminID = db.Column(db.Integer(), db.ForeignKey('admins.AdminID'))
    RoleID = db.Column(db.Integer(), db.ForeignKey('roles.RoleID'))
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f"<User username='{self.Username}', " \
               f"email='{self.Email}', active='{self.IsActive}', " \
               f"UserImage='{self.UserImage}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class QRCode(db.Model):

    __tablename__ = 'qrcodes'

    QRCodeID = db.Column(db.Integer(), primary_key=True)
    QRCodeData = db.Column(db.Text())
    ClockingEvents = db.relationship('ClockingEvent', backref='QRCode', lazy=True)
    ExpiryDate = db.Column(db.Date())
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<QRCode(QRCodeID={self.QRCodeID}, QRCodeData='{self.QRCodeData}', ExpiryDate='{self.ExpiryDate}')>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class AttendanceReport(db.Model):

    __tablename__ = 'attendance_reports'

    ReportID = db.Column(db.Integer(), primary_key=True)
    UserID = db.Column(db.Integer(), db.ForeignKey('users.UserID'))
    Date = db.Column(db.Date())
    ClockInTime = db.Column(db.Time())
    ClockOutTime = db.Column(db.Time())
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AttendanceReport Date='{self.Date}', " \
               f"User='{self.User}', " \
               f"TimeIn='{self.ClockInTime}', " \
               f"TimeOut='{self.ClockOutTime}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class ClockingEvent(db.Model):

    __tablename__ = 'clocking_events'

    EventID = db.Column(db.Integer(), primary_key=True)
    Timestamp = db.Column(db.DateTime())
    EventType = db.Column(Enum('Clock_In', 'Clock_Out'))
    UserID = db.Column(db.Integer(), db.ForeignKey('users.UserID'))
    QRCodeID = db.Column(db.Integer(), db.ForeignKey('qrcodes.QRCodeID'))
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<ClockingEvent(EventID='{self.EventID}', " \
               f"User='{self.User}', QRCodeID='{self.QRCode}', " \
               f"Timestamp='{self.Timestamp}, EventType='{self.EventType}')>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Company(db.Model):

    __tablename__ = 'companies'

    CompanyID = db.Column(db.Integer(), primary_key=True)
    CompanyName = db.Column(db.String(255), nullable=False, unique=True)
    Users = db.relationship('User', backref='Company', lazy=True)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    Locations = db.relationship('Location', backref='Company', lazy=True)

    def __repr__(self):
        return f"<company alias='{self.Alias}', address='{self.Address}', name='{self.Name}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()


# Define association table for the many-to-many relationship between User and Location
user_location_association = db.Table('user_location_association',
                                     db.Column('user_id', db.Integer(), db.ForeignKey('users.UserID'),
                                               primary_key=True),
                                     db.Column('location_id', db.Integer(), db.ForeignKey('locations.LocationID'),
                                               primary_key=True))


class Location(db.Model):

    __tablename__ = 'locations'

    LocationID = db.Column(db.Integer(), primary_key=True)
    CompanyID = db.Column(db.Integer(), db.ForeignKey('companies.CompanyID'))
    users = db.relationship('User', secondary=user_location_association, backref='Locations')
    LocationName = db.Column(db.String(45), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Address = db.Column(db.String(50), nullable=False)
    State = db.Column(db.Float(), nullable=False)
    City = db.Column(db.Float())
    Long = db.Column(db.Float(), nullable=False)
    Lat = db.Column(db.Float(), nullable=False)
    Alias = db.Column(db.String(), nullable=True)
    CreatedAt = db.Column(db.DateTime(), default=datetime.utcnow())
    UpdatedAt = db.Column(db.DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f"<CompanyID='{self.CompanyID}', " \
               f"LocationID='{self.LocationID}', " \
               f"LocationName='{self.LocationName}', " \
               f"companyAlias='{self.Alias}', " \
               f"address='{self.Address}', name='{self.Name}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()

