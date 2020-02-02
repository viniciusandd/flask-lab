class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<Character %r>' % self.name