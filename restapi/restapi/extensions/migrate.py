from flask_migrate import Migrate
from restapi.extensions.database import db

migrate = Migrate()

from restapi.models.character import Character
from restapi.models.episode import Episode

def init_app(app):
    migrate.init_app(app, db)