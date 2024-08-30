from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Weather
from api import api_get_weather

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World AND Welcome to my first API project; the weather fastapi"}



@app.get("/weather/")
async def get_weather(city: str = None):
    response = await api_get_weather(city)
    weather = Weather(**response)
    # return {
    #     "weather": weather
    #     # "weather": {
    #     #     "city": city
    #     # }
    # }

    return HTMLResponse(content=f"<h1>Weather for {weather.location.name}/{weather.location.country}<br/></h1><h2>temperature is {weather.current.temp_c} Celsius</h2> ")