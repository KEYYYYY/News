from flask import Flask
from flask_mongoengine import MongoEngine

from config import Config

db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.home import views as home_views
    from app.admin import views as admin_views
    app.register_blueprint(home_views.home)
    app.register_blueprint(admin_views.admin, url_prefix='/admin')
    return app
