from datetime import datetime

from app import mongo


class New(mongo.Document):
    title = mongo.StringField(max_length=128, required=True)
    timestamp = mongo.DateTimeField(default=datetime.now)
    content = mongo.StringField()
    category = mongo.StringField(
        max_length=32,
        choices=(('life', '生活'), ('tech', '科技'))
    )

    meta = {
        'collections': 'news'
    }
