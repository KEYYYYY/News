from datetime import datetime

from app import db


class New(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    image = db.Column(db.String(128))
    author = db.Column(db.String(64))
    view_num = db.Column(db.Integer, default=0)
    add_time = db.Column(db.DateTime, default=datetime.now)
    is_valid = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title


class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    news = db.relationship('New', backref='type')

    def __repr__(self):
        return self.name
