from flask import jsonify, abort, request
from flask_restful import Resource
from restapi.extensions.database import db
from restapi.models.episode import Episode
from restapi.schemas.episode import EpisodeSchema

class EpisodeResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return EpisodeSchema(many=True).jsonify(episodes)

    def post(self):
        es = EpisodeSchema()
        episode = es.load(request.json)
        db.session.add(episode)
        db.session.commit()
        return es.jsonify(episode)

class SingleEpisodeResource(Resource):
    def get(self, episode_id):
        es = EpisodeSchema()
        episode = Episode.query.filter_by(id=episode_id).first()
        return es.jsonify(episode)

    def delete(self, episode_id):
        Episode.query.filter_by(id=episode_id).delete()
        db.session.commit()
        return jsonify({"msg":"Episodio deletado."})

    def put(self, episode_id):
        es = EpisodeSchema()
        query = Episode.query.filter_by(id=episode_id)
        query.update(request.json)
        db.session.commit()
        return es.jsonify(query.first())