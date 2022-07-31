from db import db
from models.enums import UserRole


class BaseUserModel(db.Model):
    __abstract__ = True
    # не се използва, само съдържа общите характеристики на класовете наследници
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)  # unique само уникални имейли, без повторения
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # 255 за да има място за хеш


class ComplainerModel(BaseUserModel):
    __tablename__ = 'complainers'

    complaints = db.relationship("ComplaintModel", backref="complaint", lazy='dynamic')
    role = db.Column(db.Enum(UserRole), default=UserRole.complainer, nullable=False)


class ApproverModel(BaseUserModel):
    __tablename__ = 'approvers'
    role = db.Column(db.Enum(UserRole), default=UserRole.approver, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = 'adminss'
    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
