from datetime import datetime

from flask_restx import Resource, reqparse
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

from src.ext import api
from src.models.user import User
from src.models.message import Message
from src.config import Config

parser = reqparse.RequestParser()

parser.add_argument('id_token', required=True)
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('title', required=True)
parser.add_argument('text', required=True)
parser.add_argument('send_date', required=True, help='date format: YYYY-MM-DD eg. 2026-07-10')
class MessageResource(Resource):
    @api.expect(parser)
    def post(self):

        args = parser.parse_args()

        try:
            idinfo = id_token.verify_oauth2_token(
                args['id_token'],
                google_requests.Request(),
                Config.GOOGLE_CLIENT_ID
            )
        except ValueError:
            return {'error': 'Invalid Google token'}, 401

        if not idinfo.get('email_verified'):
            return {'error': 'Email not verified by Google'}, 400

        email = idinfo['email']

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            user = User(
                email=email
            )
            user.create()

        message = Message(
            name=args['name'],
            surname=args['surname'],
            title=args['title'],
            text=args['text'],
            send_data=datetime.fromisoformat(
                args['send_date']
            ),
            user_id=user.id
        )

        message.create()

        return {
            'status': 'created'
        }, 201