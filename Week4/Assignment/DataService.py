# data service will contain 
# x values
# y values
# labels
class DataService():
    # data will be the data returned by our api call
    # benefits of this approach is decoupling and testing
    def __init__(self, api):
        self.time = None
        self.temperature = None
        self.humidity = None

    def getTime(self):
        return self.time

    def getTemperature(self): 
        return self.temperature
    
    def getHumidity(self):
        return self.humidity