# 5-7-2 heapq - 快速的優先佇列

import heapq

q = []
heapq.heappush(q, (2, '寫程式'))
heapq.heappush(q, (1, '吃飯'))
heapq.heappush(q, (3, '睡覺'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)