import math
import heapq
import pandas as pd

from database.index import LOCATIONS, CONNECTIONS 

aircraft_speeds = {
    'Multi-copter': 100,  # 예시 속도
    'Lift and Thrust': 150,
    'Tilt-rotor':200
}

def generate_trajectory(flight_plan : pd.DataFrame): # 경로 생성 예시 코드
    connection_distances = {}
    flight_plan_results = []
    
    # Calculate distances between connected nodes
    for start_id, end_ids in CONNECTIONS.items():
        connection_distances[start_id] = {}
        for end_id in end_ids:
            start_info = LOCATIONS[start_id]
            end_info = LOCATIONS[end_id]
            distance = haversine(start_info["lat"], start_info["lon"], end_info["lat"], end_info["lon"])
            connection_distances[start_id][end_id] = distance

    # 비행 계획 데이터를 순회하며 각 UAM에 대한 경로 계산 및 출력
    for index, row in flight_plan.iterrows():
        aircraft_id = row['Aircraft ID']
        aircraft_type = row['Aircraft Type']  # Aircraft Type 추가
        departure_time = row['Departure Time']  # 출발시간 추가
        from_location = row['From']
        to_location = row['To']

        # 시작 위치와 도착 위치를 노드 ID로 변환
        start_node = None
        end_node = None
        for loc_id, loc_info in LOCATIONS.items():
            if loc_info['name'] == from_location:
                start_node = loc_id
            elif loc_info['name'] == to_location:
                end_node = loc_id

        if start_node is not None and end_node is not None:
            # 경로 계산
            shortest_path, total_distance = calculate_path(connection_distances, start_node, end_node)
            
            # 최단 경로 출력
            print(f"{aircraft_id}: {LOCATIONS[start_node]['name']} -> {LOCATIONS[end_node]['name']} ({len(shortest_path)} nodes)")
            for i, node_id in enumerate(shortest_path):
                node_name = LOCATIONS[node_id]["name"]
                print(node_name, end=" -> " if i < len(shortest_path) - 1 else "\n")
            print(f"총 거리: {total_distance} km")
            print('\n')
            
            # 예상 소요시간 계산 (시간 단위)
            aircraft_speed = aircraft_speeds.get(aircraft_type, 80)  # 기본값 설정
            estimated_time = total_distance / aircraft_speed  # 소요시간 = 거리 / 속도

            # Append the result as a dictionary to the list
            flight_plan_results.append({
                'Aircraft ID': aircraft_id,
                'Aircraft Type': aircraft_type,
                'Departure Time': departure_time,
                'From': LOCATIONS[start_node]['name'],
                'To': LOCATIONS[end_node]['name'],
                'Path': ' -> '.join([LOCATIONS[node_id]["name"] for node_id in shortest_path]),
                'Total Distance (km)': total_distance,
                'Number of Nodes': len(shortest_path),
                'Estimated Time (mins)': 4 + estimated_time*60  # 예상 소요시간 추가
            })
        else:
            print(f"Error: Invalid LOCATIONS for {aircraft_id}")

    # DataFrame 생성 및 CSV 파일로 저장
    results_flight_plan = pd.DataFrame(flight_plan_results)
    results_flight_plan.to_csv('flight_plan_results.csv', index=False)

# Define the Haversine function to calculate distances
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

def calculate_path(connection_distances, start_node, end_node):
    shortest_path, total_distance = dijkstra(connection_distances, start_node, end_node)
    return shortest_path, total_distance

def dijkstra(graph, start, end):
    # 각 노드까지의 최단 거리를 저장하는 딕셔너리
    shortest_distance = {}
    # 각 노드의 이전 노드를 저장하는 딕셔너리 (최단 경로 추적용)
    previous_node = {}
    # 최단 거리를 아직 확인하지 않은 노드의 우선순위 큐
    priority_queue = []
    
    # 모든 노드의 초기 최단 거리를 무한대로 설정하고 시작 노드의 거리를 0으로 설정
    for node in graph:
        shortest_distance[node] = float('inf')
        previous_node[node] = None
        if node == start:
            shortest_distance[node] = 0
        heapq.heappush(priority_queue, (shortest_distance[node], node))
    
    # Dijkstra 알고리즘 메인 루프
    while priority_queue:
        # 우선순위 큐에서 현재까지의 최단 거리가 가장 작은 노드를 꺼냄
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 더 긴 경로를 이미 확인한 경우 무시
        if current_distance > shortest_distance[current_node]:
            continue
        
        # 현재 노드와 연결된 모든 이웃 노드에 대해 최단 거리 갱신 시도
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # 만약 더 짧은 경로를 찾았을 경우 최단 거리 및 이전 노드 갱신
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # 최단 경로 추적 및 최단 거리 반환
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_node[current_node]
    
    return path, shortest_distance[end]