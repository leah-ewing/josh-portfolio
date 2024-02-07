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
    trip_name = db.Column(db.String, unique = True)
    trip_location = db.Column(db.String)
    trip_date = db.Column(db.String)
    trip_description = db.Column(db.String)


class Image(db.Model):
    """ Images Corresponding to a Trip """

    __tablename__ = 'image'
    
    image_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    image_url = db.Column(db.String, unique = True)
    image_description = db.Column(db.String)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.trip_id'))

    
class Slideshow(db.Model):
    """ Slideshow Images Corresponding to a Category """

    __tablename__ = 'slideshow_image'
    
    slideshow_image_id = db.Column(db.Integer, 
                        autoincrement = True,
                        primary_key = True)
    slideshow_image_url = db.Column(db.String, unique = True)
    slideshow_image_category = db.Column(db.String)


class Admin(db.Model):
    """ Admin user credentials """

    __tablename__ = 'admin_user'

    admin_user_id = db.Column(db.Integer, 
                              autoincrement = True,
                              primary_key = True)
    admin_user_username = db.Column(db.String, unique = True)
    admin_user_password = db.Column(db.String)


if __name__ == '__main__':
    from server import app
    
    db.connect_to_db(app)

    with app.app_context():
        db.create_all()