from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES

from config import Config

db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    configure_uploads(app, photos)

    from app.home import views as home_views
    from app.admin import views as admin_views
    app.register_blueprint(home_views.home)
    app.register_blueprint(admin_views.admin, url_prefix='/admin')
    return app
