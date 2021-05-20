#  test connection with database

# fallows -> https://github.com/MongoEngine/flask-mongoengine/blob/master/tests/test_connection.py

from flask_mongoengine import current_mongoengine_instance

def test_connection(db):
    assert current_mongoengine_instance() == db, \
        "Current mongo instance is not the same as the test"

def test_database_config(db):
    assert db.connection.get_database("mymbafeeder_test").name == "mymbafeeder_test"

def test_insert_db(hotspot_model, fake_name):
    try:
        t = hotspot_model()

        t.title = fake_name
        t.save()
        
        assert "a"=="a"
    except Exception as e:
        raise AssertionError(str(e))
