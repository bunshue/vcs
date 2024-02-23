# ch13_9.py                 
def dfs(graph, start, goal):
    ''' 深度優先搜尋法 '''
    path = []                               # 拜訪過的節點
    stack = [start]                         # 模擬堆疊
    while stack:        
        node = stack.pop()                  # pop堆疊
        path.append(node)                   # 加入已拜訪行列
        if node == goal:                    # 如果找到了
            print('找到了')
            return path
        for n in graph[node]:               # 將相鄰節點放入佇列
            stack.append(n)
    return "找不到"

graph = {'A':['D', 'C', 'B'],
         'B':['E'],
         'C':['F'],
         'D':['H', 'G'],
         'E':[],
         'F':['J', 'I'],
         'G':[],
         'H':[],
         'I':[],
         'J':[]
        } 
print(dfs(graph,'A','G'))







