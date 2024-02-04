from flask import Flask, render_template
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'dev'
app.static_folder = 'static'
app.app_context().push()


@app.route('/')
def homepage():
    """ Directs a user to the homepage """

    return render_template("homepage.html")


@app.route('/about')
def about_page():
    """ Directs a user to the 'about' page """

    return render_template("about.html")


@app.route('/music')
def music_page():
    """ Directs a user to the 'music' page """

    return render_template("music.html")


@app.route('/nature')
def nature_page():
    """ Directs a user to the 'nature' page """

    return render_template("nature.html")


@app.route('/resume')
def resume_page():
    """ Directs a user to the 'resume' page """

    return render_template("resume.html")


@app.route('/gallery/<trip_name>', methods = ["GET"])
def gallery_page(trip_name):
    """ Directs a user to the 'gallery' page """

    trip = crud.get_trip_by_name(trip_name)
    trip_images = crud.get_trip_images_by_id(trip.trip_id) # returns an array of image information

    return render_template("gallery.html",
                           trip_name = trip.trip_name,
                           trip_description = trip.trip_description) # add trip images


@app.route('/image_info/<image_id>', methods = ["GET"])
def image_info_page(image_id):
    """ Directs a user to an image's info page """

    image = crud.get_image_from_id(image_id)
    trip = crud.get_trip_from_id(image.trip_id)

    return render_template("image_info.html",
                           trip_name = trip.trip_name,
                           trip_location = trip.trip_location,
                           trip_date = trip.trip_date,
                           image_description = image.image_description)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)