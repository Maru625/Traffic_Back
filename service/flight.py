from schema.flight import Flight as Flight_Schema
from model.flight import Flight_DB
from database.index import DB_flights


def db_create_flight(id : str, altitude : float , lat : float, lng : float):
    for flight in DB_flights:
        if flight.id == id:
            return False
    DB_flights.append(Flight_DB(id, altitude, lat, lng))
    return True
    

def db_read_flight():
    res : list[Flight_Schema] = []
    for flight in DB_flights:
        res.append(Flight_Schema(id=flight.id, altitude=flight.altitude[-1],
                                 latitude= flight.latitude[-1], 
                                 longitude= flight.longitude[-1]))
    return res

def db_read_all_flight():
    return DB_flights

def db_update_flight_position(id : str, altitude : float , lat : float, lng : float):
    for flight in DB_flights:
        if flight.id == id:
            flight.change_flight_position(altitude, lat, lng)
            return True
    return False

def db_delete_flight(id : str):
    for i, flight in enumerate(DB_flights):
        if flight.id == id:
            del DB_flights[i]
            return True
    return False

def db_delete_all_flight():
    DB_flights.clear()