from flask import Blueprint
from flask_restful import Api
from .resources import Beer, SingleBeer

bp = Blueprint("beer", __name__, url_prefix="/v1")

api = Api(bp)
api.add_resource(Beer, "/beer/")
api.add_resource(SingleBeer, "/beer/<beer_id>")

def init_app(app):
    app.register_blueprint(bp)