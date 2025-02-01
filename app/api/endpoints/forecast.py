from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.forecast import ForecastRequest, ForecastResponse
from app.crud.forecast import create_forecast, get_forecasts_by_city
from app.core.database import get_db
from app.services.weather import get_weather, get_forecast


router = APIRouter()

@router.post("/", response_model=ForecastResponse)
def create_new_forecast(request: ForecastRequest, db: Session = Depends(get_db)):
    return create_forecast(db=db, city_id=request.city_id)

@router.get("/{city_id}", response_model=list[ForecastResponse])
def read_forecasts(city_id: int, db: Session = Depends(get_db)):
    return get_forecasts_by_city(db, city_id)

@router.get("/weather/{city_name}")
def fetch_weather(city_name: str):
    weather_data = get_weather(city_name)
    
    if "error" in weather_data:
        raise HTTPException(status_code=400, detail=weather_data["error"])
    
    return weather_data

@router.get('/5days-forecast/{city_name}')
def fetch_forecast(city_name: str):
    forecast_data = get_forecast(city_name)

    if "error" in forecast_data:
        raise HTTPException(status_code=400, detail=forecast_data["error"])
    
    return forecast_data
