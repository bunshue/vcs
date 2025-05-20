import time
st = time.time()
n = 0
for i in range(1000000):
    n = n + 1
et = time.time()
print("開始測量proc秒", st)
print("結束測量proc秒", et)
print("處理時間", et-st)
