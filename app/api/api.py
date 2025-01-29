from fastapi import APIRouter
from app.api.endpoints import city, forecast

api_router = APIRouter()
api_router.include_router(city.router, prefix="/cities", tags=["cities"])
api_router.include_router(forecast.router, prefix="/forecasts", tags=["forecasts"])
