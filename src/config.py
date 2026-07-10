import os


class Config:
    SECRET_KEY = 'secret-key'
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_PATH = os.path.join(BASE_PATH, 'static', 'uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_PATH, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = "305184097104-3469fsip3jcusvduiueokmp2jkul3qje.apps.googleusercontent.com"