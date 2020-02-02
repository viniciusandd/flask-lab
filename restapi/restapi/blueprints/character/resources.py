from flask import jsonify
from flask_restful import Resource

class Character(Resource):
    def get(self):
        return jsonify([
            {
                "id": 1,
                "name": "Buzz",
                "description": "A light, crisp and bitter IPA brewed with English and American hops."                
            },
            {
                "id": 2,
                "name": "Trashy Blonde",
                "description": "A titillating, neurotic, peroxide punk of a Pale Ale."
            }
        ])

class SingleCharacter(Resource):
    def get(self, character_id):
        return jsonify([
            {
                "id": 1,
                "name": "Buzz",
                "description": "A light, crisp and bitter IPA brewed with English and American hops."                
            }
        ])