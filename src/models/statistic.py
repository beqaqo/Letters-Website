from src.ext import db
from src.models.base import BaseModel

class Statistic(BaseModel):
    __tablename__ = 'statistic'

    total_messages = db.Column(db.Integer, default=0)
    waiting_messages = db.Column(db.Integer, default=0)
    sent_messages = db.Column(db.Integer, default=0)
