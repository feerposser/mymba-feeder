# test app config (uses pytest-flask)

def test_app_name_is_teste(app):
    assert app.name == "teste"

def test_app_config(config):
    assert config["DEBUG"] is False
    assert config["WTF_CSRF_ENABLED"] is False
    assert config["TESTING"] is True