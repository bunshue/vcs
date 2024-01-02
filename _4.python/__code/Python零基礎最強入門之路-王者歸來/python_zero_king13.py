import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_14.py

import random           # 導入模組random

n = 3
for i in range(n):
    print("1-100     : ", random.randint(1, 100))

for i in range(n):
    print("500-1000  : ", random.randint(500, 1000))

for i in range(n):
    print("2000-3000 : ", random.randint(2000, 3000))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_16.py

import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在81-100間回應玩家猜對
        print("恭喜!答對了\n")
    else:                           # 隨機數在1-80間回應玩家猜錯
        print("答錯了!請再試一次\n")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_17.py

import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_18.py

import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(porker)              # 將次序打亂重新排列
print(porker)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_19.py


import time                         # 導入模組time

print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_20.py

import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案

yourNum = int(input("請猜1-10之間數字: "))
starttime = int(time.time())    # 起始秒數
while True:    
    if yourNum == ans:
        print("恭喜!答對了")
        endtime = int(time.time())  # 結束秒數
        print("所花時間: ", endtime - starttime, " 秒")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
    yourNum = int(input("請猜1-10之間數字: "))
        



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_22.py

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_23.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_24.py

import sys

print("目前Python版本是: ", sys.version)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_25.py

import sys

print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline()
print(msg)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_26.py

import sys

print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline(8)         # 讀8個字
print(msg)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_27.py

import sys

sys.stdout.write("I like Python")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_28.py

import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_29.py

import calendar

print(calendar.month(2020,1))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch13\ch13_30.py

import calendar

print(calendar.calendar(2020))


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
