from fastapi import APIRouter
from db.client import redis_client
import os

router = APIRouter(prefix="/weather",
                   tags=["weather"], 
                   responses={404: {"message": "NOT FOUND"}})

cache = {}

EXPIRATION_TIME = os.getenv("CACHE_EXPIRATION_TIME", 3600), # 1h in ms

@router.get("/test/")
async def weather(location: str):
    return {"location": location, "weather": "Sunny and wonderful"}

@router.get("")
async def weather(location: str):
    weatherData = redis_client.get(location)

    if weatherData:
        return {"location": location, "weather": weatherData}
    
    print("CACHE NOT FOUND: Weather data for " + location + " not found in Redis cache")

    # call weather API
    weatherData = "Sunny and wonderful"

    redis_client.set(location, weatherData, ex=3600)

    return {"location": location, "weather": weatherData}