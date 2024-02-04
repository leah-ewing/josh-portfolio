"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

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
            'image_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Smoky Mountains National Park',
            'trip_location': 'Gatlinburg, TN',
            'trip_date': '2021-2023',
            'image_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Grand Canyon National Park',
            'trip_location': 'Gatlinburg, TN',
            'trip_date': '2014',
            'image_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        },
        {
            'trip_name': 'Sierra High Route',
            'trip_location': 'Gatlinburg, TN',
            'trip_date': '2018',
            'image_description': 'Sit amet venenatis urna cursus eget nunc scelerisque viverra mauris. Non arcu risus quis varius quam quisque id diam. Pulvinar mattis nunc sed blandit libero volutpat sed.'
        }]

for trip in trips:
    crud.create_trip(trip)

