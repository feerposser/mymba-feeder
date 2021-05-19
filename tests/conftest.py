# fallowing flask mongoengine docks -> https://github.com/MongoEngine/flask-mongoengine/blob/master/tests/conftest.py
# fixture scope -> https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

import pytest
from datetime import datetime
import mongoengine
from flask import Flask
from flask_mongoengine import MongoEngine


@pytest.fixture(scope="module")  
def app():
    """
    Create a new flask app instance for a testing environment
    """
    app = Flask("teste")

    app.config["TESTING"] = True  # disable error catching
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["DEBUG"] = False

    with app.app_context(): # https://flask.palletsprojects.com/en/1.1.x/appcontext/
        yield app

    mongoengine.connection.disconnect_all()


@pytest.fixture(scope="module")
def db(app):
    """
    return a testing database to be use in tests
    """

    app.config["MONGODB_SETTINGS"] = {
        "db": "mymbafeeder_test",
        "host": "localhost",
        "username": "root",
        "password": "example",
        'authentication_source': 'admin'
    }

    test_db = MongoEngine(app)

    db_name = test_db.connection.get_database("mymbafeeder_test").name

    if not db_name.endswith("_test"):
        raise RuntimeError(
            f"DATABASE PATH must point to testing db, not to '{db_name}'"
        )
    
    yield test_db

    # clear db after testing
    # test_db.connection.drop_database(db_name)


@pytest.fixture()
def todo_model(db):
    """
    Return an mongodb to do list for testing
    """
    class Todo(db.Document):
        title = mongoengine.StringField(max_length=60)
        text = mongoengine.StringField()
        done = mongoengine.BooleanField(default=False)
        pub_date = mongoengine.DateTimeField(default=datetime.utcnow)
        comments = mongoengine.ListField(mongoengine.StringField())
        comment_count = mongoengine.IntField()

    return Todo
