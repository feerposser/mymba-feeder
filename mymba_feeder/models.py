import datetime

from flask_mongoengine import MongoEngine


db = MongoEngine()

class HotspotModel(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.StringField()
    sponsors = db.ListField()
    contributors = db.ListField()
    position = db.DictField()
    created = db.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
