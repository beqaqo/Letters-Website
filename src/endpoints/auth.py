from flask import request, jsonify
from flask_restx import Resource, Namespace, reqparse
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

from src.ext import api
from src.config import Config

parser = reqparse.RequestParser()
parser.add_argument(
    'id_token',
    required=True,
    location='json',
    help='Google ID token (JWT) received from the frontend Google Sign-In button'
)

@api.route("/google-verify")
@api.expect(parser)
class GoogleVerify(Resource):
    def post(self):
        args = parser.parse_args()
        token = args['id_token']

        if not token:
            return {"error": "id_token is required"}, 400

        try:
            idinfo = id_token.verify_oauth2_token(
                token, google_requests.Request(), Config.GOOGLE_CLIENT_ID
            )

            # idinfo contains: email, email_verified, name, picture, sub (Google user id), etc.
            if not idinfo.get("email_verified"):
                return {"error": "Email not verified by Google"}, 400

            return {
                "email": idinfo["email"],
                "name": idinfo.get("name"),
                "verified": True,
            }, 200

        except ValueError:
            # Invalid token
            return {"error": "Invalid token"}, 401