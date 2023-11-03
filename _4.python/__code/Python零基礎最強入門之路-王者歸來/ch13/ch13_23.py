# ch13_23.py
import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])




