from flask import Flask
from flask import request
from flask_mongoengine import MongoEngine
import mongoengine as me

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "mymba-feeder-teste",
    "host": "mongo",
    "username": "root",
    "password": "example",
    'authentication_source': 'admin'
}

db = MongoEngine(app)


class HotspotModel(me.Document):
    title = me.StringField(required=True)
    contributors = me.ListField()
    latitude = me.FloatField()
    longitude = me.FloatField()

    def __str__(self):
        return self.title


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Hello World"
    else:
        return "GETTTTT"


@app.route("/<name>")
def name(name):
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
