import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print('開始計時')
starttime = int(time.time())    # 起始秒數

print("------------------------------------------------------------")  # 60個

import random           # 導入模組random

n = 3
for i in range(n):
    print("1-100     : ", random.randint(1, 100))

for i in range(n):
    print("500-1000  : ", random.randint(500, 1000))

for i in range(n):
    print("2000-3000 : ", random.randint(2000, 3000))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
print(num)

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(porker)              # 將次序打亂重新排列
print(porker)

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
print(ans)

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

print("目前Python版本是: ", sys.version)

print("------------------------------------------------------------")  # 60個

import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))

print("------------------------------------------------------------")  # 60個

import calendar

print(calendar.month(2020,1))

print("------------------------------------------------------------")  # 60個

import calendar

print(calendar.calendar(2020))

print("------------------------------------------------------------")  # 60個

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

print("------------------------------------------------------------")  # 60個
