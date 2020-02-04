from flask import Blueprint
from flask_restful import Api
from .resources import SynchronizeResource

bp = Blueprint("synchronize", __name__, url_prefix="/v1")

api = Api(bp)
api.add_resource(SynchronizeResource, "/synchronize/")

def init_app(app):
    app.register_blueprint(bp)