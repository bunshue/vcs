
"""
各種建立資料的寫法

"""
'''
import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

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

'''


from tkinter import Label, Tk 
import time

window = Tk() 
window.title("Digital Clock") 
window.geometry("420x150") 
window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

label = Label(window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()

window.mainloop()


