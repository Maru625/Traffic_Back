from pydantic import BaseModel
from typing import Optional

class Flight(BaseModel):
    id : str
    altitude : float
    latitude : float
    longitude : float
    phase : str | None = None
    time : str | None = None
    distance : str | None = None

