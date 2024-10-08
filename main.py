import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from routers import weather

load_dotenv()

app = FastAPI()

# Routers
app.include_router(weather.router)

@app.get("/")
def read_root():
    return {"owner": "Aperture Science"}

# init server -> uvicorn main:app --reload
# Url local: http://127.0.0.1:8000

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)