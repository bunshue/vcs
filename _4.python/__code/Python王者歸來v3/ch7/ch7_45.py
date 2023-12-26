# ch7_45.py
fib = []
n = 9
fib.append(0)                   # fib[0] = 0
fib.append(1)                   # fib[1] = 1
for i in range(2,n+1):
    f = fib[i-1] + fib[i-2]     # fib[i] = fib[i-1]+fib[i-2]
    fib.append(f)               # 加入費式數列
for i in range(n+1):
    print(fib[i], end=', ')     # 輸出費式數列








    






