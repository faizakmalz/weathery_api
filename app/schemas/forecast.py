from pydantic import BaseModel
from datetime import datetime
from typing import List

class ForecastBase(BaseModel):
    city_id: int
    date: datetime
    weather_description: List[str]
    temperature: float

    class Config:
        from_attributes = True

class ForecastCreate(ForecastBase):
    pass

class ForecastRequest(BaseModel):
    city_id: int

class ForecastResponse(ForecastBase):
    id: int

