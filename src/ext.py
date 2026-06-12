from flask_admin import Admin
from flask_login import LoginManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()

db = SQLAlchemy()

api = Api(
    title='Letters API',
    version='1.0',
    doc='/docs',
    prefix='/api'''
)

admin = Admin()