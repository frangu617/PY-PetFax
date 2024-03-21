from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    fact = db.Column(db.String(255), nullable=False)

    def __init__(self, name, fact):
        self.name = name
        self.fact = fact