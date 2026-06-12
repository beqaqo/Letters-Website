from flask_admin import Admin
from flask_login import LoginManager
from flask_restx import Api

admin = Admin()
login_manager = LoginManager()
api = Api(
    title='Letters API',
    version='1.0',
    doc='/docs',
    prefix='/api'
)