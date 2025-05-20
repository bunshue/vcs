import time
t = time.localtime()
print(t)
d = time.strftime("%Y/%m/%d %A", t)
h = time.strftime("%H:%M:%S", t)
print(d)
print(h)
