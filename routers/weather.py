from fastapi import APIRouter, HTTPException
from db.client import redis_client
import os
from api.weather_api import makeWeatherApiRequest

EXPIRATION_TIME = int(os.getenv("CACHE_EXPIRATION_TIME", 3600)) # 1h in ms

router = APIRouter(prefix="/weather",
                   tags=["weather"], 
                   responses={404: {"message": "NOT FOUND"}})

@router.get("")
async def weather(location: str):
    weatherData = redis_client.hgetall(location)

    if weatherData:
        return weatherData
    
    print("CACHE NOT FOUND: Weather data for " + location + " not found in Redis cache")

    # Call weather API
    weatherData = makeWeatherApiRequest(location)
    if "error_code" in weatherData:
        raise HTTPException(status_code=weatherData["error_code"], detail=weatherData["text"])

    # Update cache
    try:
        pipe = redis_client.pipeline()
        pipe.hset(location, mapping=weatherData)
        pipe.expire(location, EXPIRATION_TIME)
        result = pipe.execute()
        '''if not result[0]:
            print("ERROR setting weather data in cache")
        if not result[1]:
            print("ERROR setting weather data expiration in cache")'''
    except:
        print("ERROR updating Redis cache")

    return weatherData