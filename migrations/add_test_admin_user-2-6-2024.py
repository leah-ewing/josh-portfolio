import sys, os

ROOT_FOLDER = os.environ['ROOT_FOLDER']
sys.path.append(ROOT_FOLDER)

import crud
import model
import server

model.connect_to_db(server.app)


""" 
Admin User:

admin_user_username = String
admin_user_password = String
"""

crud.create_admin_user('test', 'test')