from .models import HotspotModel


class DataManager:

    def __init__(self):
        pass

    def insert(self, data):
        hotspot = HotspotModel()

        hotspot.title = data["title"]
        hotspot.description = data["description"]
        hotspot.sponsors = data["sponsors"]
        hotspot.contributors = data["contributors"]
        hotspot.position = data["position"]
        hotspot.save()

        return hotspot
    