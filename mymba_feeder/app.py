import os

from flask import Flask
from flask import request
from flask import jsonify, abort
from flask import make_response
from mongoengine.errors import NotUniqueError

from mymba_feeder.models import db, HotspotModel
from mymba_feeder.data_manager import HotspotManager


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

    @app.errorhandler(409)
    def conflict_duplicate_resource_errorhandler(message):
        response = make_response(str(message))
        response.status_code = 409
        return response

    @app.route("/hotspot/", methods=("GET", "POST"))
    def hotspots():
        if request.method == "POST": 
            try:
                return make_response(jsonify(HotspotManager().insert(request.get_json())), 201)
            except NotUniqueError as n:
                abort(409, n)
        else:
            return make_response(jsonify(HotspotModel.objects()), 200)

    @app.route("/hotspot/<title>/", methods=("GET", "PATCH", "PUT", "DELETE"))
    def hotspot(title):
        if request.method == "GET":
            return make_response(jsonify(HotspotManager().get_by_title(title)), 200)

        elif request.method == "PATCH" or request.method == "PUT":
            try:
                return make_response(jsonify(HotspotManager().update(title, request.get_json())), 200)
            except NotUniqueError as n:
                abort(409, n)

        elif request.method == "DELETE":
            HotspotManager().delete(title)
            response = make_response()
            response.status_code = 204
            return response

    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)
