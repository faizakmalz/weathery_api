from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Forecast(Base):
    __tablename__ = "forecasts"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    date = Column(String(100), index=True)
    weather_description = Column(JSON)
    temperature = Column(Integer)
    city = relationship("City", back_populates="forecasts")