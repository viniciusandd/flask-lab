from flask import Blueprint
from flask_restful import Api
from .resources import CharacterResource, SingleCharacterResource

bp = Blueprint("character", __name__, url_prefix="/v1")

api = Api(bp)
api.add_resource(CharacterResource, "/character/")
api.add_resource(SingleCharacterResource, "/character/<character_id>")

def init_app(app):
    app.register_blueprint(bp)