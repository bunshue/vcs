# ex4_2.py
from queue import Queue

food = ['漢堡', '薯條', '可樂']
q = Queue()
for f in food:
    q.put(f)
    print('成功插入 %s 至佇列' % f)

print('佇列輸出')
while not q.empty():
    print(q.get())















