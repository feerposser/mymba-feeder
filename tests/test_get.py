# uses pytest-flask

def test_request_get_response_200(client):
    """
    request a http get and test if status code equals 200
    """
    assert client.get("/hy_there").status_code == 200

def test_get_hotspots(client):
    """
    request a http get to /hotspot ang check if the answer is a 
    list of hotspot objetcs 
    """
    response = client.get("/hotspot/")

    assert response.status_code == 200, \
        "status code not 200"
    
    data = response.json

    assert isinstance(data, list), \
        "data response is not a list instance"

    assert len(data) > 40, \
        "len of indices list response less than 40. Maybe fake data not be inserted in db tests"

def test_get_by_title_200(client):
    """
    make a get request to /hotspot/title/
    """
    title = client.get("/hotspot/").get_json()[-1]["title"]
    response = client.get("/hotspot/{}/".format(title))

    assert response.status_code == 200, "get not ok"
    assert "title" in response.json, "title not in response"
    assert title == response.json["title"], "title is not the same"

def test_get_by_title_check_response(cliente):
    raise AssertionError("not implemented")

def test_get_by_title_404(client):
    raise AssertionError("not implemented")
