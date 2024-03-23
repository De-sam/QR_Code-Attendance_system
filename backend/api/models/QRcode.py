from ..utils import db
from datetime import datetime


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


        