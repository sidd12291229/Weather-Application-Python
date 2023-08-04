import tkinter as tk
import requests

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temp_c"]
        weather_description = data["current"]["condition"]["text"]
        return f"Weather in {city}: {temperature}°C, {weather_description}"
    else:
        return "Enter a valid city name."

def show_weather():
    api_key = "9d2c42f4f3644470b90185844233006"
    city = city_entry.get()
    weather_info = get_weather(api_key, city)
    weather_label.config(text=weather_info)

app = tk.Tk()
app.title("Weather App")
app.geometry("400x200")  # Adjust the size as per your requirements

city_label = tk.Label(app, text="City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack()

weather_label = tk.Label(app, text="", wraplength=350)  # To wrap long weather info text
weather_label.pack()

app.mainloop()
