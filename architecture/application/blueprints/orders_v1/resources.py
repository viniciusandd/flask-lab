from flask import jsonify
from flask_restful import Resource

class OrderResource(Resource):
    def get(self):
        return jsonify({
            "orders": [
                {
                    "id": 1,
                    "customer": "Vinicius",
                    "grand total": "100.00"
                },
                {
                    "id": 2,
                    "customer": "Zé",
                    "grand total": "200.00"
                }
            ]
        })

class OrderItemResource(Resource):
    def get(self, order_id):
        return jsonify({
            "id": 1,
            "customer": "Vinicius",
            "grand total": "100.00"
        })