# 5-5-3 LifoQueue - 可用於多執行緒的堆疊 (1)

from queue import LifoQueue

s= LifoQueue()
s.put('吃飯')
s.put('睡覺')
s.put('寫程式')

print(s)

print(s.get())
print(s.get())
print(s.get())
#print(s.get_nowait())