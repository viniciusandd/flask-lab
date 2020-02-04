from flask import jsonify, abort, request
from flask_restful import Resource
from restapi.extensions.database import db
from restapi.models.character import Character
from restapi.schemas.character import CharacterSchema

class CharacterResource(Resource):
    def get(self):
        characters = Character.query.all()
        return CharacterSchema(many=True).jsonify(characters)
    
    def post(self):
        cs = CharacterSchema()
        character = cs.load(request.json)        
        db.session.add(character)
        db.session.commit()
        return cs.jsonify(character)

class SingleCharacterResource(Resource):
    def get(self, character_id):
        cs = CharacterSchema()
        character = Character.query.filter_by(id=character_id).first()
        return cs.jsonify(character)

    def delete(self, character_id):
        Character.query.filter_by(id=character_id).delete()
        db.session.commit()
        return jsonify({"msg":"Registro deletado."})

    def put(self, character_id):
        cs = CharacterSchema()
        query = Character.query.filter_by(id=character_id)
        query.update(request.json)
        db.session.commit()
        return cs.jsonify(query.first())