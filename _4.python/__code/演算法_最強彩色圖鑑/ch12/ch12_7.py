# ch12_7.py
class Queens:
    def __init__(self):
        self.queens = size * [-1]                       # 預設皇后位置 
        self.solve(0)                                   # 從row = 0 開始搜尋        
        for i in range(size):                           # 繪製結果圖
            for j in range(size):
                if self.queens[i] == j:
                    print('Q', end='')
                else:
                    print('1',end='')
            print()
    def is_OK(self, row, col):
        ''' 檢查是否可以放在此row, col位置 '''
        for i in range(1, row + 1):                     # 迴圈往前檢查是否衝突
            if (self.queens[row - i] == col             # 檢查欄
                or self.queens[row - i] == col - i      # 檢查左上角斜線
                or self.queens[row - i] == col + i):    # 檢查右上角斜線
                return False                            # 傳回有衝突, 不可使用
        return True                                     # 傳回可以使用
           
    def solve(self, row):
        ''' 從第 row 列開始找尋皇后的位置 '''
        if row == size:                                 # 終止搜尋條件
            return True     
        for col in range(size):
            self.queens[row] = col                       # 安置(row, col)
            if self.is_OK(row, col) and self.solve(row + 1):
                return True                             # 找到並返回   
        return False                                    # 表示此row沒有解答

size = 8                                                # 棋盤大小   
Queens()
