import urllib.parse
from googleGeolocation import location
import aiohttp 


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

  
    def setTime(self, time):
        self._time = time

   
    def setTemperature(self, temperature):
        self._temperature = temperature


    def setHumidity(self, humidity):
        self._humidity = humidity



class OpenMeteoWeatherAPI(AbstractWeatherAPI):  
    def __init__(self):
        super().__init__()


    async def getData(self, address, zipcode, city, country):
        response = await location(address, zipcode, city, country)
        latitude =  response["lat"]
        longitude = response["lng"]

        print("lat: ", latitude)
        print("lng: ", longitude)

        host = "https://api.open-meteo.com"
        endpoint = "/v1/forecast"

        params =  urllib.parse.urlencode({
	        "latitude":latitude,
	        "longitude": longitude,
	        "hourly": ",".join( ["temperature_2m", "relative_humidity_2m"])
        })

        full_url =f"{host}{endpoint}?{params}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(full_url) as response:
                    print("Status:", response.status)
                    if response.status == 200:
                        json_response = await response.json()
                     
                        # response has to follow a specific stucture 
                        # {
                        #  time : []
                        #  temperature : []
                        #  humidity : []
                        #}

                        self.setTime(json_response["hourly"]["time"])
                        self.setTemperature(json_response["hourly"]["temperature_2m"])
                        self.setHumidity(json_response["hourly"]["relative_humidity_2m"])

                    else:
                        print("There was an error while fetching data from the open api")
                       
                       

        except Exception as e:
            print(f"Unexpected error: {e}")
           

