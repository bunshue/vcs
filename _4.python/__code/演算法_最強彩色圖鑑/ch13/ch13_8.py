# ch13_8.py
def is_exit(node):
    ''' 回應是否出口 ''' 
    if node == 'K':
        return True
def bfs(graph, start):
    ''' 寬度優先搜尋法 '''
    global visited                          # 拜訪過的頂點
    queue = [start]                         # 模擬佇列    
    while queue:        
        node = queue.pop(0)                 # 取索引0的值
        if is_exit(node):                   # 如果是True, 表示找到了
            print(node + ' 是迷宮出口 ')
            return visited                  # bfs()執行結束
        if node not in visited:
            visited.append(node)            # 加入已拜訪行列
            neighbors = graph[node]         # 取得已拜訪節點的相鄰節點           
            for n in neighbors:             # 將相鄰節點放入佇列
                queue.append(n)
    return visited

graph = {'A':['B'],
         'B':['A', 'C'],
         'C':['B', 'D', 'E'],
         'D':['C'],
         'E':['C', 'H'],
         'F':['G'],
         'G':['F', 'H'],
         'H':['E', 'G', 'I'],
         'I':['H', 'K'],
         'J':['G'],
         'K':['I']
        }
visited = []
print(bfs(graph,'A'))






