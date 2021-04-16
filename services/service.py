from flask_restful import fields, marshal_with, abort

from repository.db import *


class Service:

    resource_fields = {
        "Name": fields.String,
        "Sell_in": fields.Integer,
        "Quality": fields.Integer,
    }

    @staticmethod
    @marshal_with(resource_fields)
    def get_objeto(name):

        if not name:
            abort(404, message="Es necesario el nombre del item")

        item = get_objeto(name)

        if not item:
            abort(404, message="El item {} no existe".format(name))

        return item

    @staticmethod
    @marshal_with(resource_fields)
    def get_sell_in(sell_in):
        if not sell_in:
            abort(404, message="Es necesario el nombre del item")

        item = get_sell_in(sell_in)

        if not item:
            abort(404, message="El item con sell_in {} no existe".format(sell_in))

        return item

    @staticmethod
    @marshal_with(resource_fields)
    def get_quality(quality):
        if not quality:
            abort(404, message="Es necesario el nombre del item")

        item = get_quality(quality)

        if not item:
            abort(404, message="El item con quality {} no existe".format(quality))

        return item


    @staticmethod
    @marshal_with(resource_fields)
    def post_objeto(item):

        item = post_objeto(item)
