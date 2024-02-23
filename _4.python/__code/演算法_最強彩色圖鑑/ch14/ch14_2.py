# ch14_2.py                 
def get_edges(graph):
    ''' 建立邊線資訊 '''
    n1 = []                                 # 線段的節點1
    n2 = []                                 # 線段的節點2
    weight = []                             # 定義線段權重串列
    for i in graph:                         # 為每一個線段建立兩端的節點串列
        for j in graph[i]:
            if graph[i][j] != 0:
                weight.append(graph[i][j])
                n1.append(i)
                n2.append(j)
    return n1, n2, weight

def bellman_ford(graph, start):
    n1, n2, weight = get_edges(graph)
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0
    for times in range(len(graph) - 1):     # 執行迴圈len(graph)-1次
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]     # 新的路徑花費
            if  new_cost < nodes[n2[i]]:            # 新路徑如果比較短
                nodes[n2[i]] = new_cost             # 採用新路徑
                cycle = 1
        if cycle == 0:                              # 如果沒有更改結束for迴圈
            break
    flag = 0
# 下一個迴圈是檢查是否存在負權重的迴圈
    for i in range(len(nodes)):             # 對每條邊線在執行一次鬆弛操作
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:                                # 如果有變化表示有負權重的迴圈
        return '圖形含負權重的迴圈'
    return nodes

INF = 999
graph = {'A':{'A':0, 'B':2, 'C':4},
         'B':{'B':0, 'C':7, 'E':6},
         'C':{'C':0, 'D':6, 'E':2},
         'D':{'D':0, 'E':8, 'G':4},
         'E':{'E':0, 'G':2},
         'G':{'G':0}
        }

rtn = bellman_ford(graph, 'A')
print(rtn)



                                 
                                 














