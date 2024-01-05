# 定義迷宮
maze = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# 定義方向
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, path):
    # 到達終點
    if x == len(maze)-1 and y == len(maze[0])-1:
        return path + [(x, y)]
    
    # 標記已經走過的路徑
    maze[x][y] = -1
    
    # 遍歷四個方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 如果下一個位置在範圍內，且還沒有走過，就繼續往下搜尋
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1:
            res = dfs(nx, ny, path + [(x, y)])
            if res:
                return res
    
    return None

# 從起點開始搜索
path = dfs(0, 0, [])
if path:
    print("找到出口，路徑為：", path + [(len(maze)-1, len(maze[0])-1)])
else:
    print("沒有找到出口")
