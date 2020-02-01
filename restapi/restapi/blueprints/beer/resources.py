from flask import jsonify
from flask_restful import Resource

class Beer(Resource):
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

class SingleBeer(Resource):
    def get(self, beer_id):
        return jsonify([
            {
                "id": 1,
                "name": "Buzz",
                "description": "A light, crisp and bitter IPA brewed with English and American hops."                
            }
        ])