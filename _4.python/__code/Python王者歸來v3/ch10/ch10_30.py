# ch10_30.py
# 定義飛行路線
routes = {
    frozenset({"Los Angeles", "New York"}): {"距離": 2451, "時間": "5h 15m"},
    frozenset({"New York", "Chicago"}): {"距離": 713, "時間": "2h 5m"},
    frozenset({"Chicago", "Los Angeles"}): {"距離": 1744, "時間": "4h 5m"},
    frozenset({"New York", "San Francisco"}): {"距離": 2572, "時間": "5h 30m"}
}

def get_route_info(city1, city2):
    # 使用 frozenset 確保無論城市的順序如何，都可以正確查詢路線
    route = frozenset({city1, city2})
    if route in routes:
        info = routes[route]
        print(f"距離 : {info['距離']:5d} miles, 時間 : {info['時間']}")
    else:
        print(f"No route found between {city1} and {city2}")

# 查詢路線資訊
get_route_info("New York", "Los Angeles")
get_route_info("Los Angeles", "New York")
get_route_info("New York", "Chicago")
get_route_info("San Francisco", "New York")


