from flask import jsonify, abort, request
from flask_restful import Resource
import requests
from restapi.extensions.database import db
from restapi.models.character import Character
from restapi.schemas.character import CharacterSchema
from restapi.models.episode import Episode
from restapi.schemas.episode import EpisodeSchema

class SynchronizeResource(Resource):
    """
    - Foi necessário adicionar o atributo -> unknown = EXCLUDE
    com ele o marshmallow começou a gerar uma exception que
    foi corrigida passando uma sessão do banco de dados na função
    load -> cs.load(response['results'], session=db.session).

    - Todos os relatos acima foram consequência dos objetos retornados
    pela api não serem iguais as models do projeto. Na documentação do 
    marshmallow tem uma explicação de como funciona a exclusão de campos.
    """
    def get(self):
        cs = CharacterSchema(many=True)
        response_characters = requests.get('https://rickandmortyapi.com/api/character/').json()
        characters = cs.load(response_characters['results'], session=db.session)
        db.session.bulk_save_objects(characters)

        es = EpisodeSchema(many=True)
        response_episodes = requests.get('https://rickandmortyapi.com/api/episode/').json()
        episodes = es.load(response_episodes['results'], session=db.session)
        db.session.bulk_save_objects(episodes)

        db.session.commit()
        return jsonify({"msg":"Registros inseridos."})

    def post(self):
        """
        Esse método é responsável por verificar os registros novos
        e envia-los para a nuvem.
        """
        ...