
def test_patch_descriptio_hotspot_200(client):
    raise AssertionError("not implemented")

def test_patch_description_hotspot_check_response(client):
    """
    make an update to /hotspot using the last data in response
    """
    new_description = "testing put to hotspot update"

    title = client.get("/hotspot/").json[-1]["title"]

    reponse = client.put("/hotspot/{}/".format(title), json=dict(
        description=new_description
    ))

    response = client.get("hotspot/{}/".format(title)).json

    assert response["title"] == title, "get updated resource failure"
    assert response["description"] == new_description, \
        "resource not updated. new_description({}) not equals to response({})".format(new_description, response["description"])

def test_patch_description_hotspot_404(client):
    raise AssertionError("not implemented")

def test_patch_sponsors_hotspot_200(client):
    raise AssertionError("not implemented")

def test_patch_sponsors_hotspot_check_response(client):
    raise AssertionError("not implemented")

def test_patch_sponsors_hotspot_404(client):
    raise AssertionError("not implemented")

def test_patch_contributors_hotspot_200(client):
    raise AssertionError("not implemented")

def test_patch_contributors_hotspot_check_response(client):
    raise AssertionError("not implemented")

def test_patch_contributors_hotspot_404(client):
    raise AssertionError("not implemented")

def test_patch_position_hotspot_200(client):
    raise AssertionError("not implemented")

def test_patch_position_hotspot_check_response(client):
    raise AssertionError("not implemented")

def test_patch_position_hotspot_404(client):
    raise AssertionError("not implemented")