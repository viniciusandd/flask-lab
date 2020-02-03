from flask import Blueprint
from flask_restful import Api

from .resources import EpisodeResource, SingleEpisodeResource

bp = Blueprint("episode", __name__, url_prefix='/v1')

api = Api(bp)
api.add_resource(EpisodeResource, '/episode/')
api.add_resource(SingleEpisodeResource, '/episode/<episode_id>')

def init_app(app):
    app.register_blueprint(bp)