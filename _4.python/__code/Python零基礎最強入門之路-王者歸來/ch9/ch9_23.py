# ch9_23.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print("小兵數量 = ", len(armys))
    
