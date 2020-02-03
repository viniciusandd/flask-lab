from restapi.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Character(db.Model, SerializerMixin):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    specie = db.Column(db.String, nullable=False)
    # created = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<Character %r>' % self.name