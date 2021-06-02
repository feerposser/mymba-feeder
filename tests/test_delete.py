
def test_delete_by_title_200(client, create_hotspot):
    """
    create a hotspot with a title and try to delete it
    http response must be 200
    """
    title = "test_delete_by_title_200"
    create_hotspot(title)

    response = client.delete("/hotspot/{}/".format(title))

    assert response.status_code == 200, "response status code not equals to 200"

def test_delete_by_title_404(client):
    """
    test a http delete to remove a nonexistent resource
    """
    response = client.delete("/hotspot/nonexistent resource/")

    assert response.status_code == 404, "response status code not equals to 404"

def test_delete_all_hospots_not_allowed_405(client):
    """
    try to delete all hotspots
    """
    response = client.delete("/hotspot/")

    assert response.status_code == 405, "http response not equals to 405"
