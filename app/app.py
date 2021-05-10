import os

from flask import Flask
from flask import request
from flask import jsonify

from models import db, HotspotModel
from request_manager import RequestManager


app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {
    "db": os.getenv("DATABASE_NAME", "mymba-feeder-teste"),
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "username": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", "example"),
    'authentication_source': 'admin'
}


db.init_app(app)


@app.route("/hotspot", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        RequestManager(request).is_valid([*HotspotModel()._data.keys()])

        hotspot = HotspotModel()

        data = request.get_json()

        hotspot.title = data["title"]
        hotspot.description = data["description"]
        hotspot.sponsors = data["sponsors"]
        hotspot.contributors = data["contributors"]
        hotspot.position = data["position"]

        hotspot.save()

        return jsonify(HotspotModel.objects())
    else:
        return jsonify(HotspotModel.objects())


@app.route("/<name>")
def name(name):
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
