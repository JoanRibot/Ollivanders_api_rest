from flask_restful import Resource
from services.service import Service

class Items(Resource):

    # /item/<name>
    def get(self, name):
        # curl http://localhost:5000/items/"Aged%20Brie"
        return Service.get_item(name), 200