from flask import Flask, render_template
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime
from model import connect_to_db


app = Flask(__name__)
app.secret_key = 'dev'
app.static_folder = 'static'
app.app_context().push()


@app.route('/')
def homepage():
    """ Directs a user to the homepage """

    return render_template("homepage.html")


## login logic (correct/incorrect credentials, login session)


@app.route('/about')
def about_page():
    """ Directs a user to the 'about' page """

    about_slideshow_images = crud.get_slideshow_images_from_category('about')

    return render_template("about.html",
                           about_slideshow_images = about_slideshow_images)


@app.route('/music')
def music_page():
    """ Directs a user to the 'music' page """

    music_slideshow_images = crud.get_slideshow_images_from_category('music')

    return render_template("music.html",
                           music_slideshow_images = music_slideshow_images)


@app.route('/nature')
def nature_page():
    """ Directs a user to the 'nature' page """

    trip_names = crud.get_all_trip_names()
    nature_slideshow_images = crud.get_slideshow_images_from_category('nature')

    return render_template("nature.html",
                           trip_names = trip_names,
                           nature_slideshow_images = nature_slideshow_images)


@app.route('/resume')
def resume_page():
    """ Directs a user to the 'resume' page """

    return render_template("resume.html")


@app.route('/gallery/<trip_name>', methods = ["GET"])
def gallery_page(trip_name):
    """ Directs a user to the 'gallery' page """

    trip = crud.get_trip_by_name(trip_name)
    trip_images = crud.get_trip_images_by_id(trip.trip_id)

    return render_template("gallery.html",
                           trip_name = trip.trip_name,
                           trip_date = trip.trip_date,
                           trip_description = trip.trip_description,
                           trip_images = trip_images)


@app.route('/image_info/<image_id>', methods = ["GET"])
def image_info_page(image_id):
    """ Directs a user to an image's info page """

    image = crud.get_image_from_id(int(image_id))
    trip = crud.get_trip_from_id(image.trip_id)

    return render_template("image_info.html",
                           image = image.image_url,
                           trip_name = trip.trip_name,
                           trip_location = trip.trip_location,
                           trip_date = trip.trip_date,
                           image_description = image.image_description)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port=8000)