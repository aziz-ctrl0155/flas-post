from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pathlib

db = SQLAlchemy()

DB_NAME = "database.sqlite"
BASE_PATH = pathlib.Path(__file__).parent
DB_PATH = path.join(BASE_PATH, 'database', DB_NAME)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'LKLDSFLsASAKDSNF'
    from .views import home
    from .views.posts import posts
    from .views.account import auth
    """ registering BluePrints """
    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(posts)

    """Db Configurations"""
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    create_db(app)

    """CSRF configuration"""

    return app


def create_db(app):
    print(DB_PATH)
    if not path.exists(DB_PATH):
        db.create_all(app=app)
