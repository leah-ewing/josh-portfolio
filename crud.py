"""CRUD operations."""

from model import db, connect_to_db, Trip, Image


def create_trip(trip_name, trip_location, trip_date, trip_description):
    """ Create and return a month """

    new_trip = Trip(trip_name = trip_name,
                    trip_location = trip_location,
                    trip_date = trip_date,
                    trip_description = trip_description)

    db.session.add(new_trip)
    db.session.commit()

    return new_trip


def create_image(image_url, image_description, trip_id):
    """ Create and return a new image """

    new_image = Image(image_url = image_url,
                      image_description = image_description,
                      trip_id = trip_id)
    
    db.session.add(new_image)
    db.session.commit()

    return new_image


if __name__ == '__main__':
    from server import app
    connect_to_db(app)