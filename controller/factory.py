from flask import Flask
from flask_restful import Resource, Api
from wellcome import Wellcome
from objeto import Objeto


def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Wellcome, "/")
    api.add_resource(Objeto, "/objeto/<name>")

    return app
