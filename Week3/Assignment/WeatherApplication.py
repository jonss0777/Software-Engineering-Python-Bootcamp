
from WeatherApi import getData
class WeatherApplication:

    def __init__(self):
        self.data = [] # instance variable unique to each instance
        self.humidity = ""
        self.city = ""
        self.temperature = ""

    def fetchData(self,city):
        self.data = getData(city)

    def getTemperature(self):
        return self.data[0]


    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getHumidity(self):
        return self.data[1]
    


