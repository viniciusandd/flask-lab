from flask import Blueprint
from flask_restful import Api
from .resources import Product, Order

bp = Blueprint("v1", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(Product, "/product/")
api.add_resource(Order, "/order/")

def init_app(app):
    app.register_blueprint(bp)