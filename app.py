from flask import Flask
from flask import request

app = Flask("Mymba Feeder")


@app.route("/", methods=["GET"])
def index():
    if request.method == "POST":
        return "Hello World"


@app.route("/<name>")
def name(name):
    return "hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
