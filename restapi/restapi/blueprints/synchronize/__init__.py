from flask import Blueprint
from flask_restful import Api
from .resources import Fetch, Send

bp = Blueprint("synchronize", __name__, url_prefix="/v1")

api = Api(bp)
api.add_resource(Fetch, "/synchronize/fetch")
api.add_resource(Send, "/synchronize/send")

def init_app(app):
    app.register_blueprint(bp)