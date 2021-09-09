from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db_name = "database.sqlite"


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
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    create_db(app)

    """CSRF configuration"""

    return app


def create_db(app):
    pass
