"""Script to seed database"""

import os
import json

import crud
import model
import server

os.system('dropdb taboo')
os.system('createdb taboo')

model.connect_to_db(server.app)
model.db.create_all()