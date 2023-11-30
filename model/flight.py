from dataclasses import dataclass, field
from typing import List 

@dataclass
class Flight_DB:
    id : str
    altitude : List[float] = field(default_factory=list)
    latitude : List[float] = field(default_factory=list)
    longitude : List[float] = field(default_factory=list)

    def add_flight_position(self, altitude:float, latitude:float, longitude:float):
        self.altitude.append(altitude)
        self.latitude.append(latitude)
        self.longitude.append(longitude)

    def get_position(self, idx : int):
        return [self.altitude[idx], self.latitude[idx], self.longitude[idx]]
    
    def get_flight_data_length(self):
        return len(self.altitude)