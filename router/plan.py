import time
from fastapi import APIRouter, responses, File, UploadFile, HTTPException

# from schema.plan import plan
from service.plan import *


planRouter = APIRouter(tags=['plan'])

@planRouter.post('/plan')
async def create_plan(files : list[UploadFile] = File(...)):
    try:
        for file in files:
            contents = await file.read()
            # 여기에서 contents를 원하는 대로 처리
            # 파일 저장, 데이터베이스에 저장 등의 작업을 수행
            print(f"Received file: {file.filename}, size: {len(contents)} bytes")
            generate_trajectory(file.filename)
        print("process done")
        return {"message": "Ready to generate UAMs positions"}
    except HTTPException as e:
        print(f"Exception Detail: {e.detail}")
        raise e

@planRouter.get('/plan/generate/flights')
async def start_simulator(speed : float):
    await generate_positions(speed)
    return {'message' : ""}