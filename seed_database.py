"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb {DATABASE NAME}')
os.system('createdb {DATABASE NAME}') # $createdb {DATABASE NAME}

model.connect_to_db(server.app)
model.db.create_all()