from WeatherAPIs import OpenMeteoWeatherAPI


import matplotlib.pyplot as plt

import numpy as np

import asyncio



async def main():
    api = input("Choose the API: ")
    city = input("Choose a city: ")
    country = input("Choose a country: ")

    if api  == "OpenMeteo":
        r = OpenMeteoWeatherAPI()
        await r.getData("","", city, country)
       
    elif  api == "":
        pass


    xtime = np.array( r.getTime())
    ytemp = np.array( r.getTemperature())
    yhumid = np.array(r.getHumidity())

    #x = np.linspace(0, 2, 100)  # Sample data.

    plt.figure(figsize=(6, 3.7), layout='constrained')
    plt.plot(xtime, ytemp, label="temperature")
    plt.plot(xtime, yhumid, label="humidity")  

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"{city} {country} Weather Info")
    plt.legend()
    plt.show()

asyncio.run(main())
