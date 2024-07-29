import googlemaps

from dotenv import load_dotenv
import os
load_dotenv()

def get_latitude_longitude(city, country):  
    
    gmaps = googlemaps.Client(os.getenv("GOOGLEMAPSAPIKEY"))
    geocode_result = gmaps.geocode((city.get() + " " + country.get()))
    print(geocode_result)

    return geocode_result[0]["geometry"]["location"]


