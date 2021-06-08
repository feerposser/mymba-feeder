
def patch(title, client, **kwargs):
    resource = {}
    for key, value in kwargs.items():
        resource.update({key: value})

    return client.patch("/hotspot/{}/".format(title), json=resource)

def test_patch_descriptio_hotspot_200(client, hotspot_for_patch):
    """
    make a update in the description of a resource and patches
    """
    new_description = "the new description of the resource"

    response = patch(hotspot_for_patch["title"], client, description=new_description)

    assert response.status_code == 200, \
        "response not equals to 200. {} instead.".format(response.status_code)

def test_patch_description_hotspot_check_response(client, hotspot_for_patch):
    """
    make an update to /hotspot/title/ using the last data in response
    """
    new_description = "testing patch to hotspot update"

    title = hotspot_for_patch["title"]

    patch(title, client, description=new_description)

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

    assert response.status_code == 404, \
        "status code response not equals to 404. {} instead.".format(response.status_code)

def test_patch_sponsors_hotspot_200(client, hotspot_for_patch):
    """
    update sponsors by title
    """
    title = hotspot_for_patch["title"]
    sponsors = hotspot_for_patch["sponsors"]
    sponsors.append("Bob")

    response = patch(title, client, sponsors=sponsors)

    assert response.status_code == 200, \
        "response not equals to 200. {} instead".format(response.status_code)

def test_patch_sponsors_hotspot_check_response(client, hotspot_for_patch):
    """
    update sponsors by title and check response
    """
    title = hotspot_for_patch["title"]
    sponsors = hotspot_for_patch["sponsors"]
    sponsors.append("Check response")

    response = patch(title, client, sponsors=sponsors)

    for sponsor in response.get_json()["sponsors"]:
        assert sponsor in sponsors, \
            "{} not in sponsors({})".format(sponsor, response.get_json()["sponsors"])
    
    for sponsor in sponsors:
        assert sponsor in response.get_json()["sponsors"], \
            "{} not in response".format(sponsor)

def test_patch_sponsors_hotspot_404(client):
    """
    update sponsors using a invalid title
    """
    title = "an impossible used titlee"

    response = patch(title, client, sponsors=["Jack Shephard", "Sayid Jarrah"])

    assert response.status_code == 404, \
        "response not equals to 404. {} instead.".format(response.status_code)

def test_patch_contributors_hotspot_200(client, hotspot_for_patch):
    """
    update contributors by title and get 200 status code response
    """
    title = hotspot_for_patch["title"]
    contributors = hotspot_for_patch["contributors"]
    contributors.append("Christian Shephard")

    response = patch(title, client, contributors=contributors)

    assert response.status_code == 200, \
        "resppnse status code not equals to 200. {} instead.".format(response.status_code)

def test_patch_contributors_hotspot_check_response(client, hotspot_for_patch):
    """
    update contributors by title and check the update
    """
    title = hotspot_for_patch["title"]
    contributors = hotspot_for_patch["contributors"]
    contributors.append("Madison the Dog")

    response = patch(title, client, contributors=contributors)

    for contributor in response.get_json()["contributors"]:
        assert contributor in contributors, \
            "response contributor({}) not in contributors({})".format(contributor, contributors)

    for contributor in contributors:
        assert contributor in response.get_json()["contributors"], \
            "contributor({}) not in response contributors({})".format(contributor, response.get_json()["contributors"])

def test_patch_contributors_hotspot_404(client):
    """
    update a hotspot by a invalid title and get a 404 status code response
    """
    title = "See you in another life, brother"
    contributors = ["Desmond Humes"]

    response = patch(title, client, contributors=contributors)
    
    assert response.status_code == 404, \
        "response not equals to 404. {} instead.".format(response.status_code)

def test_patch_position_hotspot_200(client, hotspot_for_patch):
    """
    update a hotspot position by title and get a 200 status code response
    """
    title = hotspot_for_patch["title"]
    position = {"latitude": 50, "longitude": 50}

    response = patch(title, client, position=position)

    assert response.status_code == 200, \
        "response not equals to 200. {} instead.".format(response.status_code)

def test_patch_position_hotspot_check_response(client, hotspot_for_patch):
    """
    update a hotspot position by title and check the update
    """
    title = hotspot_for_patch["title"]
    position = {"latitude": 51, "longitude": 51}

    response = patch(title, client, position=position)

    assert response.get_json()["position"] == position, \
        "response position({}) not equals to position({})".format(response.get_json()["position"], position)

def test_patch_position_hotspot_404(client):
    """
    try to update a hotspot by a invalid title and get a 404 status code response
    """
    title = "Impossible title for update a latitude and longitude"
    position = {"latitude": 0, "longitude": 0}

    response = patch(title, client, position=position)

    assert response.status_code == 404, \
        "status code not equals to 404. {} instead.".format(response.status_code)
