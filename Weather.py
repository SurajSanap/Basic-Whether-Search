import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '4e8d8429f6abf89433c7c5763038a20f'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

city_name = input('Enter a city name: ')
weather_data = get_weather(city_name)
print(weather_data)
