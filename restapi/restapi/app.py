from flask import Flask

from restapi.blueprints import beer

app = Flask(__name__)

beer.init_app(app)