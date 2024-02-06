import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)

""" 
Slideshow Image:

slideshow_image_url: String
slideshow_image_category: String
"""

music_slideshow_images = ['/static/media/slideshow-photos/music-slideshow-photos/music-test-1.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-2.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-3.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-4.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-5.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-6.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-7.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-8.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-9.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-10.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-11.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-12.jpeg',
                          '/static/media/slideshow-photos/music-slideshow-photos/music-test-13.jpeg']


for image in music_slideshow_images:
    crud.create_slideshow_image(image, 'music')

