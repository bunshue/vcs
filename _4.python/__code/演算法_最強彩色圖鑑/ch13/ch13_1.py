# ch13_1.py
from collections import deque
    
graph = {}                                  # 建立空字典
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']     # 建立字典graph, key='Tom'的值
people = deque()                            # 建立queue
people += graph['Tom']                      # 將graph字典Tom鍵的值加入people
print('列出people資料類型 : ',type(people))
print('列出搜尋名單       : ', people)
for name in range(len(people)):
    print(people.popleft())








