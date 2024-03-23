from ..utils import db
from datetime import datetime
from sqlalchemy import Enum
from users import User

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