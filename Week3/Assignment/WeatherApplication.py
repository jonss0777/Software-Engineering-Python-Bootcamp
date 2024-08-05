
class WeatherApplication:

    def __init__(self):
        self.data = [] # instance variable unique to each instance
        self.humidity = None
        self.city = None
        self.temperature = None

    def fetchData(self,city):
        pass

    def getTemperature(self):
        return self.data

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getHumidity(self):
        return self.data
    


