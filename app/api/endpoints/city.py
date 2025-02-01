from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.city import CityCreate, CityResponse, CityBase
from app.crud.city import create_city, get_cities, delete_city, update_city
from app.core.database import get_db

router = APIRouter()

@router.put("/{city_id}", response_model=CityResponse)
def update_city_route(city_id: int, city_data: CityBase, db: Session = Depends(get_db)):
    updated_city = update_city(db, city_id, city_data)
    if updated_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return updated_city

@router.post("/", response_model=CityResponse)
def create_new_city(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db, city)

@router.get("/", response_model=list[CityResponse])
def read_cities(db: Session = Depends(get_db)):
    return get_cities(db)

@router.delete("/{city_id}")
def delete_existing_city(city_id:int , db: Session = Depends(get_db)):
    return delete_city(db, city_id)
