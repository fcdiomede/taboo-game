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

with open('data/cards.json') as f:
    cards_data = json.loads(f.read())

    for card in cards_data:
        keyword = card["keyword"]
        buzzword_1 = card["buzzword_1"]
        buzzword_2 = card["buzzword_2"]
        buzzword_3 = card["buzzword_3"]
        buzzword_4 = card["buzzword_4"]
        buzzword_5 = card["buzzword_5"]

        crud.create_card(keyword, buzzword_1, buzzword_2, buzzword_3, 
                         buzzword_4, buzzword_5)