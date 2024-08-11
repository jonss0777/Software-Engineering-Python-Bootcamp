import http.client
import urllib.parse


class LongLat():

    def __init__(self):
        self.longitude = None
        self.latitude = None
        pass

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude

    def requestLngLat(self, key):


        self.latitude = ""
        self.longitude = ""