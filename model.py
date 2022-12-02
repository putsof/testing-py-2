from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.

    game_one = Game(name='monopoly', description='a family fun board game')
    game_two = Game(name='set', description='a thrilling matching game')
    game_three = Game(name='uno', description='a popular game to play with friends and family')

    db.session.add_all([game_one,game_two, game_three])
    db.session.commit()
    


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
