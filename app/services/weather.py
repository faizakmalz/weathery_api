import requests
import os

WEATHERAPI_API_KEY = os.getenv("WEATHERAPI_API_KEY")
WEATHERAPI_URL = "http://api.weatherapi.com/v1"


def get_weather(city_name: str):
    url = f"{WEATHERAPI_URL}/current.json?key={WEATHERAPI_API_KEY}&q={city_name}&aqi=no"
    response = requests.get(url)
    data = response.json()
    print('WeatherAPI API hitted', data)

    if "error" in data:
        return {"error": data["error"]["message"]}

    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temp_c"], 
        "weather_descriptions": [data["current"]["condition"]["text"]], 
        "wind_speed": data["current"]["wind_kph"],
        "humidity": data["current"]["humidity"]
    }

def get_forecast(city_name: str):

    url = f"{WEATHERAPI_URL}/forecast.json?key={WEATHERAPI_API_KEY}&q={city_name}&days=5&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 200:
        data =  response.json()
        forecast_days = data.get("forecast", {}).get("forecastday", [])
    
        filtered_forecast = [
            {
                "date": day["date"],
                "condition": day["day"]["condition"]["text"],
                "avg_temp_c": day["day"]["avgtemp_c"],
                "wind_kph": day["day"]["maxwind_kph"],
                "humidity": day["day"]["avghumidity"]
            }
            for day in forecast_days
        ]

        return filtered_forecast

    else:
        return {"error": f"Failed to fetch weather data. Status Code: {response.status_code}"}
