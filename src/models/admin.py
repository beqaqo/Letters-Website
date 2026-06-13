from src.ext import db
from src.models.base import BaseModel
from flask_login import UserMixin

class Admin(UserMixin, BaseModel):
    __tablename__ = 'admin'

    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)