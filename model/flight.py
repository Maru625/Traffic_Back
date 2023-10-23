from dataclasses import dataclass

@dataclass
class Flight_DB:
    id : str
    latitude : float
    longitude : float

    def change_flight_position(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude