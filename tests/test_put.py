
def test_update_hotspot_200(client):
    raise AssertionError("not implemented")

def test_update_hotspot_check_response(client):
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

def test_update_hotspot_duplated_title(client):
    raise AssertionError("not implemented")
