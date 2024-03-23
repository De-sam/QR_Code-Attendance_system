from ..utils import db
from datetime import datetime


class Roles(db.Model):
    __tablename__ = 'roles'
    RoleID = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(255), unique=True)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

