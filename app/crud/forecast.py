from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.city import City
from app.services.weather import get_weather
from app.models.forecast import Forecast
from app.schemas.forecast import ForecastCreate, ForecastResponse

def create_forecast(db: Session, city_id: int) -> ForecastResponse:
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    
    weather_data = get_weather(city.name)
    if "error" in weather_data:
        raise HTTPException(status_code=400, detail=weather_data["error"])
    
    forecast_data = ForecastCreate(
        city_id=city_id,
        date=datetime.now().strftime("%Y-%m-%d"),
        weather_description=weather_data.get("weather_descriptions", []),
        temperature=weather_data["temperature"]
    )
    
    db_forecast = Forecast(**forecast_data.model_dump())
    
    db.add(db_forecast)
    db.commit()
    db.refresh(db_forecast)
    
    return ForecastResponse.from_orm(db_forecast)

def get_forecasts_by_city(db: Session, city_id: int):
    try:
        forecasts = db.query(Forecast).filter(Forecast.city_id == city_id).all()
        for forecast in forecasts:
            try:
                print(f"Type of weather_description: {type(forecast.weather_description)}")
                print(f"Content of weather_description: {forecast.weather_description}")
            except Exception as e:
                print(f"Error accessing weather_description: {str(e)}")
        return forecasts
    except Exception as e:
        print(f"Database query error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
