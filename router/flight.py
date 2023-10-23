from fastapi import APIRouter

from model.flight import Flight


flightRouter = APIRouter(tags=['flight'])

@flightRouter.post('/flight')
async def create_flight():
    return 

@flightRouter.get('/flight', response_model=list[Flight])
async def read_flight():
    return [
        {
            "flight_name" : "test1", 
            "latitude" :37.566515 + 0.001,
            "longitude" : 126.977969 + 0.001 ,
        },
        {
            "flight_name" : "test2", 
            "latitude" :37.566515 - 0.001,
            "longitude" : 126.977969 - 0.001 ,
        }
    ]

@flightRouter.patch('/flight')
async def update_flight():
    return 

@flightRouter.delete('/flight')
async def delete_flight():
    return   