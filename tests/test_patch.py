
def patch(title, client, **kwargs):
    resource = dict
    for key, value in kwargs.items():
        resource.update({key: value})

    return client.patch("/hotspot/{}".format(title), json=resource)

def test_patch_descriptio_hotspot_200(client, hotspot_for_patch):
    """
    make a update in the description of a resource and patches
    """
    new_description = "the new description of the resource"

    response = patch(hotspot_for_patch["title"], client, description=new_description)

    # response = client.patch("/hotspot/{}/".format(hotspot_for_patch["title"]), json=dict(
    #     description=new_description
    # ))

    assert response.status_code == 200, "response not equals to 200"

def test_patch_description_hotspot_check_response(client, hotspot_for_patch):
    """
    make an update to /hotspot/title/ using the last data in response
    """
    new_description = "testing put to hotspot update"

    title = hotspot_for_patch["title"]

    patch(title, client, description=new_description)

    # reponse = client.patch("/hotspot/{}/".format(title), json=dict(
    #     description=new_description
    # ))

    response = client.get("hotspot/{}/".format(title)).json

    assert response["title"] == title, "get updated resource failure"
    assert response["description"] == new_description, \
        "resource not updated. new_description({}) not equals to response({})".format(new_description, response["description"])

def test_patch_description_hotspot_404(client):
    """
    make a http patch for a nonexistent resource
    """
    new_description = "testing a 404 description"

    response = patch("nonexistent__resource", client, description=new_description)

    # response = client.patch("/hotspot/nonexistent__resource/", json=dict(
    #     description=new_description
    # ))

    assert response.status_code == 404, "status code response not equals to 404"

def test_patch_sponsors_hotspot_200(client, hotspot_for_patch):
    """
    update sponsors
    """
    title = hotspot_for_patch["title"]
    sponsors = hotspot_for_patch["sponsors"]
    sponsors.append("Bob")

    response = patch(title, client, sponsors=sponsors)

    assert response.status_code == 200, "response not equals to 200"

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