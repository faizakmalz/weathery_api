import requests
import os

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
WEATHERSTACK_URL = "http://api.weatherstack.com/current"

def get_weather(city_name: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city_name
    }
    response = requests.get(WEATHERSTACK_URL, params=params)
    data = response.json()
    print('weatherstack api hitted', data)

    if "error" in data:
        return {"error": data["error"]["info"]}
    
    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temperature"],
        "weather_descriptions": data["current"]["weather_descriptions"],
        "wind_speed": data["current"]["wind_speed"],
        "humidity": data["current"]["humidity"]
    }
