# 5-5-2 deque - 快速穩定的堆疊

from collections import deque

s = deque()
s.append('吃飯')
s.append('睡覺')
s.append('寫程式')

print(s)
print(s[1])
print(s.pop())
print(s.pop())
print(s.pop())
#print(s.pop())