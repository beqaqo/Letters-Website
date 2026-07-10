from flask import Flask

from src.admin_views import register_admin_views
from src.config import Config
from src.ext import admin, api, db, login_manager, migrate
from src.models.admin import Admin

from src.endpoints.photo import PhotoResource
from src.endpoints.message import MessageResource
from src.endpoints.auth import GoogleVerify

from src.admin_views.base import SecureIndexView

from src.commands import (
    init_db,
    populate_db
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    migrate.init_app(app, db)

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

    app.cli.add_command(init_db)
    app.cli.add_command(populate_db)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    return app