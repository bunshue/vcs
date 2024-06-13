
"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
'''
#各種建立資料的寫法
print("range")

N1 = 3
N2 = 9
STEP = 2

a = range(N1)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = range(N1, N2)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = range(N1, N2, STEP)
print(a)
for _ in a:
    print(_, end=" ")
print()

"""
    range(101)可以產生一個0到100的整數序列。
    range(1, 100)可以產生一個1到99的整數序列。
    range(1, 100, 2)可以產生一個1到99的奇數序列，其中的2是步長，即數值序列的增量。
"""


print("使用np.linspace, 和range一樣")

a = np.arange(N1)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = np.arange(N1, N2)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = np.arange(N1, N2, STEP)
print(a)
for _ in a:
    print(_, end=" ")
print()


# 二維

W = 640
H = 480
w = 160
h = 160

for y in range(0, H, h):
    for x in range(0, W, w):
        print(x, y, end="    ")
print()

print("------------------------------------------------------------")  # 60個

print("使用np.linspace")

N1 = 3
N2 = 9
N = 2

x = np.linspace(N1, N2, N)  # 從N1到N2, 分成N個, 包含頭尾
print(x)

x = np.linspace(N1, N2)  # 若沒有給定N值, 則分成 50 個, 包含頭尾
print(x)

# np.linspace 若只給a b 則代表分成50點
x = np.linspace(0, 2 * np.pi)
print(x.shape)


import numpy as np

# 含頭尾共N個元素的陣列
N = 11
x = np.linspace(0, 10, 11)  # 建立含11個元素的陣列

print("包含頭尾之linespace :", x)


print("------------------------------------------------------------")  # 60個

n = list(range(100))
r = list(range(25))
n = list(range(10)) * 10

print("------------------------------------------------------------")  # 60個

for _ in range(10):
    a = random.randint(3, 8)  # 唯一包含頭尾
    print(a)

print("------------------------------------------------------------")  # 60個

W = 5
H = 5
nextCells = {}  # 字典
for x in range(H):
    for y in range(W):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = "Y"
        else:
            nextCells[(x, y)] = "N"
print(type(nextCells))
print(nextCells)

print("------------------------------------------------------------")  # 60個


print("20位 靠右對齊")

string = "abcdefg"
print(string.rjust(20))

number = 1234567
print(repr(int(number)).rjust(20))

print("4位 不對齊")
for _ in range(20):
    a = random.randint(0, 200)
    print(repr(int(a)), end=" ")
print()

print("4位 靠左對齊")
for _ in range(20):
    a = random.randint(0, 200)
    print(repr(int(a)).ljust(4), end="")
print()

print("------------------------------------------------------------")  # 60個

year = 2023
month = 3
day = 11
total = 123
print(f"{year}年{month}月{day}日是{year}年的第{total}天")

print("------------------------------------------------------------")  # 60個

import os

#用預設程式開啟檔案
#os.system('cccc.mp3')

#用預設程式wav檔案
#os.startfile('harumi99.wav')

#用系統預設程式開啟檔案
#os.system('cv03.png')

print("------------------------------------------------------------")  # 60個

import random
import time

N = 10
lst = list(range(N))
print(lst)
random.shuffle(lst)
print(lst)

lst.sort()
print(lst)

print("------------------------------------------------------------")  # 60個

import random

animals1 = ['鼠', '牛', '虎']
animals2 = ['兔', '龍', '蛇']
animals3 = ['馬', '羊', '猴']
animals4 = ['雞', '狗', '豬']

print('本次選出人員')
print(random.choice(animals1) + " " + random.choice(animals2) + " " + random.choice(animals3) + " "+ random.choice(animals4))

print("------------------------------------------------------------")  # 60個

import random

passlen = 3
s = "ABCDEFG"
p =  "".join(random.sample(s,passlen ))
print (p)

print("------------------------------------------------------------")  # 60個

number = 1234.5678
print("Number :", format(number, ".2f"))

print("------------------------------------------------------------")  # 60個

"""
import sys, time

PAUSE = 0.02

print('無限迴圈進行中..... 按 Ctrl+C離開 ')

try:
    while True:
        print("A", end = " ")
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.

    print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
   
except KeyboardInterrupt:
    print('你按了 Ctrl+C 離開')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""

print("------------------------------------------------------------")  # 60個
"""
import time
for i in range(5, 0, -1):
    print("\r", "倒计时{}秒！".format(i), end="", flush=True)
    time.sleep(1)
"""

print("------------------------------------------------------------")  # 60個
"""
print('目前的全螢幕截圖')

from PIL import ImageGrab

image = ImageGrab.grab()
filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
image.save(filename)

image = ImageGrab.grab().convert('L')  
data = image.load()
print(type(data))
#print(data.size)
if data[260, 300] > 150:
    #isCollision_day(data)
    print("aaaaaaa")
else:
    #isCollision_night(data)
    print("bbbbbbb")
"""
print("------------------------------------------------------------")  # 60個


import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)
'''

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


