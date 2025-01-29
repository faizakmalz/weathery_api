from app.core.database import engine
from sqlalchemy import text
from app.core.config import settings
from app.models import City, Forecast  # Import from models package
from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app instance

client = TestClient(app)  # Initialize TestClient with the app

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Database connection successful!")
            return True
    except Exception as e:
        print(f"Database connection failed: {str(e)}")
        return False

def test_models():
    try:
        # Check if relationship is properly set up
        city = City()
        forecast = Forecast()
        # Check if the relationship attributes exist
        assert hasattr(city, 'forecasts')
        assert hasattr(forecast, 'city')
        print("Model relationships are correctly set up!")
        return True
    except Exception as e:
        print(f"Model check failed: {str(e)}")
        return False

def test_config():
    print("Environment Settings:")
    print(f"Database URL: {settings.DATABASE_URL}")
    print(f"API Key available: {'Yes' if settings.WEATHERSTACK_API_KEY else 'No'}")
    print(f"Environment: {settings.APP_ENV}")
    print(f"Debug mode: {settings.DEBUG}")

def test_routes():
    # Test root endpoint
    response = client.get("/")
    print(f"Root endpoint status: {response.status_code}")
    
    # Test cities endpoint
    response = client.get("/api/v1/cities/")
    print(f"Cities endpoint status: {response.status_code}")
    
    # Test forecasts endpoint
    response = client.get("/api/v1/forecasts/1")
    print(f"Forecasts endpoint status: {response.status_code}")

if __name__ == "__main__":
    test_connection()
    test_config()
    test_models()
    test_routes()
