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


def get_trip_by_name(trip_name):
    """ Returns information for a trip, given a name """

    trips = Trip.query.all()

    for trip in trips:
        if trip.trip_name == trip_name:
            return trip
        

def get_image_from_id(image_id):
    """ Returns information for an image, given an id """

    images = Image.query.all()

    for image in images:
        if image.image_id == image_id:
            return image


def get_trip_images_by_id(trip_id):
    """ Returns images for a trip given a trip_id """

    images = Image.query.all()
    trip_images = []

    for image in images:
        if image.trip_id == trip_id:
            trip_images.append(image)
    
    return trip_images


def get_all_trip_names():
    """ Returns a list of all trip names in the db """

    trips = Trip.query.all()
    trip_names = []
    
    for trip in trips:
        trip_names.append(trip.trip_name)
    
    return trip_names


def get_trip_from_id(trip_id):
    """ Returns a trip given a trip_id """

    trips = Trip.query.all()
    
    for trip in trips:
        if trip.trip_id == trip_id:
            return trip
            

if __name__ == '__main__':
    from server import app
    connect_to_db(app)