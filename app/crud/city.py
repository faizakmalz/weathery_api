from sqlalchemy.orm import Session
from app.models.city import City
from app.schemas.city import CityCreate, CityBase

def create_city(db: Session, city: CityCreate):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()

def get_cities(db: Session):
    return db.query(City).all()

def delete_city(db: Session, city_id:int):
    city = db.query(City).filter(City.id == city_id).first()
    if city:
        db.delete(city)
        db.commit()
        return city

def update_city(db: Session, city_id: int, city_data: CityBase):
    city = db.query(City).filter(City.id == city_id).first()

    city.name = city_data.name
    city.country = city_data.country

    db.commit()
    db.refresh(city)
    return city
