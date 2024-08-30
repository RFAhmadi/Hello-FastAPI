# THANKS TO https://youtu.be/J5Z7rhrSVgc?si=Stwg38_ge9FL8Z7D
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Weather
from api import api_get_weather

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World AND Welcome to my first API project; the weather fastapi"}



@app.get("/weather/")
async def get_weather(city: str = None, is_json: bool = False):
    response = await api_get_weather(city)
    weather = Weather(**response)

    if is_json:
        return{
            "weather": weather
        }

    return HTMLResponse(content=f"<h1>Weather for {weather.location.name}/{weather.location.country}<br/></h1><h2>temperature is {weather.current.temp_c} Celsius</h2> ")