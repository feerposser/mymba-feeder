import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

from models import db, HotspotModel
from request_manager import RequestManager
from data_manager import DataManager


app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {
    "db": os.getenv("DATABASE_NAME", "mymbafeeder"),
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "username": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", "example"),
    'authentication_source': 'admin'
}


db.init_app(app)


@app.route("/hotspot", methods=["GET", "POST"])
def index():
    if request.method == "POST":
            
        response = make_response(
            jsonify(
                DataManager().insert(request.get_json())), 
                200)
        
        return response
        
    else:
        return make_response(
            jsonify(HotspotModel.objects()),
            200)


@app.route("/<name>")
def name(name):
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
