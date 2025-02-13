import requests
from config_weather import API_KEY


async def api_get_weather(city):
    """
    this function returns the weather information for the given city
    """
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()