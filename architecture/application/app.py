from flask import Flask

from application.ext import configuration 
from application.ext import database

from application.blueprints import webui
from application.blueprints import restapi_v1

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)

restapi_v1.init_app(app)

@app.route("/")
def index():
    return 'Hello, Word!'