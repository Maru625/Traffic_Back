from schema.flight import Flight
from model.flight import Flight_DB
from database.index import DB_flights


def db_create_flight(id : str, lat : float, lng : float):
    DB_flights.append(Flight_DB(id=id, latitude=lat, longitude=lng))
    

def db_read_flight():
    res : list[Flight] = []
    for flight in DB_flights:
        res.append(Flight(flight_id=flight.id, latitude=flight.latitude, longitude=flight.longitude))
    return res

def db_update_flight_position(flight_id : str, new_lat : float, new_lng : float):
    for flight in DB_flights:
        if flight.id == flight_id:
            flight.change_flight_position(new_lat,new_lng)
            break

def db_delete_flight(flight_id : str):
    for i, flight in enumerate(DB_flights):
        if flight.id == flight_id:
            del DB_flights[i]
            break