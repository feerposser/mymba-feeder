import os

from flask import Flask
from flask import request
from flask import jsonify

from models import db, HotspotModel


app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {
    "db": os.getenv("DATABASE_NAME", "mymba-feeder-teste"),
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "username": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", "root"),
    'authentication_source': 'admin'
}


db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        print(6,request.get_json()["teste"])

        return "Hello World"
    else:
        return jsonify(HotspotModel.objects())


@app.route("/<name>")
def name(name):
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
