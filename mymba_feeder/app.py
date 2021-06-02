import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

from .models import db, HotspotModel
from .data_manager import HotspotManager


def create_app():

    app = Flask(__name__)

    app.config["MONGODB_SETTINGS"] = {
        "db": os.getenv("DATABASE_NAME", "mymbafeeder"),
        "host": os.getenv("DATABASE_HOST", "localhost"),
        "username": os.getenv("DATABASE_USER", "root"),
        "password": os.getenv("DATABASE_PASSWORD", "example"),
        'authentication_source': 'admin'
    }

    db.init_app(app)

    @app.route("/hotspot/", methods=("GET", "POST", "PUT"))
    def hotspots():
        print("está aqui")
        if request.method == "POST": 
            response = make_response(
                jsonify(HotspotManager().insert(request.get_json())), 201)
            return response
        else:
            return make_response(
                jsonify(HotspotModel.objects()), 200)

    @app.route("/hotspot/<title>/", methods=("GET", "PATCH", "PUT", "DELETE"))
    def hotspot(title):
        print("ou está aqui")
        print("-->", request.method)
        if request.method == "GET":
            return make_response(
                jsonify(HotspotManager().get_by_title(title)), 200
            )
        elif request.method == "PATCH" or request.method == "PUT":
            return make_response(
                jsonify(HotspotManager().update(title, request.get_json())), 200)

    @app.route("/<name>")
    def name(name):
        return "hello {}".format(name)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)
