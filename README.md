# Weathery API

A weather forecast API built with FastAPI that provides weather data and predictions.

## Features

- RESTful API endpoints for weather data
- Weather forecast predictions using weatherAPI
- Database integration with MySQL
- Data validation using Pydantic
- Database migrations with Alembic

## Tech Stack

- FastAPI -  Python web API framework
- SQLAlchemy - SQL toolkit and ORM
- Pydantic - Data validation
- MySQL - Database
- Alembic - Database migrations

## Prerequisites
- Python 3.13+
- MySQL
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/faizakmalz/weathery-api.git
cd weathery-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn pydantic databases mysql-connector-python sqlalchemy alembic requests scikit-learn pytest pymysql python-dotenv
```

4. Copy the `.env.copy` to your .env file in the root directory and add your configuration:
```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/weathery
API_KEY=your_weather_api_key
# add Database configuration for mysql if needed
```

5. Run database migrations:
```bash
alembic upgrade head
```
If something fails, just delete the migration and init it again with :
```bash
alembic revision -m "Recreate Migration"
```

## Running the Application

1. Start the development server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`
3. Access the API documentation at `http://localhost:8000/docs`

## Setup Test
I also add a test_db.py file to test, just run it if you need to make sure the api works perfectly
