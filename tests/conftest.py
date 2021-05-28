# fallowing flask mongoengine docks -> https://github.com/MongoEngine/flask-mongoengine/blob/master/tests/conftest.py
# fixture scope -> https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

import pytest
from datetime import datetime
import mongoengine
from flask import Flask
from flask_mongoengine import MongoEngine
from faker import Faker

from mymba_feeder.models import HotspotModel
from mymba_feeder.app import create_app

@pytest.fixture(scope="module")  
def app():
    """
    Create a new flask app instance for a testing environment with context
    https://flask.palletsprojects.com/en/1.1.x/appcontext/
    """
    app = create_app()

    app.config["TESTING"] = True  # disable error catching
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["DEBUG"] = False

    with app.app_context():
        yield app

    mongoengine.connection.disconnect_all()


@pytest.fixture(scope="module")
def db(app):
    """
    return a testing database to be use in tests
    """

    mongoengine.disconnect_all()

    app.config["MONGODB_SETTINGS"]["db"] = "mymbafeeder_test"

    test_db = MongoEngine(app)

    db_name = test_db.connection.get_database("mymbafeeder_test").name

    if not db_name.endswith("_test"):
        raise RuntimeError(
            f"DATABASE PATH must point to testing db, not to '{db_name}'"
        )
    
    yield test_db

    # clear db after testing
    test_db.connection.drop_database(db_name)


@pytest.fixture()
def hotspot_model(db):
    """
    Return the hotspot model class as a fixture
    """

    return HotspotModel

@pytest.fixture(scope="module",  autouse=True)
def fake_dict_latlng():
    """
    Return a random fake dict(lat, lng) using random coordinates from faker
    """
    fake = Faker()
    lat, lng = fake.latlng()
    return {"latitude": float(lat), "longitude": float(lng)}
