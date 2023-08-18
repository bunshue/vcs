# ch7_20.py
x = 1000000
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        print("當 i = %7d 時 PI = %20.19f" % (i, pi))


  













          


