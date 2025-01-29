from app.core.database import Base
from app.models.city import City
from app.models.forecast import Forecast

# This will ensure models are only imported once
__all__ = ['City', 'Forecast']