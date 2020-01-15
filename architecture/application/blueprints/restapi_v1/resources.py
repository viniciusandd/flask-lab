from flask import jsonify
from flask_restful import Resource

class ProductResource(Resource):
    def get(self):
        return jsonify({
            "products": [
                {
                    "id": 1,
                    "name": "mouse",
                    "price": "100.00"
                },
                {
                    "id": 2,
                    "name": "keyboard",
                    "price": "200.00"
                }
            ]
        })

class ProductItemResource(Resource):
    def get(self, product_id):
        return jsonify({
            "id": 1,
            "name": "keyboard",
            "price": "200.00"
        })