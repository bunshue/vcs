# ch13_3.py
from collections import deque
    
people = deque()                            # 建立queue
people.append('Ivan')                       # 右邊加入
people.append('Ira')                        # 右邊加入
print('列出名單 : ', people)
people.appendleft('Unistar')                # 右邊加入
print('列出名單 : ', people)
people.appendleft('Ice Rain')               # 右邊加入
print('列出名單 : ', people)








