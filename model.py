"""Models for Taboo app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri='postgresql:///taboo', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class Card(db.Model):
    """A Taboo card"""

    __tablename__ = "cards"

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)
    room_id = db.Column(db.String)
    keyword = db.Column(db.String, nullable=False)
    buzzword_1 = db.Column(db.String)
    buzzword_2 = db.Column(db.String)
    buzzword_3 = db.Column(db.String)
    buzzword_4 = db.Column(db.String)
    buzzword_5 = db.Column(db.String)
    player_created = db.Column(db.Boolean, default=False, nullable=False)


    def __repr__(self):
        """Show human-readable info about card"""

        return f"<Card id={self.id} keyword={self.keyword}>"


if __name__ == '__main__':
    from server import app

    connect_to_db(app)