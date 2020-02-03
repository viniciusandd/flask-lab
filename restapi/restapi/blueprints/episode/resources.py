from flask import jsonify, abort
from flask_restful import Resource
from restapi.models.episode import Episode

class EpisodeResource(Resource):
    def get(self):
        episodes = Episode.query.all() or abort(204)
        return jsonify(
            {"episodes": [episode.to_dict() for episode in episodes]}
        )

class SingleEpisodeResource(Resource):
    def get(self, episode_id):
        episode = Episode.query.filter_by(id=episode_id).first() or abort(404)
        return jsonify(episode.to_dict())