from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///josh-portfolio-db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class Trip(db.Model):
    """ Nature Trips """

    __tablename__ = 'trip'

    trip_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    trip_name = db.Column(db.String)
    trip_location = db.Column(db.String)
    trip_date = db.Column(db.String)


class Image(db.Model):
    """ Trip Images """

    __tablename__ = 'image'
    image_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    image_url = db.Column(db.String)
    trip_id = db.Column(db.String, db.ForeignKey('trip.trip_id'))