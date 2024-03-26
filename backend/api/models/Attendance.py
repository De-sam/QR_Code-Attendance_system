from ..utils import db
from datetime import datetime
from users import User 


class AttendanceReport(db.Model):
    __tablename__ = 'attendancereport'
    ReportID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'))
    Date = db.Column(db.Date)
    ClockInTime = db.Column(db.Time)
    ClockOutTime = db.Column(db.Time)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    UserID = db.column(db.Integer, db.ForeignKey('user.UserID')

    def __repr__(self):
        return f"<AttendanceReport Date='{self.Date}', Username='{self.user.username}', TimeIn='{self.ClockInTime}', TimeOut='{self.ClockOutTime}'>"

    def save(self):
        db.session.add(self)
        db.session.commit()