from src.ext import db
from src.models.base import BaseModel

class Photo(BaseModel):
    __tablename__ = 'photo'

    img = db.Column(db.String(64), nullable=False)