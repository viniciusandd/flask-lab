from flask import Flask

from myrestapi.ext import configuration
from myrestapi.blueprints import v1

app = Flask(__name__)

configuration.init_app(app)
v1.init_app(app)