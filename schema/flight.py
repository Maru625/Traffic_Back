from pydantic import BaseModel
from typing import Optional

class Flight(BaseModel):
    id : str
    altitude : float
    latitude : float
    longitude : float

