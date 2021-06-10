from mongoengine.errors import NotUniqueError

from mymba_feeder.models import HotspotModel


class HotspotManager:

    def __init__(self):
        self.hotspot = HotspotModel()

    def insert(self, data):
        try:
            self.hotspot.title = data["title"]
            self.hotspot.description = data["description"]
            self.hotspot.sponsors = data["sponsors"]
            self.hotspot.contributors = data["contributors"]
            self.hotspot.position = data["position"]
            self.hotspot.save()

            return self.hotspot
        except NotUniqueError:
            raise NotUniqueError("{} already exists".format(self.hotspot.title))

    @staticmethod
    def get_by_title(title):
        return HotspotModel.objects.get_or_404(title=title)
    
    def update(self, title, data):
        hotspot = self.get_by_title(title)

        if "title" in data:
            hotspot.title = data["title"]
        if "description" in data:
            hotspot.description = data["description"]
        if "sponsors" in data and isinstance(data["sponsors"], list):
            hotspot.sponsors = data["sponsors"]
        if "contributors" in data and isinstance(data["contributors"], list):
            hotspot.contributors = data["contributors"]
        if "position" in data and isinstance(data["position"], dict):
            hotspot.position = data["position"]

        hotspot.save()

        return hotspot
    
    def delete(self, title):
        return self.get_by_title(title).delete()