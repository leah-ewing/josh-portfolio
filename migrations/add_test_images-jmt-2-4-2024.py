import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)

""" 
Image:

image_url: String
image_description: String
trip_id: Integer
"""

jmt_images = [{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-1.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-2.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-3.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-4.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-5.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-6.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-7.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-8.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-9.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-10.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-11.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-12.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
},{
    "image_url": f"/static/media/gallery-photos/John Muir Trail/jmt-test-13.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 1
}]

for image in jmt_images:
    crud.create_image(image['image_url'], image['image_description'], image['trip_id'])