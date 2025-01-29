from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.city import CityCreate, CityResponse
from app.crud.city import create_city, get_cities
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=CityResponse)
def create_new_city(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db, city)

@router.get("/", response_model=list[CityResponse])
def read_cities(db: Session = Depends(get_db)):
    return get_cities(db)
