import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)

directory = f'{ROOT_FOLDER}/static/media/about-page-photos'

""" 
Slideshow Image:

slideshow_image_url: String
slideshow_image_category: String
"""

url_num = 1

while url_num < len(os.listdir(directory)) + 1:
    about_page_image = f'/static/media/about-page-photos/about-test-{url_num}.jpg'
    crud.create_slideshow_image(about_page_image, 'about')
    url_num += 1