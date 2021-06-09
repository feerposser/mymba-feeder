
def put(resource, client, **kwargs):
    data = {}
    for key, value in kwargs.items():
        data.update({key: value})

    return client.put("/hotspot/{}/".format(resource), json=data)

def test_put_hotspot_200(client, hotspot_for_patch_put, faker):
    """
    test a http put
    """

    title = hotspot_for_patch_put["title"]

    response = put(
        title, client,
        description="new description for put test",
        sponsors=[faker.name(), faker.name()],
        contributors=[faker.name(), faker.name(), faker.name()],
        position={"latitude": 10, "longitude": 10})
    
    assert response.status_code == 200, \
        "response status code not equals to 200. {} instead.".format(response.status_code)

def test_put_hotspot_check_response(client, hotspot_for_patch_put, faker):
    """
    make an update to /hotspot using the last data in response
    """
    title = hotspot_for_patch_put["title"]
    description = "new description for check response"
    sponsors = [faker.name()]
    contributors = [faker.name(), faker.name(), faker.name()]
    position = {"latitude": 12, "longitude": 32}

    response = put(
        title, client,
        description=description,
        sponsors=sponsors,
        contributors=contributors,
        position=position)

    response = response.get_json()

    assert response["title"] == title, \
        "response title({}) not equals to title({})".format(response["title"], title)
    assert response["description"] == description, \
        "response description({}) not equals to new descriptio({})".format(response["description"], description)
    assert response["sponsors"] == sponsors, \
        "response sponsors ({}) not equals to new sponsors({})".format(response["sponsors"], sponsors)
    assert response["contributors"] == contributors, \
        "response contributors({}) not equals to new contributors({})".format(response["contributors"], contributors)
    assert response["position"] == position, \
        "response position({}) not equals to new position({})".format(response["position"], position)

def test_put_hotspot_duplicated_title_405(client, faker, hotspot_for_patch_put):
    """
    make a put http with a new duplicated title
    """
    title = client.get("/hotspot/").get_json()[0]["title"]

    duplicated_title = hotspot_for_patch_put["title"]
    description = "new description for duplicated title"
    sponsors = [faker.name()]
    contributors = [faker.name(), faker.name(), faker.name()]
    position = {"latitude": 33, "longitude": 42}

    response = put(
        title, client,
        title=duplicated_title,
        description=description,
        sponsors=sponsors,
        contributors=contributors,
        position=position)
    
    assert response.status_code == 409, \
        "response status code not equals to 409. {} instead.".format(response.status_code)

def test_put_hotspot_title_not_found_404(client, faker):
    """
    try to put a nonexistence resource
    """
    title = "Demostenes, the first avenger"
    description = "new description for nonexistence resource"
    sponsors = [faker.name()]
    contributors = [faker.name(), faker.name(), faker.name()]
    position = {"latitude": 33, "longitude": 42}

    response = put(
        title, client,
        title=title,
        description=description,
        sponsors=sponsors,
        contributors=contributors,
        position=position)

    assert response.status_code == 404, \
        "response status code not equals to 404. {} instead.".format(response.status_code)
