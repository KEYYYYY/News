from datetime import datetime

from app import db


class Comment(db.EmbeddedDocument):
    username = db.StringField(max_length=64, required=True)
    content = db.StringField(required=True)


class New(db.Document):
    title = db.StringField(max_length=128, required=True)
    timestamp = db.DateTimeField(default=datetime.now)
    is_valid = db.BooleanField(default=True)
    content = db.StringField()
    category = db.StringField(
        max_length=32,
        choices=('生活', '科技')
    )
    comments = db.ListField(db.EmbeddedDocumentField(Comment))

    def __repr__(self):
        return self.title

    meta = {
        'collection': 'news',
        'ordering': ['-timestamp'],
    }
