# uses pytest-flask

def test_request(client):
    assert client.get("/hotspot").status_code == 404