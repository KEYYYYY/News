import os

BASE_DIR = os.path.abspath('.')


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = os.path.abspath('.') + '/uploads'
    SECRET_KEY = '763997136'
