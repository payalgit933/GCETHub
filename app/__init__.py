from flask import Flask
from config import Config

from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import Models
    from app.models.user import User

    # Register Blueprints
    from app.routes.home import home

    app.register_blueprint(home)

    with app.app_context():
        db.create_all()

    return app