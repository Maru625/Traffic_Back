import asyncio
import pandas as pd
import math
import time

from model.flight import Flight_DB as Flight_Model
from database.index import DB_flights as DB_FLIGHTS
from database.index import LOCATIONS

async def generate_positions(speed : float):
    # print(f'/plan get tmp list len : {len(tmp_flights_list)}')    
    # # for idx in range(len(tmp_flights_list)):
    # #     await generate_single_positions(speed, idx)
    # tasks = [generate_single_positions(speed, idx) for idx in range(len(tmp_flights_list))]
    # await asyncio.gather(*tasks)
    # tmp_flights_list = [] # 초기화

    # 파일에서 항공기 데이터를 로드합니다.
    flights = load_flights("C:/Users/HJW/Documents/Dev/TrafficSim/TrafficSim/FlightSchedules/flight_plan_results.csv")

    # 시뮬레이션 환경 생성
    simulation = SimulationEnvironment(start_time=0)

    # 생성된 항공기 객체들을 시뮬레이션 환경에 추가합니다.
    for flight in flights:
        simulation.add_flight(flight)

    # 시뮬레이션 실행
    simulation.run(duration=7200)  # 시뮬레이션 7200초(2시간) 동안 실행

    
    
async def generate_single_positions(speed : float, idx : int):
    global tmp_flights_list

    DB_FLIGHTS.append(Flight_Model(tmp_flights_list[idx].id))

    for pos_idx in range(tmp_flights_list[idx].get_flight_data_length()):
        alt, lat, lng = tmp_flights_list[idx].get_position(pos_idx)
        for db_fligth in DB_FLIGHTS:
            if db_fligth.id == tmp_flights_list[idx].id:
                db_fligth.add_flight_position(alt, lat, lng)
                await asyncio.sleep(1/speed)

def calculate_distance(lat1, lon1, lat2, lon2):
        return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

class Flight:
    def __init__(self, aircraft_id, aircraft_type, departure_time, from_vertiport, to_vertiport, path, total_distance, number_of_nodes, estimated_time):
        self.aircraft_id = aircraft_id
        self.current_node_index = 0
        self.is_moving = False
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.from_vertiport = from_vertiport
        self.to_vertiport = to_vertiport
        self.path = path
        self.total_distance = total_distance
        self.number_of_nodes = number_of_nodes
        self.estimated_time = estimated_time

        # 항공기 유형에 따른 속도 설정
        aircraft_speeds = {
            'Multi-copter': 100,  # 예시 속도
            'Lift and Thrust': 150,
            'Tilt-rotor': 200
        }
        self.speed = aircraft_speeds.get(aircraft_type, 60)  # 기본값으로 60 km/h 설정

            
def parse_path(self, path_str):
    # Path 문자열을 노드의 시퀀스로 변환합니다.
    path_names = path_str.split(" -> ")
    self.path = []
    for name in path_names:
        # LOCATIONS 사전에서 해당 이름을 가진 노드를 찾습니다.
        matched_node = next((node for node, info in LOCATIONS.items() if info["name"] == name), None)
        if matched_node is not None:
            self.path.append(matched_node)
        else:
            print(f"Node '{name}' not found in LOCATIONS.")

def simulate(self, current_time):
    if current_time >= self.departure_time and self.current_node_index < len(self.path) - 1:
        if not self.is_moving:
            self.departure_time = current_time
            self.is_moving = True

        current_node = self.path[self.current_node_index]
        next_node = self.path[self.current_node_index + 1]

        distance = calculate_distance(LOCATIONS[current_node]["lat"], LOCATIONS[current_node]["lon"], LOCATIONS[next_node]["lat"], LOCATIONS[next_node]["lon"])
        travel_time = distance / self.speed * 3600 * 60  # 이동 시간 (초)

        # 항공기가 이동한 시간 비율 계산
        time_ratio = (current_time - self.departure_time) / travel_time
        time_ratio = min(time_ratio, 1)  # 비율이 1을 초과하지 않도록 제한

        # 현재 위치 계산 (선형 보간)
        current_lat = LOCATIONS[current_node]["lat"] + (LOCATIONS[next_node]["lat"] - LOCATIONS[current_node]["lat"]) * time_ratio
        current_lon = LOCATIONS[current_node]["lon"] + (LOCATIONS[next_node]["lon"] - LOCATIONS[current_node]["lon"]) * time_ratio

        if current_time - self.departure_time >= travel_time:
            # 다음 노드로 이동
            self.current_node_index += 1
            self.is_moving = False
            print(f"{self.aircraft_id} has reached {LOCATIONS[next_node]['name']} at {current_time} mins")
        else:
            # print("1")
            print(f"{self.aircraft_id} is at latitude {current_lat}, longitude {current_lon} at {current_time} secs")

                
def load_flights(file_path):
    flights_data = pd.read_csv(file_path)
    flights = []
    for _, row in flights_data.iterrows():
        flight = Flight(row['Aircraft ID'], row['Aircraft Type'], row['Departure Time'], row['From'], row['To'], row['Path'], row['Total Distance (km)'], row['Number of Nodes'], row['Estimated Time (mins)'])
        flight.parse_path(row['Path'])  # parse_path 메서드 호출
        flights.append(flight)
    return flights


class SimulationEnvironment:
    def __init__(self, start_time):
        self.current_time = start_time
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def update(self):
        # 시간 업데이트 로직
        self.current_time += 1 
        # print(f"Current simulation time: {self.current_time} sec")

    def run(self, duration):
        # 시뮬레이션 실행 로직
        for _ in range(duration):
            self.update()
            for flight in self.flights:
                flight.simulate(self.current_time)
            time.sleep(1)  
