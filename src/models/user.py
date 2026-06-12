from src.ext import db
from src.models.base import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    email = db.Column(db.String(), unique=True, nullable=False)
    messages = db.relationship('Message', back_populates='user')
