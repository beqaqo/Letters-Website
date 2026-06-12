from flask_restx import Resource, reqparse

from src.ext import api
from src.models.photo import Photo

parser = reqparse.RequestParser()

parser.add_argument(
    'count',
    type=int,
    required=True,
    location='args'
)


@api.expect(parser)
class PhotoResource(Resource):

    def get(self):
        args = parser.parse_args()

        photos = Photo.query.limit(
            args['count']
        ).all()

        return [
            {
                'id': photo.id,
                'img': photo.img
            }
            for photo in photos
        ]