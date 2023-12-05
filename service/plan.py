import asyncio
import time
import random

from model.flight import Flight_DB as Flight_Model
from database.index import DB_flights as DB_FLIGHTS

tmp_flights_list : list[Flight_Model] = [] # 생성한 경로 임시 저장 공간

def generate_trajectory(sample_id :str): # 경로 생성 예시 코드
    global tmp_flights_list
    lat = 37.543735026505246
    lng = 127.07770397976434
    count = 0

    tmp_flights_list.append(Flight_Model(id=sample_id))

    multiple = random.randrange(1,5)

    while(1):
        lat += 0.0001 * multiple
        lng += 0.0001 * multiple
        
        for flight in tmp_flights_list:
            if flight.id == sample_id:
                flight.add_flight_position(0, lat, lng)
        time.sleep(0.01)
        count += 1
        if count > 300:
            break
    print(f'/plan post tmp list len : {len(tmp_flights_list)}')        

async def generate_positions(speed : float):
    global tmp_flights_list
    print(f'/plan get tmp list len : {len(tmp_flights_list)}')    
    # for idx in range(len(tmp_flights_list)):
    #     await generate_single_positions(speed, idx)
    tasks = [generate_single_positions(speed, idx) for idx in range(len(tmp_flights_list))]
    await asyncio.gather(*tasks)
    tmp_flights_list = [] # 초기화
        
    
async def generate_single_positions(speed : float, idx : int):
    global tmp_flights_list

    DB_FLIGHTS.append(Flight_Model(tmp_flights_list[idx].id))

    for pos_idx in range(tmp_flights_list[idx].get_flight_data_length()):
        alt, lat, lng = tmp_flights_list[idx].get_position(pos_idx)
        for db_fligth in DB_FLIGHTS:
            if db_fligth.id == tmp_flights_list[idx].id:
                db_fligth.add_flight_position(alt, lat, lng)
                await asyncio.sleep(1/speed)

    