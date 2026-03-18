from . import db

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    category = db.Column(db.String(100))
    filename = db.Column(db.String(200))
