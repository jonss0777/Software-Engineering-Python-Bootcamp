import urllib.parse
import aiohttp 

from dotenv import load_dotenv
import os

load_dotenv()

async def location(address, zipcode, city, country):
  
    host = "https://maps.googleapis.com"
    endpoint = "/maps/api/geocode/json"

    key = os.getenv("GOOGLEMAPSAPIKEY")

    full_address = f"{address} {zipcode} {city} {country}"

    params = urllib.parse.urlencode({
        "key": f"{key}",
        "address": full_address
    })
    
    full_url = host + f"{endpoint}?{params}"

    try:

        async with aiohttp.ClientSession() as session:
            async with session.get("" + full_url) as response:
                if response.status == 200:
                    json_response = await response.json()

                    # response structure:
                    # r = {
                    # lat: FLOAT
                    # lgn: FLOAT
                    #}

                    return json_response["results"][0]["geometry"]["location"]
                
                else:
                    print("There was an error")
                    return {"lat": 0.0 , "lng":0.0}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


