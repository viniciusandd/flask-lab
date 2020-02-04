from marshmallow import EXCLUDE
from restapi.extensions.serealizer import ma
from restapi.models.episode import Episode

class EpisodeSchema(ma.ModelSchema):
    class Meta:
        model = Episode
        unknown = EXCLUDE