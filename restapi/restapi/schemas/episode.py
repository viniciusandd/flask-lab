from restapi.extensions.serealizer import ma
from restapi.models.episode import Episode

class EpisodeSchema(ma.ModelSchema):
    class Meta:
        model = Episode