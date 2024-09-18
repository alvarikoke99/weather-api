import os, uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
#WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/")
def read_item(location: str):
    return {"location": location, "weather": "Sunny and wonderful", "degrees": 33}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)