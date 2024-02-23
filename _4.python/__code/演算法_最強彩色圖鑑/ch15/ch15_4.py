# ch15_4.py
def greedy(graph, cities, start):
    ''' 貪婪演算法計算業務員旅行 '''
    visited = []                                    # 儲存已拜訪城市
    visited.append(start)                           # 儲存起點城市
    start_i = cities.index(start)                   # 獲得起點城市的索引
    distance = 0                                    # 旅行距離
    for outer in range(len(cities) - 1):            # 尋找最近城市
        graph[start_i][start_i] = INF               # 將自己城市距離設為極大值
        min_dist = min(graph[start_i])              # 找出最短路徑
        distance += min_dist                        # 更新總路程距離        
        end_i = graph[start_i].index(min_dist)      # 最短距離城市的索引
        visited.append(cities[end_i])               # 將最短距離城市列入已拜訪
        for inner in range(len(graph)):             # 將已拜訪城市距離改為極大值
            graph[start_i][inner] = INF
            graph[inner][start_i] = INF
        start_i = end_i                             # 將下一個城市改為新的起點
    return distance, visited
        
INF = 9999                                          # 距離極大值
cities = ['新竹', '竹南', '竹北', '關西', '竹東']
graph = [[0, 12, 10, 28, 16],
         [12, 0, 20, 35, 19],
         [10, 20, 0, 21, 11],
         [28, 35, 21, 0, 12],
         [16, 19, 11, 12, 0]
        ]

dist, visited = greedy(graph, cities, '新竹')
print('拜訪順序 : ', visited)
print('拜訪距離 : ', dist)


   















