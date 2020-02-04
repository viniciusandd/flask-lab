from flask import jsonify, abort
from flask_restful import Resource
import requests
from restapi.models.character import Character
from restapi.models.episode import Episode

class Fetch(Resource):
    def get(self):
        r = requests.get('https://rickandmortyapi.com/api/character/1')
        response = r.json()


class Send(Resource):
    def post(self):
        pass