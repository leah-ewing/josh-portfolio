"""CRUD operations."""

from model import db, connect_to_db, Trip, Image, Slideshow, Admin


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


def create_slideshow_image(slideshow_image_url, slideshow_image_category):
    """ Create and return a new slideshow image """

    new_slideshow_image = Slideshow(slideshow_image_url = slideshow_image_url,
                      slideshow_image_category = slideshow_image_category)
    
    db.session.add(new_slideshow_image)
    db.session.commit()

    return new_slideshow_image


def create_admin_user(username, password):
    """ Creates a new admin user """

    new_admin_user = Admin(admin_user_username = username, 
                           admin_user_password = password)

    db.session.add(new_admin_user)
    db.session.commit()

    return new_admin_user


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
        

def get_slideshow_images_from_category(slideshow_image_category):
    """ Returns slideshow images for a given category """

    slideshow_images = Slideshow.query.all()
    slideshow_image_list = []

    for slideshow_image in slideshow_images:
        if slideshow_image.slideshow_image_category == slideshow_image_category:
            slideshow_image_list.append(slideshow_image.slideshow_image_url)

    return slideshow_image_list        


def check_for_admin_user(username, password):
    """ Returns a boolean representing whether an admin user is found in the database """

    admin_users = Admin.query.all()

    for admin_user in admin_users:
        if admin_user.admin_user_username.lower() == username.lower():
            if admin_user.admin_user_password.lower() == password.lower():
                return True
    return False


if __name__ == '__main__':
    from server import app
    connect_to_db(app)