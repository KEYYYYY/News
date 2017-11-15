from datetime import datetime

from app import db
from app import photos


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    add_time = db.Column(db.DateTime, default=datetime.now)
    is_valid = db.Column(db.Boolean, default=False)
    # 图片名
    photo = db.Column(db.String(128))
    # 缩略图名
    photo_t = db.Column(db.String(128))
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))

    @property
    def photo_url(self):
        return photos.url(self.photo)

    @photo_url.setter
    def photo_url(self, url):
        raise AttributeError('图片URL不可以修改')

    @property
    def photo_t_url(self):
        return photos.url(self.photo_t)

    @photo_t_url.setter
    def photo_t_url(self, url):
        raise AttributeError('缩略图URL不可以修改')

    def __repr__(self):
        return self.title


class Category(db.Model):
    __tablename__ = 'categorys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    news = db.relationship('News', backref='category')

    def __repr__(self):
        return self.name
