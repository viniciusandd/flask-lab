from flask import jsonify, abort
from flask_restful import Resource
from restapi.models.character import Character
from restapi.models.episode import Episode

class Fetch(Resource):
    def get(self):
        return 'teste'


class Send(Resource):
    def post(self):
        pass