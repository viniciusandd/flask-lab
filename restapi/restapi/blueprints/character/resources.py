from flask import jsonify, abort
from flask_restful import Resource
from restapi.models.character import Character

class CharacterResource(Resource):
    def get(self):
        characters = Character.query.all() or abort(204)
        return jsonify(
            {"characters": [character.to_dict() for character in characters]}
        )

class SingleCharacterResource(Resource):
    def get(self, character_id):
        character = Character.query.filter_by(id=character_id).first() or abort(404)
        return jsonify(character.to_dict())