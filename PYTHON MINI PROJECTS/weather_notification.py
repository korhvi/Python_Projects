import requests
from config import API_KEY

city = input("Tell me a city: ")
try:
  response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
  response.raise_for_status()
  data = response.json()
except requests.exceptions.HTTPError as err:
  print(f"Error: {err}")
  exit()


weather_temp = data['main']['temp']
weather = data['weather'][0]['main']


if (weather_temp < 0):
  print("It's freezing! You have to wear more clothes!")
else:
  print(f"Enjoy the weather! It's {weather_temp}°C")

if (weather == "Rain"):
  print("It's raining! Take your umbrella with you!")

elif(weather == "Clear"):
  print("It's sunny! Take your sunglasses with you!")
