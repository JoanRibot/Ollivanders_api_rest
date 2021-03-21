from flask_restful import Resource
from ..services.service import Service


class Objeto(Resource):

    def get(self, name):
        # curl http://localhost:5000/objeto/"Aged%20Brie"
        return Service.get_objeto(name), 200