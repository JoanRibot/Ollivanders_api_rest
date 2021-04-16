from flask import Flask
from flask_restful import Resource, Api
from domain.types import *
import os
from flask_sqlalchemy import SQLAlchemy
from flask import g
import click
from flask.cli import with_appcontext
from flask import current_app as app

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:120320@localhost/ollivanders"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.init_app(app)
        g.db = db
        g.Items = Inventory

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.session.close()

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40), nullable=False)
    Sell_in = db.Column(db.Integer, nullable=False)
    Quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Item ({self.Name, self.Sell_in, self.Quality})'
    
def init_db():
    db = get_db()

   # with app.open_resource('schema.mysql') as f:
    #    db.executescript(f.read().decode('utf8'))

    items = [AgedBrie("Aged Brie", 2, 0),
            NormalItem("Elixir of the Mongoose", 5, 7),
            NormalItem("+5 Dexterity Vest", 10, 20),
            Sulfuras("Hand of Ragnaros", 0, 80),
            Sulfuras("Hand of Ragnaros", -1, 80),
            BackstagePasses("TAFKAL80ETC concert", 15, 20),
            BackstagePasses("TAFKAL80ETC concert", 10, 49),
            BackstagePasses("TAFKAL80ETC concert", 5, 49),
            NormalItem("Conjured Mana Cake", 3, 6)]

    resultado = []

    for item in items:
        objeto = Inventory(Name = item.name, Sell_in = item.sell_in, Quality = item.quality)
        resultado.append(objeto)
        
    db.drop_all()
    db.create_all()
    db.session.add_all(resultado)
    db.session.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

################################################################################################

def get_objeto(name):
    query = db.session.query(Inventory).filter_by(Name = name).all()
    return query

def get_sell_in(sell_in):
    query = db.session.query(Inventory).filter_by(Sell_in = sell_in).all()
    return query

def get_quality(quality):
    query = db.session.query(Inventory).filter_by(Quality = quality).all()
    return query

def post_objeto(item):
    objeto = Inventory(Name = item.name, Sell_in = item.sell_in, Quality = item.quality)

    db.session.add(objeto)
    db.session.commit()