from fastapi import APIRouter, responses

from schema.flight import Flight
from service.flight import *


flightRouter = APIRouter(tags=['flight'])

@flightRouter.post('/flight')
async def create_flight(id : str, lat : float, lng : float):
    db_create_flight(id=id, lat=lat, lng=lng)
    return responses.JSONResponse(status_code=200, content={"message" : "secesss create flight data"})

@flightRouter.get('/flight', response_model=list[Flight])
async def read_flight():
    res = db_read_flight()
    if (len(res)):
        return res
    return [Flight(flight_id = "dummy_flight", latitude=37.566515, longitude = 126.977969)]

@flightRouter.patch('/flight', )
async def update_flight(id : str, new_lat : float, new_lng : float):
    db_update_flight_position(flight_id=id, new_lat=new_lat, new_lng=new_lng)
    return responses.JSONResponse(status_code=200, content={"message" : "secesss flight DB update"})

@flightRouter.delete('/flight')
async def delete_flight(id : str):
    db_delete_flight(flight_id=id)
    return responses.JSONResponse(status_code=200, content={"message" : "secesss delete flight data"})