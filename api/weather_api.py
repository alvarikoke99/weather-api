import os, requests

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")

def makeWeatherApiRequest(location: str) -> dict[str, str]:
    requestUrl = WEATHER_API_URL + "/" + location
    weatherData = {}

    response = requests.get(url=requestUrl, params={"key": WEATHER_API_KEY})

    try:
        response.raise_for_status()
        currentDayData =  response.json()["days"][0]
        weatherData = {
            "location": location,
            "conditions": currentDayData["conditions"],
            "tempmax": fahrenheitToCelsius(currentDayData["tempmax"]),
            "tempmin": fahrenheitToCelsius(currentDayData["tempmin"]),
            "temp": fahrenheitToCelsius(currentDayData["temp"]),
            "humidity": 83.7,
            "precipprob": 6.5
        }
        return weatherData
    except requests.exceptions.HTTPError as err:
        print(f"ERROR sending request to 3rd party weather API {response.status_code}: {err}")
        return {"error_code": response.status_code, "text": response.text}
    except:
        print("EXCEPTION sending request to 3rd party weather API")
        return {"error_code": 502, "text": "Internal exception consulting weather data"}

    

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)