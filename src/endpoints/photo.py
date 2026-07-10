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
parser.add_argument(
    'page',
    type=int,
    required=True,
    location='args'
)

parser.add_argument(
    'year',
    type=int,
    required=False,
    location='args'
)


@api.expect(parser)
class PhotoResource(Resource):

    def get(self):
        args = parser.parse_args()
        page = args['page']
        perpage_count = args['count']
        year = args['year']

        query = Photo.query
        if year:
            query = query.filter_by(year=year)

        photos = query.paginate(page=page, per_page=perpage_count, error_out=False)

        return [
            {
                'id': photo.id,
                'img': photo.img,
                'year': photo.year,
            }
            for photo in photos.items
        ]