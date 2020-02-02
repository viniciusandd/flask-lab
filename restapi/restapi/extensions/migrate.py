from flask_migrate import Migrate
from restapi.extensions.database import db

def init_app(app):
    Migrate(app, db)