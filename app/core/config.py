import os
from dotenv import load_dotenv

# Load environment variables from the `.env` file
load_dotenv()

class Settings:
    # Weatherstack API Key
    WEATHERSTACK_API_KEY: str = os.getenv("WEATHERSTACK_API_KEY")

    # Database Configuration
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "weather_app")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    
    # Generate full DATABASE_URL for SQLAlchemy
    DATABASE_URL: str = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # App Environment
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
