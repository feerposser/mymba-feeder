import pytest
from datetime import datetime

import mongoengine
from flask import Flask
from flask_mongoengine import MongoEngine


@pytest.fixture()
def app():
    app = Flask(__name__)

    app.config["TESTING"] = True  # disable error catching

    with app.app_context(): # https://flask.palletsprojects.com/en/1.1.x/appcontext/
        yield app

    mongoengine.connection.disconnect_all()


@pytest.fixture()
def db(app):
    app.config["MONGODB_HOST"] = os.getenv("DATABASE_HOST", "localhost"),
    test_db = MongoEngine(app)
    db_name = test_db.connection.get_database(os.getenv("DATABASE_HOST", "localhost")).name

    print(db_name)
    if not db_name.endswith("_test_db"):
        raise RuntimeError(
            f"DATABASE_URL must point to testing db, not to master db ({db_name})"
        )
    
    # clear db before testing
    test_db.connection.drop_database(db_name)

    yield test_db

    # clear db after testing
    test_db.connection.drop_database(db_name)


@pytest.fixture()
def todo(db):
    class Todo(db.Document):
        title = mongoengine.StringField(max_length=60)
        text = mongoengine.StringField()
        done = mongoengine.BooleanField(default=False)
        pub_date = mongoengine.DateTimeField(default=datetime.utcnow)
        comments = mongoengine.ListField(mongoengine.StringField())
        comment_count = mongoengine.IntField()

    return 