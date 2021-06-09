testing_title = "title_test_post"

def test_post_hotspot(client, faker, fake_dict_latlng):
    """
    make a post to /hotspot inserting fake data
    """
    title = testing_title
    description = "testing post to hotspot"
    sponsors = [faker.name(), faker.name(), faker.name()]
    contributors = [faker.name(), "Test Community"]
    position = fake_dict_latlng

    response = client.post("/hotspot/", json=dict(
        title=title,
        description=description,
        sponsors=sponsors,
        contributors=contributors,
        position=position
    ))

    assert response.status_code == 201, \
        "status code not equals to 201(created)"
    
    data = response.json

    assert "title" in data, "title not in response"
    assert "description" in data, "description not in response"
    assert "sponsors" in data, "sponsors not in response"
    assert "contributors" in data, "contributors not in response"
    assert "position" in data, "position not in response"

    assert data["title"] == title
    assert data["description"] == description, "description not equals to {}".format(description)
    assert data["sponsors"] == sponsors, "sponsors not equals to {}".format(sponsors)
    assert data["contributors"] == contributors, "contributors not equals to {}".format(contributors)
    assert data["position"] == position, "position not equals to {}".format(position)

def test_post_hotspot_duplicated_title_409(client, faker, fake_dict_latlng):
    """
    testing post for a duplicated hotspot 
    """
    title = testing_title
    description = "testing a duplicated title for post"
    sponsors = [faker.name(), faker.name()]
    contributors = [faker.name(), faker.name()]
    position = fake_dict_latlng

    response = client.post("/hotspot/", json=dict(
        title=title,
        description=description,
        sponsors=sponsors,
        contributors=contributors,
        position=position
    ))

    assert response.status_code == 409, \
        "response status code not equals to 409. {} instead.".format(response.status_code)
