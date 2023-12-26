# ex13_6.py
import random                       # 導入模組random

num = []
for i in range(600):
    num.append(random.choice([1,2,3,4,5,6]))
    
numCount = {i:num.count(i) for i in num}
for num in sorted(numCount.keys()):
    print(num, ':', numCount[num])






