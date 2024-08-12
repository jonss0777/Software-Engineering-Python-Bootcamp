import openmeteo_requests

import requests_cache
import pandas as pd

from retry_requests import retry

def getWeatherData(coordinates):
    
    # Setup the Open-Meteo API client with cache and retry on error 
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries= 5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": coordinates["lat"],
	"longitude": coordinates["lng"],
	"hourly": ["temperature_2m", "relative_humidity_2m"],
    "temperature_unit": "fahrenheit",
	"forecast_days": 1
    }

    responses = openmeteo.weather_api(url, params=params)
    
    # Process hourly data. The order of variables needs to be the same as requested.
    response = responses[0]
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"  
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
    
    print("temperature: ", hourly_data["temperature_2m"][0])
    print("relative humidity: ", hourly_data["relative_humidity_2m"][0])
    return [hourly_data["temperature_2m"][0], hourly_data["relative_humidity_2m"][0]]
