"""Script to seed database."""

import os, sys

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

os.system('dropdb josh-portfolio-db')
os.system('createdb josh-portfolio-db')

model.connect_to_db(server.app)
model.db.create_all()


""" Seed Trips """

trips = [{
            'trip_name': 'John Muir Trail',
            'trip_location': 'Yosemite National Park',
            'trip_date': '2016',
            'trip_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Great Smoky Mountains National Park',
            'trip_location': 'Gatlinburg, TN',
            'trip_date': '2021-2023',
            'trip_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Grand Canyon National Park',
            'trip_location': 'Grand Canyon, AZ',
            'trip_date': '2014',
            'trip_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Sierra High Route',
            'trip_location': 'Yosemite National Park',
            'trip_date': '2018',
            'trip_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        }]

for trip in trips:
    crud.create_trip(trip['trip_name'], trip['trip_location'], trip['trip_date'], trip['trip_description'])