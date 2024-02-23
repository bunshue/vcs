# ex16_4.py
def traveling(W, wt, val):
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

item = ['頤和園', '天壇', '故宮', '萬里長城', '圓明園']
value = [7, 6, 9, 9, 8]                                     # 旅遊點評分數
weight = [1, 1, 2, 4, 1]                                    # 單項景點所需天數
travel_weight = 4                                           # 總旅遊天數
items, total_value = traveling(travel_weight, weight, value)
print('旅遊點評總分 : ', total_value)
print('旅遊景點組合 : ', items[len(item)][travel_weight])







   















