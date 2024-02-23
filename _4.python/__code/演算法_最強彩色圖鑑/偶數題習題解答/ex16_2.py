# ex16_2.py
def fruits_bag(W, wt, val):
    ''' 動態規劃演算法 '''
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 最初化表格
    items = [[[] for x in range(W + 1)] for x in range(n + 1)]  # 最初化表格    
    for r in range(n + 1):                                  # 填入表格row
        for c in range(W + 1):                              # 填入表格column
            if r == 0 or c == 0:
                table[r][c] = 0
            elif wt[r-1] <= c:
                cur = val[r-1] + table[r-1][c-wt[r-1]]
                cur_items = []
                cur_items.append(item[r-1])
                if items[r-1][c-wt[r-1]]:
                    cur_items += items[r-1][c-wt[r-1]]
                pre = table[r-1][c]
                pre_items = items[r-1][c]                
                if cur > pre:   
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r-1][c]
                items[r][c] = items[r-1][c]
    return items, table[n][W]

item = ['釋迦', '西瓜', '玉荷包', '蘋果', '蓮霧', '番茄']
value = [800, 200, 600, 700, 400, 100]                      # 商品價值
weight = [5, 3, 2, 2, 3, 1]                                 # 商品重量
bag_weight = 5                                              # 背包可容重量
items, total_value = fruits_bag(bag_weight, weight, value)
print('最高價值 : ', total_value)
print('商品組合 : ', items[len(item)][bag_weight])







   















