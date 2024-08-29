from fastapi import FastAPI
from models import *

app = FastAPI()




@app.get("/")
async def index():
    return {"message": "Hello World AND Welcome to my first API project; the weather fastapi"}



@app.get("/weather/")
async def get_weather(city: str = None):
    return {
        "weather": {
            "city": city
        }
    }