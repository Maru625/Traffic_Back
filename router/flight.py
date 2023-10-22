from fastapi import APIRouter


flightRouter = APIRouter(tags=['flight'])

@flightRouter.post('/flight')
async def create_flight():
    return 

@flightRouter.get('/flight')
async def read_flight():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

@flightRouter.patch('/flight')
async def update_flight():
    return 

@flightRouter.delete('/flight')
async def delete_flight():
    return   