from dataclasses import dataclass
from typing import Optional

@dataclass
class Flight_DB:
    id : str
    altitude : float
    latitude : float
    longitude : float
    phase : str | None = None
    time : str | None = None
    distance : str | None = None

    def change_flight_position(self, altitude:float, latitude:float, longitude:float, phase : str | None = None
                               ,time: str | None = None, distance : str | None = None):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.phase = phase
        self.time = time
        self.distance = distance