# ch19_12.py
def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:                              # 1根篱笆的刷法
        return k
    same = k                                # 2根相同颜色刷法
    diff = k * (k - 1)                      # 2根不相同颜色刷法
    for i in range(3, n+1):                 # 3根篱笆以上的刷法
        same, diff = diff, (same+diff) * (k - 1)
    return same + diff                      # 回傳總計
                          
print(numWays(1, 2))
print(numWays(2, 2))
print(numWays(3, 2))
print(numWays(4, 2))










      



    





        





