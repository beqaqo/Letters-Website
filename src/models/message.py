from sqlalchemy import DateTime

from src.ext import db
from src.models.base import BaseModel

class Message(BaseModel):
    __tablename__ = 'message'

    name = db.Column(db.String(), nullable=False)
    send_data = db.Column(DateTime, nullable=False)
    surname = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='messages')