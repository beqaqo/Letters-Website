from datetime import datetime

from flask_restx import Resource, reqparse

from src.models.user import User
from src.models.message import Message

parser = reqparse.RequestParser()

parser.add_argument('email', required=True)
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('title', required=True)
parser.add_argument('text', required=True)
parser.add_argument('send_date', required=True)
class MessageResource(Resource):

    def post(self):

        args = parser.parse_args()

        user = User.query.filter_by(
            email=args['email']
        ).first()

        if not user:
            user = User(
                email=args['email']
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