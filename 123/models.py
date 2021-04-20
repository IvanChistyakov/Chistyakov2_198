
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    price = db.Column(db.Integer)