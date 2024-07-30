import http.client
import urllib.parse

from dotenv import load_dotenv
import os

load_dotenv()


host = "maps.googleapis.com"
endpoint = "/maps/api/geocode/json"
headers = {"Content-type": "application/x-www-form-urlencode"}

key = os.getenv("GOOGLEMAPSAPIKEY")

params = urllib.parse.urlencode({
    "key": f"{key}",
    "address": "24%20Sussex%20Drive%20Ottawa%20ON"
})



conn = http.client.HTTPSConnection(host)
conn.request("POST", f"{endpoint}?{params}", headers = {"Host":host})
response = conn.getresponse()
print(response.status, response.reason)

while chunk := response.read(200):
    print(repr(chunk))



