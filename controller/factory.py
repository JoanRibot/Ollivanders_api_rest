from flask import Flask
from flask_restful import Resource, Api
from controller.wellcome import Wellcome


def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Wellcome, '/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)