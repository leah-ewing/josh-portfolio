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

## Seed 'Grand Canyon' test images:

grand_canyon_images = [{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-1.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-2.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-3.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-4.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-5.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-6.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-7.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-8.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-9.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-10.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-11.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-12.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
},
{
    "image_url": f"{ROOT_FOLDER}/static/media/gallery-photos/Grand Canyon National Park/grand-canyon-test-13.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 3
}]

for image in grand_canyon_images:
    crud.create_image(image['image_url'], image['image_description'], image['trip_id'])