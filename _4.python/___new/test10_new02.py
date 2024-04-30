import os
import sys
import time
import random

'''
print("------------------------------------------------------------")  # 60個

"""
#按 ctrl + c 離開程式

import random, shutil, sys, time

PAUSE = 0.1  # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['0', '1']  # (!) Try changing this to other characters.

print('按 ctrl + c 離開程式')

try:
    while True:
        print(random.choice(STREAM_CHARS), end='')
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-hour clocks show 12:00, not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        print(hours, minutes, seconds)

        print('按 ctrl + c 離開程式')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""


print("------------------------------------------------------------")  # 60個

import itertools

print('test itertools')
local_y_range = range(10)
local_x_range = range(10)
coords = list(itertools.product(local_x_range, local_y_range))
random.shuffle(coords)
print(coords)


print("------------------------------------------------------------")  # 60個

print('test random.triangular')

for _ in range(10):
    print(random.triangular(1, 5))

print('test random.uniform')
for _ in range(10):
    print(random.uniform(0.2, 0.9))

print("------------------------------------------------------------")  # 60個

cc = 'ABC' * 5
print(cc)

cc = ['A', 'B', 'C'] * 5
print(cc)

cc = [1,2,3] * 5
print(cc)


cc = 'A' * 5
print(cc)

print("------------------------------------------------------------")  # 60個

a = [i for i in range(10)]
print(a)

a = (i for i in range(10))
print(a)


print("------------------------------------------------------------")  # 60個

import numpy as np

x1 = np.linspace(-2.0, 2.0, 11) #包含頭尾共21點

# 移除 x1 > 0.55 的點, 就是保存 x1 <=0.6的點
x2 = x1[x1 <= 0.55]

# 遮罩 x1 > 0.7 的點, 會多了點線標記
x3 = np.ma.masked_where(x1 > 0.7, x1)

print(x1)
print(x2)
print(x3)


"""
x = np.random.normal(mu, sigma, size=N*10)  # 隨機數

# list 移除資料的寫法
x2 = x[x <= 100.0]
x2 = x2[ x2 >= 0]

"""

#過濾資料

"""
scores1 = np.random.normal(mu, sigma, size=N)  # 隨機數
print("資料個數1 :", len(scores1))
print("最高分 :", max(scores1))
print("最低分 :", min(scores1))

scores2 = scores1[scores1 <= 100.0]
scores3 = scores2[scores2 >= 0.0]
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



import os
from pathlib import Path

cc = os.path.realpath(__file__)
print('目前檔案 :', cc)

cc = [str(Path(cc).parent)]
print('父資料夾 :', cc)

cc = __file__

print(cc)
'''
print("------------------------------------------------------------")  # 60個

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(type(portfolio))
print(portfolio)
print()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import re

s = ' hello world \n'
print("|"+s.strip()+"|")
print("|"+s.lstrip()+"|")
print("|"+s.rstrip()+"|")

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

# 对中间不会影响
s = ' hello     world \n'
print(s.strip())

print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))



print("------------------------------------------------------------")  # 60個

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 填充字符
print(text.rjust(20,'='))
print(text.center(20,'*'))

# format函数
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# 同时增加填充字符
print(format(text, '=>20s'))
print(format(text, '*^20s'))

# 格式化多个值
print('{:=>10s} {:*^10s}'.format('Hello', 'World'))

# 格式化数字
x = 1.2345
print(format(x, '=^10.2f'))

print("------------------------------------------------------------")  # 60個

"""
#plot 暫存
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]
plt.plot(x, y, marker='d',ms=10, mfc='r', mec='b')
"""

print("------------------------------------------------------------")  # 60個




import os

print(os.getcwd())
print(os.path.relpath('C:\\'))              # 列出目前工作目錄至C:\的相對路徑
print(os.path.relpath('C:\\___small\\Dropresize'))  # 列出目前工作目錄至特定path的相對路徑
print(os.path.relpath('C:\\', '*.py')) # 列出目前檔案至D:\的相對路徑

import os

print(os.path.abspath('.'))              # 列出目前工作目錄的絕對路徑
print(os.path.abspath('..'))             # 列出上一層工作目錄的絕對路徑
print(os.path.abspath('*.py'))      # 列出目前檔案的絕對路徑


import os

print(os.path.join('D:\\', 'Python', 'ch14', 'ch14_9.py'))   # 4個參數
print(os.path.join('D:\\Python', 'ch14', 'ch14_9.py'))       # 3個參數
print(os.path.join('D:\\Python\\ch14', 'ch14_9.py'))         # 2個參數


print("------------------------------------------------------------")  # 60個

import os
import os.path as path
 
fpath = os.getcwd() + "\\temp"
if path.exists(fpath+"\\ball0.jpg"):
    print("存在!")
if path.isdir(fpath+"\\test"):
    print("是目錄!")
if path.isfile(fpath+"\\ball0.jpg"):
    print("是檔案!")

print("------------------------------------------------------------")  # 60個


import sys

cc = sys.getdefaultencoding()

print(cc)


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
