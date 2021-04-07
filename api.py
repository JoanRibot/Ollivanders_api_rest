from flask import Flask
from flask_restful import Resource, Api
from controller.wellcome import Wellcome
from controller.objeto import Objeto
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

api.add_resource(Wellcome, "/")
api.add_resource(Objeto, "/objeto/<name>") 


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:120320@localhost/ollivanders"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Inventory(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40), nullable=False)
    Sell_in = db.Column(db.Integer, nullable=False)
    Quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Item ({self.Name, self.Sell_in, self.Quality})'

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
