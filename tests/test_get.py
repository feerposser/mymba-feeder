# uses pytest-flask

def test_get_hotspots(client):
    """
    request a http get to /hotspot ang check if the answer is a 
    list of hotspot objetcs and status code 200
    """
    response = client.get("/hotspot/")
    data = response.json

    assert response.status_code == 200, "status code not 200"
    assert isinstance(data, list), "data response is not a list instance"
    assert len(data) > 40, "len of indices list response less than 40. Maybe fake data not be inserted in db tests"

def test_get_by_title_200(client):
    """
    make a get request to /hotspot/title/ and check if status code equals to 200
    """
    title = client.get("/hotspot/").get_json()[-1]["title"]
    response = client.get("/hotspot/{}/".format(title))

    assert response.status_code == 200, "get not ok"

def test_get_by_title_check_response(client):
    """
    get the title of the last hotspot resource
    make a http get searching by the title and check if
    the titles matches
    """
    title = client.get("/hotspot/").get_json()[-1]["title"]
    response = client.get("/hotspot/{}/".format(title))

    assert "title" in response.json, "title not in response"
    assert title == response.json["title"], "title is not the same"

def test_get_by_title_404(client):
    """
    make a http get for a title that not being used by a resource
    and check if the status code equals to 404
    """
    response = client.get("/hotspot/a title that not being used/")

    assert response.status_code == 404, "status code not equals to 404"
