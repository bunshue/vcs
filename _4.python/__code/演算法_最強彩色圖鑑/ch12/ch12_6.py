# ch12_6.py
def is_OK(row, col):
    ''' 檢查是否可以放在此row, col位置 '''
    for i in range(1, row + 1):                 # 迴圈往前檢查是否衝突
        if (queens[row - i] == col              # 檢查欄
            or queens[row - i] == col - i       # 檢查左上角斜線
            or queens[row - i] == col + i):     # 檢查右上角斜線
            return False                        # 傳回有衝突, 不可使用
    return True                                 # 傳回可以使用

def location(row):
    ''' 搜尋特定row的col欄位 '''
    start = queens[row] + 1                     # 也許是回溯,所以start不一定是0                 
    for col in range(start, SIZE):
        if is_OK(row, col):
            return col                          # 暫時可以在(row,col)放置皇后   
    return -1                                   # 沒有適合位置所以回傳 -1

def solve():
    ''' 從特定row列開始找尋皇后的位置 '''
    row = 0
    while row >= 0 and row <= 7:
        col = location(row)
        if col < 0:                             # 如果回傳是 -1, 必須回溯前一列
            queens[row] = -1
            row -= 1                            # 設定row少1, 可以回溯前一列                      
        else:
            queens[row] = col                   # 第row列皇后位置是col
            row += 1                            # 往下一列    
    if row == -1:
      return False                              # 沒有解答
    else:
      return True                               # 找到解答

SIZE = 8                                        # 棋盤大小
queens = [-1] * SIZE                            # 預設皇后位置 
solve()                                         # 解此題目                               
for i in range(SIZE):                           # 繪製結果圖
    for j in range(SIZE):
        if queens[i] == j:
            print('Q', end='')
        else:
            print('1',end='')
    print()

