from flask import Flask

from application.ext import configuration 
from application.ext import database

from application.blueprints import orders_v1
from application.blueprints import products_v1

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)

products_v1.init_app(app)
orders_v1.init_app(app)