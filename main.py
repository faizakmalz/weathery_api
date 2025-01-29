from fastapi import FastAPI
from app.api.api import api_router
from app.core.database import engine
from app.models import Base  # Import Base from models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather App API!"}