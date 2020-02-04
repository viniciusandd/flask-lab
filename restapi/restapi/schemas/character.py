from marshmallow import EXCLUDE
from restapi.extensions.serealizer import ma
from restapi.models.character import Character

class CharacterSchema(ma.ModelSchema):
    class Meta:
        model = Character
        unknown = EXCLUDE