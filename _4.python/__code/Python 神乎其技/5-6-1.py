# 5-6-1 deque - 快速穩定的佇列

from collections import deque

q = deque()
q.append('吃飯')
q.append('睡覺')
q.append('寫程式')

print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
#print(q.popleft())