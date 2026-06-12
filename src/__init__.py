from flask import Flask

from src.ext import (
    admin,
    login_manager,
    api
)

from flask_restx import Resource


def create_app():
    app = Flask(__name__)

    app.config.from_object('src.config.Config')

    admin.init_app(app)
    #login_manager.init_app(app)
    api.init_app(app)

    @app.route('/')
    def home():
        return "Letters Website"


    @api.route('/test')
    class Test(Resource):
        def get(self):
            return {'status': 'ok'}


    return app