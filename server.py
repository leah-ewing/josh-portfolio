from flask import Flask, render_template
from jinja2 import StrictUndefined
import crud, json
from datetime import datetime

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)