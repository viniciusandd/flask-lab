from flask import Blueprint
from flask_restful import Api
from .resources import OrderResource, OrderItemResource

bp = Blueprint("order", __name__, url_prefix="/api/v1")

api = Api(bp)
api.add_resource(OrderResource, "/order/")
api.add_resource(OrderItemResource, "/order/<order_id>")

def init_app(app):
    app.register_blueprint(bp)