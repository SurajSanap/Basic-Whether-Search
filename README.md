
# Weather Information Retrieval

This Python script retrieves the current weather information for a specified city using the OpenWeatherMap API. It prompts the user to enter a city name and displays the weather details such as temperature, humidity, wind speed, and more.

## Requirements

- Python 3.x
- requests library (install using `pip install requests`)

## Getting Started

1. Clone the repository or download the script `weather.py` to your local machine.

2. Sign up for an account at [OpenWeatherMap](https://openweathermap.org/) to obtain an API key.

3. Replace `'YOUR_API_KEY'` in the script with your actual OpenWeatherMap API key.

4. Run the script using the command `python weather.py`.

5. Enter the name of the city for which you want to retrieve weather information.

## Example Usage

```
$ python weather.py
Enter a city name: London
{
    "coord": {
        "lon": -0.1257,
        "lat": 51.5085
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 18.63,
        "feels_like": 18.7,
        "temp_min": 18.3,
        "temp_max": 19.2,
        "pressure": 1018,
        "humidity": 70
    },
    "visibility": 10000,
    "wind": {
        "speed": 2.68,
        "deg": 297,
        "gust": 3.19
    },
    "clouds": {
        "all": 75
    },
    "dt": 1668056993,
    "sys": {
        "type": 2,
        "id": 2035973,
        "country": "GB",
        "sunrise": 1668024160,
        "sunset": 1668080237
    },
    "timezone": 3600,
    "id": 2643743,
    "name": "London",
    "cod": 200
}
```

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use this code for your own projects.

Please note that the usage of the OpenWeatherMap API is subject to their terms and conditions.

For more information, refer to the official [OpenWeatherMap API documentation](https://openweathermap.org/api).
