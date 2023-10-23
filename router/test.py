from fastapi import APIRouter

from schema.test import Test


testRouter = APIRouter(tags=['test'])

@testRouter.post('/test')
async def create_test():
    return 

@testRouter.get('/test', response_model=list[Test])
async def read_test():
    return Test.test_value

@testRouter.patch('/test')
async def update_test():
    return 

@testRouter.delete('/test')
async def delete_test():
    return   