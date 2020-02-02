from flask import Flask

from restapi.extensions import database
from restapi.extensions import migrate
from restapi.extensions import configuration
from restapi.blueprints import character

app = Flask(__name__)

database.init_app(app)
migrate.init_app(app)
configuration.init_app(app)
character.init_app(app)