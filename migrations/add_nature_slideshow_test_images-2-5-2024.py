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

nature_slideshow_images = ['/static/media/slideshow-photos/nature-slideshow-photos/nature-test-1.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-3.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-4.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-5.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-6.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-7.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-8.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-9.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-10.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-11.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-12.jpeg',
                           '/static/media/slideshow-photos/nature-slideshow-photos/nature-test-13.jpeg']


for image in nature_slideshow_images:
    crud.create_slideshow_image(image, 'nature')

