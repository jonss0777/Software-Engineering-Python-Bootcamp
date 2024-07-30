import http.client
import urllib.parse


class WeatherAPI():
    def __init__(self):
        self.data = None

    def fetchData(self,host = "api.open-meteo.com", endpoint = "/v1/forecast", params =  urllib.parse.urlencode({
	        "latitude": 40.7143,
	        "longitude": -74.006,
	        "hourly": ["temperature_2m","relative_humidity_2m"]
        })):


        conn = http.client.HTTPSConnection(host)
        conn.request("GET", f"{endpoint}?{params}",  headers={"Host": host})
        response = conn.getresponse()
        print(response.status, response.reason)
        while chunk := response.read(200):
            continue
            #print(repr(chunk))
        
        self.data = chunk

    def getData(self):
        return self.data







