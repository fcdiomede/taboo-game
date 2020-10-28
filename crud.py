"""CRUD operations"""

from model import db, Card

def create_card(keyword, buzzword_1, buzzword_2, buzzword_3, 
                buzzword_4, buzzword_5, room_id=None, player_created=False):
    """Create and return a new Taboo card"""

    card = Card(room_id=room_id, keyword=keyword, buzzword_1=buzzword_1, 
                buzzword_2=buzzword_2, buzzword_3=buzzword_3, 
                buzzword_4=buzzword_4, buzzword_5=buzzword_5, 
                player_created=player_created)

    db.session.add(card)
    db.session.commit()

    return card