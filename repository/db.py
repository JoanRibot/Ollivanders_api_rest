from flask import Flask
from flask_restful import Resource, Api
from domain.types import *
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:120320@localhost/ollivanders"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40), nullable=False)
    Sell_in = db.Column(db.Integer, nullable=False)
    Quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Item ({self.Name, self.Sell_in, self.Quality})'

db.drop_all()
db.create_all()

items = [AgedBrie("Aged Brie", 2, 0),
            NormalItem("Elixir of the Mongoose", 5, 7),
            NormalItem("+5 Dexterity Vest", 10, 20),
            Sulfuras("Hand of Ragnaros", 0, 80),
            Sulfuras("Hand of Ragnaros", -1, 80),
            BackstagePasses("TAFKAL80ETC concert", 15, 20),
            BackstagePasses("TAFKAL80ETC concert", 10, 49),
            BackstagePasses("TAFKAL80ETC concert", 5, 49),
            NormalItem("Conjured Mana Cake", 3, 6)]

def conversion(items):
    resultado = []

    for item in items:
        objeto = Inventory(Name = item.name, Sell_in = item.sell_in, Quality = item.quality)
        resultado.append(objeto)
        
    return resultado

db.session.add_all(conversion(items))
db.session.commit()