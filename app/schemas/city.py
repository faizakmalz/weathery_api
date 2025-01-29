from pydantic import BaseModel

class CityBase(BaseModel):
    name: str
    country: str

class CityCreate(CityBase):
    pass

class CityResponse(CityBase):
    id: int

class Config:
    from_attributes = True