from flask_restx import Resource

class StatisticsResource(Resource):
    def get(self):
        return {'received': 0,
                'pending': 0,
                'sent': 0}