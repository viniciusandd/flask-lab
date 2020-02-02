class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    episode = db.Column(db.String, nullable=False)
    air_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Episode %r>' % self.name