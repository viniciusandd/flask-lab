from flask import Flask

from restapi.extensions import configuration
from restapi.extensions import database
from restapi.extensions import commands

from restapi.blueprints import character
from restapi.blueprints import episode

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)
commands.init_app(app)

character.init_app(app)
episode.init_app(app)