from model.flight import Flight_DB


DB_flights : list[Flight_DB] = []
DB_Test : int = 0

# 서울 UAM 운용시 주요 거점 정보
LOCATIONS = {
    1: {"name": "SuSeo Vertiport", "lat": 37.4909, "lon": 127.1056, "is_vertiport": True},
    2: {"name": "JamSil Vertiport", "lat": 37.5174, "lon": 127.0685, "is_vertiport": True},
    3: {"name": "YongSan Vertiport", "lat": 37.5288, "lon": 126.959, "is_vertiport": True},
    4: {"name": "Yeouido Vertiport", "lat": 37.5321, "lon": 126.9242, "is_vertiport": True},
    5: {"name": "Gimpo Airport Vertiport", "lat": 37.5598, "lon": 126.8043, "is_vertiport": True},
    6: {"name": "Godeok Vertiport", "lat": 37.5697, "lon": 127.1621, "is_vertiport": True},
    7: {"name": "Cheonho Vertiport", "lat": 37.5442, "lon": 127.1264, "is_vertiport": True},
    8: {"name": "Sangbong Vertiport", "lat": 37.5956, "lon": 127.0701, "is_vertiport": True},
    9: {"name": "Wangsimni Vertiport", "lat": 37.5672, "lon": 127.0408, "is_vertiport": True},
    10: {"name": "Yangjae Vertiport", "lat": 37.4905, "lon": 127.0467, "is_vertiport": True},
    11: {"name": "Gwanghwamun Vertiport", "lat": 37.5771, "lon": 126.9814, "is_vertiport": True},
    12: {"name": "SinChon Vertiport", "lat": 37.5621, "lon": 126.9334, "is_vertiport": True},
    13: {"name": "Mapo Vertiport", "lat": 37.5507, "lon": 126.9134, "is_vertiport": True},
    14: {"name": "Sangam Vertiport", "lat": 37.5697, "lon": 126.8837, "is_vertiport": True},
    15: {"name": "Mokdong Vertiport", "lat": 37.5303, "lon": 126.8828, "is_vertiport": True},
    16: {"name": "Gimpo Vertiport", "lat": 37.6672, "lon": 126.6752, "is_vertiport": True},
    17: {"name": "Incheon Airport Vertiport", "lat": 37.4501, "lon": 126.469, "is_vertiport": True},
    18: {"name": "Tancheon Bridge 1", "lat": 37.497, "lon": 127.094, "is_vertiport": False},
    19: {"name": "Dogok Road", "lat": 37.5038, "lon": 127.0708, "is_vertiport": False},
    20: {"name": "Seongsu Bridge Intersection", "lat": 37.5369, "lon": 127.0356, "is_vertiport": False},
    21: {"name": "Dongho Bridge", "lat": 37.5374, "lon": 127.0223, "is_vertiport": False},
    22: {"name": "Dongjak Bridge", "lat": 37.5099, "lon": 126.9825, "is_vertiport": False},
    23: {"name": "Hangang Railway Bridge", "lat": 37.5208, "lon": 126.9522, "is_vertiport": False},
    24: {"name": "Bam Island", "lat": 37.5363, "lon": 126.9327, "is_vertiport": False},
    25: {"name": "Dangsan Railway Bridge Intersection", "lat": 37.5409, "lon": 126.9083, "is_vertiport": False},
    26: {"name": "Sangam-Mokdong Intersection", "lat": 37.5636, "lon": 126.8727, "is_vertiport": False},
    27: {"name": "Magok Railway Bridge", "lat": 37.5816, "lon": 126.8409, "is_vertiport": False},
    28: {"name": "Jangham Wetland", "lat": 37.6334, "lon": 126.751, "is_vertiport": False}
}

# 각 노드간 연결 정보
CONNECTIONS = { 
    1: [18],
    2: [19, 20],
    3: [23],
    4: [24, 25],
    5: [27, 17],
    6: [7],
    7: [6, 19],
    8: [9],
    9: [8, 11, 20],
    10: [20, 19, 17],
    11: [12, 9],
    12: [11, 13],
    13: [12, 25],
    14: [26],
    15: [26, 25, 17, 10],
    16: [17, 28],
    17: [16, 15, 10, 5],
    18: [1, 19],
    19: [18, 2, 7, 10],
    20: [21, 2, 9, 10],
    21: [22, 20],
    22: [23, 21],
    23: [24, 22, 3],
    24: [4, 23, 25],
    25: [4, 13, 26, 15, 24],
    26: [25, 15, 14, 27],
    27: [5, 26],
    28: [16, 27]
}
