# ch16_3.py
def knapsack(W, wt, val):
    ''' 動態規劃演算法 '''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格
    for r in range(n + 1):                                  # 填入表格row
        for c in range(W + 1):                              # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r-1] <= c:
                table[r][c] = max(val[r-1] + table[r-1][c-wt[r-1]], table[r-1][c])
            else:
                table[r][c] = table[r-1][c]
    return table[n][W]

value = [20000,50000,40000,25000]                           # 商品價值
weight = [1, 4, 3, 1]                                       # 商品重量
bag_weight = 4                                              # 背包可容重量
print('商品價值 : ', knapsack(bag_weight, weight, value))







   















