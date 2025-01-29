from sqlalchemy.orm import Session
from app.models.city import City
from app.schemas.city import CityCreate

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
