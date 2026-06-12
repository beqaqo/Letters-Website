import os


class Config:
    SECRET_KEY = 'secret-key'
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_PATH = os.path.join(BASE_PATH, 'static', 'uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_PATH, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False