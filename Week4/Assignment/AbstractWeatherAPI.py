from abc import ABC, abstractmethod

class AbstractWeatherAPI(ABC):

    def __init__(self):
        super().__init__()
        self._time = None
        self._temperature = None
        self._humidity = None
    # gets data from any weather api and returns the response
    @abstractmethod
    def getData(self, address, zicode, city,country):
        pass
    
    def getTime(self):
        return self._time
    
    def getTemperature(self):
        return self._temperature
        
    def getHumidity(self):
        return self._humidity

    @abstractmethod
    def setTime(self, time):
        self._time = time

    @abstractmethod
    def setTemperature(self, temperature):
        self._temperature = temperature

    @abstractmethod 
    def setHumidity(self, humidity):
        self._humidity = humidity