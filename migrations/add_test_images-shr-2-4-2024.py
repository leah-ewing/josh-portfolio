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

shr_images = [{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-1.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-2.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-3.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-4.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-5.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-6.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-7.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-8.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-9.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-10.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-11.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-12.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
},{
    "image_url": f"/static/media/gallery-photos/Sierra High Route/sierra-high-route-test-13.jpeg",
    "image_description": "At risus viverra adipiscing at in tellus integer feugiat scelerisque. Nulla posuere sollicitudin aliquam ultrices sagittis orci. Posuere morbi leo urna molestie at elementum eu facilisis sed.",
    "trip_id": 4
}]

for image in shr_images:
    crud.create_image(image['image_url'], image['image_description'], image['trip_id'])