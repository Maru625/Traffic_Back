from pydantic import BaseModel

class Flight(BaseModel):
    flight_name : str
    latitude : float
    longitude : float