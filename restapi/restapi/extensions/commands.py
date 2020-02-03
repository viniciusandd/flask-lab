from restapi.extensions.database import db
from restapi.models.character import Character
from restapi.models.episode import Episode

def init_app(app):
    @app.cli.command()
    def populatedb():
        characters = [
            Character(id=1, name='Rick Sanchez', gender='Male', specie='Human'),
            Character(id=2, name='Morty Smith', gender='Male', specie='Human'),
            Character(id=3, name='Summer Smith', gender='Female', specie='Human')
        ]
        db.session.bulk_save_objects(characters)

        episodes = [
            Episode(id=1, name='Pilot', episode='S01E01'),
            Episode(id=2, name='Lawnmower Dog', episode='S01E02'),
            Episode(id=3, name='Anatomy Park', episode='S01E03')
        ]
        db.session.bulk_save_objects(episodes)
        db.session.commit()

    @app.cli.command()
    def createdb():
        db.create_all()

    @app.cli.command()
    def dropdb():
        db.drop_all()
