#  test connection with database

# fallows -> https://github.com/MongoEngine/flask-mongoengine/blob/master/tests/test_connection.py

import random
from flask_mongoengine import current_mongoengine_instance
from mongoengine.errors import DoesNotExist

def insert_fake_data_in_db(hotspot_model, faker, fake_dict_latlng):
    """
    Insert fake data in database
    """
    hotspot = hotspot_model()

    hotspot.title = faker.unique.name()
    for _ in range(random.randint(1, 7)):
        hotspot.sponsors.append(faker.name())
    for _ in range(random.randint(1, 4)):
        hotspot.contributors.append(faker.name())
    hotspot.position = fake_dict_latlng

    hotspot.save()

def test_connection(db):
    """
    test if current mongo conn is the same as used by testing app
    """
    assert current_mongoengine_instance() == db, \
        "Current mongo instance is not the same as the test"

def test_insert_hotspots_in_db(hotspot_model, faker, fake_dict_latlng):
    try:
        for _ in range(0, 50):
            insert_fake_data_in_db(hotspot_model, faker, fake_dict_latlng)
    except Exception as e:
        raise AssertionError(str(e))

def test_retrieve_hotspots_from_db(hotspot_model):
    assert len(hotspot_model.objects()) > 0

def test_delete_hotspot_from_db(hotspot_model):
    try:
        hotspot = hotspot_model.objects.first()

        hotspot.delete()

        assert len(hotspot_model.objects(title=hotspot.title)) == 0, "hotspot was not deleted"
    except DoesNotExist as dne:
        raise AssertionError(dne)
    except Exception as e:
        raise AssertionError(str(e))