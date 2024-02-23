# ch19_8.py
def gold(W, wt, val):
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

value = [10, 16, 20, 22, 25]                                # 金礦產值
weight = [3, 4, 3, 5, 5]                                    # 單項金礦所需人力
gold_weight = 10                                            # 總人力
print('最大產值 = {} 公斤'.format(gold(gold_weight, weight, value)))







   















