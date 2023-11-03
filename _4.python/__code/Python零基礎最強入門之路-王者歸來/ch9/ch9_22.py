# ch9_22.py
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}         # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]                      # 小兵組成串列
for army in armys:                                          # 列印小兵
    print(army)
