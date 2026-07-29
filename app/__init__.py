from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import Models
    from app.models.user import User
    from app.models.announcement import Announcement
    from app.models.community import Community
    from app.models.note import Note
    from app.models.placement import Placement
    
    # Register Blueprints
    from app.routes.home import home
    app.register_blueprint(home)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.dashboard import dashboard
    app.register_blueprint(dashboard)

    from app.routes.announcement import announcement
    app.register_blueprint(announcement)

    from app.routes.community import community
    app.register_blueprint(community)

    from app.routes.note import note
    app.register_blueprint(note)

    from app.routes.profile import profile
    app.register_blueprint(profile)

    from app.routes.placement import placement
    app.register_blueprint(placement)

    return app