from flask import Flask
from flask import request

from models import db


app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {
    "db": "mymba-feeder-teste",
    "host": "mongo",
    "username": "root",
    "password": "example",
    'authentication_source': 'admin'
}


db.init_app(app)


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
    app.run(debug=True, host="0.0.0.0", port=5000)
