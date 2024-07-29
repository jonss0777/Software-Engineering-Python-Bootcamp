from testingMaps import get_latitude_longitude
from WeatherApi import getWeatherData
import tkinter 

def getData(city, country):
    result = get_latitude_longitude(city,country)
    print("result: ", result)
    data = getWeatherData(result)
    print("data: ", data)

    result_temperature.set(f"Temperature: {data[0]} F")
    result_humidity.set(f"Relative Humidity: {data[1]}")




root = tkinter.Tk()
root.title("Weather App")
root.geometry("400x400")
result_temperature = tkinter.StringVar() 
result_humidity = tkinter.StringVar()

country = tkinter.StringVar()
city = tkinter.StringVar()
app_name = tkinter.Label(root, text="Weather App")

country_label = tkinter.Label(root, text="Country")
country_input = tkinter.Entry(root, textvariable=country)
city_label = tkinter.Label(root, text="City")
city_input = tkinter.Entry(root, textvariable=city)

button = tkinter.Button(root, text='Search', width=10, command=lambda:getData(city, country))

result_humidity_label = tkinter.Label(root, textvariable=result_humidity)
result_temperature_label = tkinter.Label(root, textvariable=result_temperature)
app_name.pack()

country_label.pack()
country_input.pack()
city_label.pack()
city_input.pack()

button.pack()

result_humidity_label.pack()
result_temperature_label.pack()

root.mainloop()