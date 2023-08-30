'''
一大堆random範例

'''

import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在此區間回應玩家猜對
        print("恭喜!答對了\n")
    else:                           # 隨機數在此區間回應玩家猜錯
        print("答錯了!請再試一次\n")

print('------------------------------------------------------------')	#60個

import random

for i in range(5):
    print(random.random())
    
print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個

import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print('------------------------------------------------------------')	#60個

import random                       # 導入模組random

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end=",")

print('------------------------------------------------------------')	#60個

import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)              # 將次序打亂重新排列
    print(porker)

print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)           # 列印特別號

print('------------------------------------------------------------')	#60個

import random
random.seed(5)
for i in range(5):
    print(random.random())
    
print('------------------------------------------------------------')	#60個

import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
yourNum = int(input("請猜1-10之間數字: "))
starttime = int(time.time())        # 起始秒數
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

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

print(time.ctime())

print('------------------------------------------------------------')	#60個

import time
x = 1000000
pi = 0
time.clock()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.clock()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))

print('------------------------------------------------------------')	#60個

import time
x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))

print('------------------------------------------------------------')	#60個

import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))

print('------------------------------------------------------------')	#60個

import calendar

print(calendar.month(2020,1))

print('------------------------------------------------------------')	#60個

import calendar

print(calendar.calendar(2020))

print('------------------------------------------------------------')	#60個

import random                       # 導入模組random
money = 300                         # 賭金總額
bet = 100                           # 賭注
min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("歡迎光臨 : 目前籌碼金額 %d 美金 " % money)
    print("每次賭注 %d 美金 " % bet)
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在此區間回應玩家猜對
        print("恭喜!答對了\n")
        money += bet                # 賭金總額增加
    else:                           # 隨機數在此區間回應玩家猜錯
        print("答錯了!請再試一次\n")
        money -= bet                # 賭金總額減少
    if money <= 0:
        break

print("歡迎下次再來")

print('------------------------------------------------------------')	#60個

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)

print('------------------------------------------------------------')	#60個
