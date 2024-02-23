# ex14_2.py                 
def dijkstra(graph, start):
    visited = []
    index = start
    nodes = dict((k, INF) for k in graph)           # 設定節點為最大值    
    nodes[start] = 0                                # 設定起點為start
   
    while len(visited) < len(graph):                # 有幾個節點就執行幾次
        visited.append(index)
        for i in graph[index]:
            new_cost = nodes[index] + graph[index][i]   # 新路徑距離
            if  new_cost < nodes[i]:                # 新路徑如果比較短
                nodes[i] = new_cost                 # 採用新路徑
                
        next = INF
        for n in nodes:                             # 從串列中找出下一個節點
            if n in visited:                        # 如果已拜訪回到for選下一個
                continue
            if nodes[n] < next:                     # 找出新的最小權重節點
                next = nodes[n]
                index = n
    return nodes

INF = 9999
graph = {'A':{'A':0, 'B':2, 'C':4},
         'B':{'B':0, 'A':2, 'C':7, 'E':6},
         'C':{'C':0, 'A':4, 'D':6, 'E':2},
         'D':{'D':0, 'C':6, 'E':8, 'G':4},
         'E':{'E':0, 'B':6, 'C':2, 'D':8, 'G':2},
         'G':{'G':0, 'D':4, 'E':2}
        }
node = input('請輸入起點 : ')
rtn = dijkstra(graph, node)
print(rtn)













