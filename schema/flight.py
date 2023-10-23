from pydantic import BaseModel

class Flight(BaseModel):
    flight_id : str
    latitude : float
    longitude : float