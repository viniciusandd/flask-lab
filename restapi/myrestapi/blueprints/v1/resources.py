from flask import jsonify
from flask_restful import Resource

class Product(Resource):
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

class Order(Resource):
    def get(self):
        return jsonify({
            "orders": [
                {
                    "id": 1,
                    "customer": "vinicius",
                    "status": "closed"
                },
                {
                    "id": 2,
                    "customer": "vinicius",
                    "status": "open"
                }
            ]
        })    