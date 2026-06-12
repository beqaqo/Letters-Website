from flask import Flask
from flask_restx import Resource

from src.admin_views import register_admin_views
from src.config import Config
from src.ext import admin, api, db, login_manager
from src.models.admin import Admin

from src.endpoints.photo import PhotoResource
from src.endpoints.message import MessageResource

from src.admin_views.base import SecureIndexView


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    admin.init_app(
        app,
        index_view=SecureIndexView()
    )
    register_admin_views(admin, db.session)
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    api.init_app(app)

    api.add_resource(
        PhotoResource,
        '/photo',
    )
    api.add_resource(
        MessageResource,
        '/message',
    )

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    @app.route('/')
    def home():
        return "Letters Website"


    @api.route('/test')
    class Test(Resource):
        def get(self):
            return {'status': 'ok'}

    return app