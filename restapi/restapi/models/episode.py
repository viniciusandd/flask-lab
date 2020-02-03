from restapi.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    episode = db.Column(db.String, nullable=False)
    # air_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Episode %r>' % self.name