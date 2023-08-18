# ch13_21.py
import time
x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))


  













          


