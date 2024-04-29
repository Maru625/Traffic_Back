from fastapi import APIRouter, responses
import os

from schema.flight import Flight
from service.flight_path_gen import *


flightRouter = APIRouter(tags=['flight'])

@flightRouter.post('/flight')
async def create_flight(flight : Flight):
    res = db_create_flight(flight.id, flight.altitude, flight.latitude, flight.longitude)
    if res:
        return responses.JSONResponse(status_code=201, content={"message" : "Secesss create flight data"})
    return responses.JSONResponse(status_code=409, content={"message" : "The ID you entered is duplicate."})

@flightRouter.get('/flight')
async def read_flight():
    res : list[Flight] = db_read_flight()
    if (len(res)):
        return res
    return responses.JSONResponse(status_code=210, content={"message" : "Flight is None"})


@flightRouter.get("/flight/files")
async def get_file():
    """파일을 가져옵니다."""
    res = db_read_all_flight()
    return res


@flightRouter.patch('/flight')
async def update_flight(flight : Flight):
    res = db_update_flight_position(flight.id, flight.altitude, flight.latitude, flight.longitude)
    if res:
        return responses.JSONResponse(status_code=200, content={"message" : "secesss flight DB update"})
    return responses.JSONResponse(status_code=404, content={"message" : "Flight information with the same ID entered cannot be found."})

@flightRouter.delete('/flight')
async def delete_flight(id : str):
    res = db_delete_flight(id=id)
    if res :
        return responses.JSONResponse(status_code=200, content={"message" : "secesss delete flight data"})
    return responses.JSONResponse(status_code=404, content={"message" : "Flight information with the same ID entered cannot be found."})

@flightRouter.delete('/flight/all')
async def delete_all_flight():
    db_delete_all_flight()
    return responses.JSONResponse(status_code=200, content={"message" : "secesss delete flight data"})

