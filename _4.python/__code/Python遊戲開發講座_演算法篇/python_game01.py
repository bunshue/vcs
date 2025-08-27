"""
python_game01.py

"""

import tkinter as tk

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

import calendar

print(calendar.month(2021, 3))

print("------------------------------------------------------------")  # 60個

import datetime

n = datetime.datetime.now()
print(n)
print("取得小時", n.hour)
print("取得分鐘", n.minute)
print("取得秒", n.second)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter3\janken_game_1.py

print("========== 計時開始 ==========")
ts = time.time()
print("epoch秒數", ts)

input("計算按下Enter鍵之前的時間")  # input

te = time.time()
print("epoch秒數", te)
print("========== 計時結束 ==========")
print("遊戲秒數", te - ts)
print("遊戲秒數", int(te - ts))

print("------------------------------------------------------------")  # 60個

KUJI = ["大大吉", "大吉", "中吉", "小吉", "凶"]
input("請抽籤([Enter]鍵)")
print(random.choice(KUJI))

print("------------------------------------------------------------")  # 60個

t = time.localtime()
print(t)
d = time.strftime("%Y/%m/%d %A", t)
h = time.strftime("%H:%M:%S", t)
print(d)
print(h)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter8\monte_carlo_pi.py

pi = 0
rp = 0
cp = 0


def main():
    global pi, rp, cp
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    rp += 1
    col = "red"
    if (x - 200) * (x - 200) + (y - 200) * (y - 200) <= 200 * 200:
        cp += 1
        col = "blue"
    ca.create_rectangle(x, y, x + 1, y + 1, fill=col, width=0)
    ca.update()
    pi = 4 * cp / rp
    root.title("圓周率 " + str(pi))
    if rp < 10000:
        root.after(1, main)


root = tk.Tk()
ca = tk.Canvas(width=400, height=400, bg="black")
ca.pack()
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_1.py
print("井字遊戲1")


def masume():
    cvs.create_line(200, 0, 200, 600, fill="gray", width=8)
    cvs.create_line(400, 0, 400, 600, fill="gray", width=8)
    cvs.create_line(0, 200, 600, 200, fill="gray", width=8)
    cvs.create_line(0, 400, 600, 400, fill="gray", width=8)


root = tk.Tk()
root.title("井字遊戲1")
root.resizable(False, False)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_2.py
print("井字遊戲2")

masu = [[1, 0, 0], [0, 0, 2], [0, 0, 0]]


def masume():
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)


root = tk.Tk()
root.title("井字遊戲2")
root.resizable(False, False)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_3.py
print("井字遊戲3")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)


def click(e):
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
    else:
        masu[my][mx] = 0
    masume()


root = tk.Tk()
root.title("井字遊戲3")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_4.py
print("井字遊戲4")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
shirushi = 0


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)
    cvs.update()


def click(e):
    global shirushi
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        if shirushi < 9:
            computer()


def computer():
    global shirushi
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            masume()
            time.sleep(0.5)
            break


root = tk.Tk()
root.title("井字遊戲4")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_5.py
print("井字遊戲5")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
shirushi = 0
kachi = 0


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)
    cvs.update()


def click(e):
    global shirushi
    if shirushi == 1 or shirushi == 3 or shirushi == 5 or shirushi == 7:
        return
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        hantei()
        if shirushi < 9:
            computer()


def computer():
    global shirushi
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            masume()
            time.sleep(0.5)
            hantei()
            break


def hantei():
    global kachi
    kachi = 0
    for n in range(1, 3):
        # 判斷符號是否於垂直方向連成一線
        if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
            kachi = n
        if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
            kachi = n
        if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
            kachi = n
        # 判斷符號是否於水平方向連成一線
        if masu[0][0] == n and masu[0][1] == n and masu[0][2] == n:
            kachi = n
        if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
            kachi = n
        if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
            kachi = n
        # 判斷符號是否於傾斜方向連成一線
        if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
            kachi = n
        if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
            kachi = n
    if kachi == 1:
        root.title("〇連成一線了")
    if kachi == 2:
        root.title("×連成一線了")


root = tk.Tk()
root.title("井字遊戲5")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\list5_6.py
print("井字遊戲6")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
shirushi = 0
kachi = 0
FNT = ("Times New Roman", 60)


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)
    if shirushi == 0:
        cvs.create_text(300, 300, text="遊戲開始！", fill="navy", font=FNT)
    cvs.update()


def click(e):
    global shirushi
    if shirushi == 9:
        replay()
        return
    if shirushi == 1 or shirushi == 3 or shirushi == 5 or shirushi == 7:
        return
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        hantei()
        syouhai()
        if shirushi < 9:
            computer()


def computer():
    global shirushi
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            masume()
            time.sleep(0.5)
            hantei()
            syouhai()
            break


def hantei():
    global kachi
    kachi = 0
    for n in range(1, 3):
        # 判斷符號是否於垂直方向連成一線
        if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
            kachi = n
        if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
            kachi = n
        if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
            kachi = n
        # 判斷符號是否於水平方向連成一線
        if masu[0][0] == n and masu[0][1] == n and masu[0][2] == n:
            kachi = n
        if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
            kachi = n
        if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
            kachi = n
        # 判斷符號是否於傾斜方向連成一線
        if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
            kachi = n
        if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
            kachi = n


def syouhai():
    global shirushi
    if kachi == 1:
        cvs.create_text(300, 300, text="玩家獲勝！", font=FNT, fill="cyan")
        shirushi = 9
    if kachi == 2:
        cvs.create_text(300, 300, text="電腦\n獲勝！", font=FNT, fill="gold")
        shirushi = 9
    if kachi == 0 and shirushi == 9:
        cvs.create_text(300, 300, text="平手", font=FNT, fill="lime")


def replay():
    global shirushi
    shirushi = 0
    for y in range(3):
        for x in range(3):
            masu[y][x] = 0
    masume()


root = tk.Tk()
root.title("井字遊戲6")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\sanmoku_narabe.py
print("井字遊戲7")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
shirushi = 0
kachi = 0
FNT = ("Times New Roman", 60)


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        cvs.create_line(200 * i, 0, 200 * i, 600, fill="gray", width=8)
        cvs.create_line(0, i * 200, 600, i * 200, fill="gray", width=8)
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 20, Y + 20, X + 180, Y + 180, outline="blue", width=12
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 20, Y + 20, X + 180, Y + 180, fill="red", width=12)
                cvs.create_line(X + 180, Y + 20, X + 20, Y + 180, fill="red", width=12)
    if shirushi == 0:
        cvs.create_text(300, 300, text="遊戲開始！", fill="navy", font=FNT)
    cvs.update()


def click(e):
    global shirushi
    if shirushi == 9:
        replay()
        return
    if shirushi == 1 or shirushi == 3 or shirushi == 5 or shirushi == 7:
        return
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        hantei()
        syouhai()
        if shirushi < 9:
            computer()
            masume()
            time.sleep(0.5)
            hantei()
            syouhai()


def computer():
    global shirushi
    # 有沒有連成一線的符號
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 2
                hantei()
                if kachi == 2:
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    # 阻止玩家連成一線
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 1
                hantei()
                if kachi == 1:
                    masu[y][x] = 2
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            break


def hantei():
    global kachi
    kachi = 0
    for n in range(1, 3):
        # 判斷垂直方向是否連成一線
        if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
            kachi = n
        if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
            kachi = n
        if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
            kachi = n
        # 判斷水平方向是否連成一線
        if masu[0][0] == n and masu[0][1] == n and masu[0][2] == n:
            kachi = n
        if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
            kachi = n
        if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
            kachi = n
        # 判斷傾斜方向是否連成一線
        if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
            kachi = n
        if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
            kachi = n


def syouhai():
    global shirushi
    if kachi == 1:
        cvs.create_text(300, 300, text="玩家獲勝！", font=FNT, fill="cyan")
        shirushi = 9
    if kachi == 2:
        cvs.create_text(300, 300, text="電腦\n獲勝！", font=FNT, fill="gold")
        shirushi = 9
    if kachi == 0 and shirushi == 9:
        cvs.create_text(300, 300, text="平手", font=FNT, fill="lime")


def replay():
    global shirushi
    shirushi = 0
    for y in range(3):
        for x in range(3):
            masu[y][x] = 0
    masume()


root = tk.Tk()
root.title("井字遊戲7")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter5\sanmoku_narabe_kai.py
print("井字遊戲8")

masu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
shirushi = 0
kachi = 0
FNT = ("Times New Roman", 60)


def masume():
    cvs.delete("all")
    for i in range(1, 3):
        n = 200 * i
        cvs.create_line(
            n,
            0,
            n - 10,
            200,
            n + 10,
            400,
            n,
            600,
            fill="lightgreen",
            width=8,
            smooth=True,
        )
        cvs.create_line(
            0,
            n,
            200,
            n - 10,
            400,
            n + 10,
            600,
            n,
            fill="lightgreen",
            width=8,
            smooth=True,
        )
    for y in range(3):
        for x in range(3):
            X = x * 200
            Y = y * 200
            if masu[y][x] == 1:
                cvs.create_oval(
                    X + 40, Y + 40, X + 160, Y + 160, outline="skyblue", width=30
                )
            if masu[y][x] == 2:
                cvs.create_line(X + 40, Y + 40, X + 160, Y + 160, fill="pink", width=24)
                cvs.create_line(X + 160, Y + 40, X + 40, Y + 160, fill="pink", width=24)
    if shirushi == 0:
        cvs.create_text(300, 300, text="遊戲開始！", fill="navy", font=FNT)
    cvs.update()


def click(e):
    global shirushi
    if shirushi == 9:
        replay()
        return
    if shirushi == 1 or shirushi == 3 or shirushi == 5 or shirushi == 7:
        return
    mx = int(e.x / 200)
    my = int(e.y / 200)
    if mx > 2:
        mx = 2
    if my > 2:
        my = 2
    if masu[my][mx] == 0:
        masu[my][mx] = 1
        shirushi = shirushi + 1
        masume()
        time.sleep(0.5)
        hantei()
        syouhai()
        if shirushi < 9:
            computer()
            masume()
            time.sleep(0.5)
            hantei()
            syouhai()


def computer():
    global shirushi
    # 有沒有連成一線的符號
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 2
                hantei()
                if kachi == 2:
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    # 阻止玩家連成一線
    for y in range(3):
        for x in range(3):
            if masu[y][x] == 0:
                masu[y][x] = 1
                hantei()
                if kachi == 1:
                    masu[y][x] = 2
                    shirushi = shirushi + 1
                    return
                masu[y][x] = 0
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if masu[y][x] == 0:
            masu[y][x] = 2
            shirushi = shirushi + 1
            break


def hantei():
    global kachi
    kachi = 0
    for n in range(1, 3):
        # 判斷垂直方向是否連成一線
        if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
            kachi = n
        if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
            kachi = n
        if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
            kachi = n
        # 判斷水平方向是否連成一線
        if masu[0][0] == n and masu[0][1] == n and masu[0][2] == n:
            kachi = n
        if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
            kachi = n
        if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
            kachi = n
        # 判斷傾斜方向是否連成一線
        if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
            kachi = n
        if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
            kachi = n


def syouhai():
    global shirushi
    if kachi == 1:
        cvs.create_text(300, 300, text="玩家獲勝！", font=FNT, fill="cyan")
        shirushi = 9
    if kachi == 2:
        cvs.create_text(300, 300, text="電腦\n獲勝！", font=FNT, fill="gold")
        shirushi = 9
    if kachi == 0 and shirushi == 9:
        cvs.create_text(300, 300, text="引き分け", font=FNT, fill="lime")


def replay():
    global shirushi
    shirushi = 0
    for y in range(3):
        for x in range(3):
            masu[y][x] = 0
    masume()


root = tk.Tk()
root.title("井字遊戲8")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=600, bg="ivory")
cvs.pack()
masume()
root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_1.py
print("黑白棋1")


def banmen():
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")


root = tk.Tk()
root.title("黑白棋1")
root.resizable(False, False)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_2.py
print("黑白棋2")

BLACK = 1
WHITE = 2
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def click(e):
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7
    if board[my][mx] == 0:
        board[my][mx] = BLACK
    elif board[my][mx] == BLACK:
        board[my][mx] = WHITE
    elif board[my][mx] == WHITE:
        board[my][mx] = 0
    banmen()


def banmen():
    cvs.delete("all")
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)


root = tk.Tk()
root.title("黑白棋2")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_3.py
print("黑白棋3")

BLACK = 1
WHITE = 2
board = [
    [0, 2, 2, 2, 2, 2, 2, 1],
    [2, 2, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 0, 1, 0, 0],
    [2, 0, 0, 1, 0, 2, 0, 0],
    [2, 0, 0, 0, 0, 2, 0, 0],
    [2, 0, 0, 1, 2, 0, 2, 1],
    [2, 0, 0, 0, 0, 2, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
]


def click(e):
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7
    if board[my][mx] == 0:
        ishi_utsu(mx, my, BLACK)
    banmen()


def banmen():
    cvs.delete("all")
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


root = tk.Tk()
root.title("黑白棋3")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_4.py
print("黑白棋4")

BLACK = 1
WHITE = 2
board = [
    [0, 2, 2, 0, 2, 2, 2, 1],
    [2, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 2, 0, 0, 1, 2, 0],
    [1, 0, 0, 1, 0, 2, 2, 0],
    [0, 0, 0, 0, 0, 2, 2, 0],
    [0, 0, 0, 1, 2, 0, 2, 1],
    [2, 0, 0, 2, 0, 2, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
]


def click(e):
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7
    if board[my][mx] == 0:
        ishi_utsu(mx, my, BLACK)
    banmen()


def banmen():
    cvs.delete("all")
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
            if kaeseru(x, y, BLACK) > 0:
                cvs.create_oval(X + 5, Y + 5, X + 75, Y + 75, outline="cyan", width=2)
    cvs.update()


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


root = tk.Tk()
root.title("黑白棋4")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
banmen()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_5.py
print("黑白棋5")

BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7


def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver")
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False


# 電腦的思考邏輯
def computer_0(iro):  # 隨機落子
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro) > 0:
            return rx, ry


def main():
    global mc, proc, turn, msg
    banmen()
    if proc == 0:  # 等待遊戲開始
        msg = "點選畫面，開始對奕"
        if mc == 1:  # 點選視窗
            mc = 0
            turn = 0
            proc = 1
    elif proc == 1:  # 顯示換誰下棋的訊息
        msg = "換您下棋"
        if turn == 1:
            msg = "電腦 思考中."
        proc = 2
    elif proc == 2:  # 決定落子的位置
        if turn == 0:  # 玩家
            if mc == 1:
                mc = 0
                if kaeseru(mx, my, BLACK) > 0:
                    ishi_utsu(mx, my, BLACK)
                    proc = 3
        else:  # 電腦
            cx, cy = computer_0(WHITE)
            ishi_utsu(cx, cy, WHITE)
            proc = 3
    elif proc == 3:  # 換邊下棋
        turn = 1 - turn
        proc = 4
    elif proc == 4:  # 確認有沒有可以落子的棋格
        if uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            msg = "雙方皆無處落子，對奕結束"
        elif turn == 0 and uteru_masu(BLACK) == False:
            msg = "你沒有可落子之處，換邊下棋"
            proc = 3
        elif turn == 1 and uteru_masu(WHITE) == False:
            msg = "電腦沒有可落子之處，換邊下棋"
            proc = 3
        else:
            proc = 1
    root.after(100, main)


root = tk.Tk()
root.title("黑白棋5")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter7\list7_6.py
print("黑白棋6")

import tkinter.messagebox

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0] * 2
who = ["玩家", "電腦"]
board = []
for y in range(8):
    board.append([0, 0, 0, 0, 0, 0, 0, 0])


def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7


def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False


# 計算黑棋與白棋各有幾顆
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK:
                b += 1
            if board[y][x] == WHITE:
                w += 1
    return b, w


# 電腦的思考邏輯
def computer_0(iro):  # 隨機落子
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro) > 0:
            return rx, ry


def main():
    global mc, proc, turn, msg, space
    banmen()
    if proc == 0:  # 標題畫面
        msg = "請選擇先攻或後攻"
        cvs.create_text(320, 200, text="Reversi", fill="gold", font=FL)
        cvs.create_text(160, 440, text="先攻(黑)", fill="lime", font=FS)
        cvs.create_text(480, 440, text="後攻(白)", fill="lime", font=FS)
        if mc == 1:  # 點選視窗
            mc = 0
            if (mx == 1 or mx == 2) and my == 5:
                ban_syokika()
                color[0] = BLACK
                color[1] = WHITE
                turn = 0
                proc = 1
            if (mx == 5 or mx == 6) and my == 5:
                ban_syokika()
                color[0] = WHITE
                color[1] = BLACK
                turn = 1
                proc = 1
    elif proc == 1:  # 顯示換誰下棋的訊息
        msg = "換您下棋"
        if turn == 1:
            msg = "電腦  思考中."
        proc = 2
    elif proc == 2:  # 決定落子的位置
        if turn == 0:  # 玩家
            if mc == 1:
                mc = 0
                if kaeseru(mx, my, color[turn]) > 0:
                    ishi_utsu(mx, my, color[turn])
                    space -= 1
                    proc = 3
        else:  # 電腦
            cx, cy = computer_0(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc == 3:  # 換邊下棋
        msg = ""
        turn = 1 - turn
        proc = 4
    elif proc == 4:  # 確認有沒有可以落子的棋格
        if space == 0:
            proc = 5
        elif uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            tk.messagebox.showinfo("", "雙方皆無處落子，對奕結束")
            proc = 5
        elif uteru_masu(color[turn]) == False:
            tk.messagebox.showinfo("", who[turn] + "沒有可落子之處，換邊下棋")
            proc = 3
        else:
            proc = 1
    elif proc == 5:  # 判斷勝負
        b, w = ishino_kazu()
        tk.messagebox.showinfo("對奕結束", "黑={}、白={}".format(b, w))
        if (color[0] == BLACK and b > w) or (color[0] == WHITE and w > b):
            tk.messagebox.showinfo("", "玩家獲勝！")
        elif (color[1] == BLACK and b > w) or (color[1] == WHITE and w > b):
            tk.messagebox.showinfo("", "電腦獲勝！")
        else:
            tk.messagebox.showinfo("", "平手")
        proc = 0
    root.after(100, main)


root = tk.Tk()
root.title("黑白棋6")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

print("------------------------------------------------------------")  # 60個

print("黑白棋7")

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter8\list8_2.py

import tkinter.messagebox

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0] * 2
who = ["玩家", "電腦"]
board = []
for y in range(8):
    board.append([0] * 8)


def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7


def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False


# 計算黑棋與白棋各有幾顆
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK:
                b += 1
            if board[y][x] == WHITE:
                w += 1
    return b, w


point = [
    [6, 2, 5, 4, 4, 5, 2, 6],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [6, 2, 5, 4, 4, 5, 2, 6],
]


def computer_1(iro):  # 搜尋優先落子棋格
    sx = 0
    sy = 0
    p = 0
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0 and point[y][x] > p:
                p = point[y][x]
                sx = x
                sy = y
    return sx, sy


def main():
    global mc, proc, turn, msg, space
    banmen()
    if proc == 0:  # 標題畫面
        msg = "請選擇先攻或後攻"
        cvs.create_text(320, 200, text="Reversi", fill="gold", font=FL)
        cvs.create_text(160, 440, text="先攻(黑)", fill="lime", font=FS)
        cvs.create_text(480, 440, text="後攻(白)", fill="lime", font=FS)
        if mc == 1:  # 點選視窗
            mc = 0
            if (mx == 1 or mx == 2) and my == 5:
                ban_syokika()
                color[0] = BLACK
                color[1] = WHITE
                turn = 0
                proc = 1
            if (mx == 5 or mx == 6) and my == 5:
                ban_syokika()
                color[0] = WHITE
                color[1] = BLACK
                turn = 1
                proc = 1
    elif proc == 1:  # 顯示換誰下棋的訊息
        msg = "換您下棋"
        if turn == 1:
            msg = "電腦  思考中."
        proc = 2
    elif proc == 2:  # 決定落子的位置
        if turn == 0:  # 玩家
            if mc == 1:
                mc = 0
                if kaeseru(mx, my, color[turn]) > 0:
                    ishi_utsu(mx, my, color[turn])
                    space -= 1
                    proc = 3
        else:  # 電腦
            cx, cy = computer_1(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc == 3:  # 換邊下棋
        msg = ""
        turn = 1 - turn
        proc = 4
    elif proc == 4:  # 確認有沒有可以落子的棋格
        if space == 0:
            proc = 5
        elif uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            tk.messagebox.showinfo("", "雙方皆無處落子，對奕結束")
            proc = 5
        elif uteru_masu(color[turn]) == False:
            tk.messagebox.showinfo("", who[turn] + "沒有可落子之處，換邊下棋")
            proc = 3
        else:
            proc = 1
    elif proc == 5:  # 判斷勝負
        b, w = ishino_kazu()
        tk.messagebox.showinfo("對奕結束", "黑={}、白={}".format(b, w))
        if (color[0] == BLACK and b > w) or (color[0] == WHITE and w > b):
            tk.messagebox.showinfo("", "玩家獲勝！")
        elif (color[1] == BLACK and b > w) or (color[1] == WHITE and w > b):
            tk.messagebox.showinfo("", "電腦獲勝！")
        else:
            tk.messagebox.showinfo("", "平手")
        proc = 0
    root.after(100, main)


root = tk.Tk()
root.title("黑白棋7")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter8\reversi.py
print("黑白棋8")

import tkinter.messagebox

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0] * 2
who = ["玩家", "電腦"]
board = []
back = []
for y in range(8):
    board.append([0] * 8)
    back.append([0] * 8)


def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x / 80)
    my = int(e.y / 80)
    if mx > 7:
        mx = 7
    if my > 7:
        my = 7


def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False


# 計算黑棋與白棋各有幾顆
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK:
                b += 1
            if board[y][x] == WHITE:
                w += 1
    return b, w


# 電腦的思考邏輯
def save():
    for y in range(8):
        for x in range(8):
            back[y][x] = board[y][x]


def load():
    for y in range(8):
        for x in range(8):
            board[y][x] = back[y][x]


def uchiau(iro):
    while True:
        if uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            break
        iro = 3 - iro
        if uteru_masu(iro) == True:
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if kaeseru(x, y, iro) > 0:
                    ishi_utsu(x, y, iro)
                    break


def computer_2(iro, loops):
    global msg
    win = [0] * 64
    save()
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                msg += "."
                banmen()
                win[x + y * 8] = 1
                for i in range(loops):
                    ishi_utsu(x, y, iro)
                    uchiau(iro)
                    b, w = ishino_kazu()
                    if iro == BLACK and b > w:
                        win[x + y * 8] += 1
                    if iro == WHITE and w > b:
                        win[x + y * 8] += 1
                    load()
    m = 0
    n = 0
    for i in range(64):
        if win[i] > m:
            m = win[i]
            n = i
    x = n % 8
    y = int(n / 8)
    return x, y


def main():
    global mc, proc, turn, msg, space
    banmen()
    if proc == 0:  # 標題畫面
        msg = "先手、後手を選んでください"
        cvs.create_text(320, 200, text="Reversi", fill="gold", font=FL)
        cvs.create_text(160, 440, text="先手(黒)", fill="lime", font=FS)
        cvs.create_text(480, 440, text="後手(白)", fill="lime", font=FS)
        if mc == 1:  # 點選視窗
            mc = 0
            if (mx == 1 or mx == 2) and my == 5:
                ban_syokika()
                color[0] = BLACK
                color[1] = WHITE
                turn = 0
                proc = 1
            if (mx == 5 or mx == 6) and my == 5:
                ban_syokika()
                color[0] = WHITE
                color[1] = BLACK
                turn = 1
                proc = 1
    elif proc == 1:  # 顯示換誰下棋的訊息
        msg = "換您下棋"
        if turn == 1:
            msg = "電腦  思考中."
        proc = 2
    elif proc == 2:  # 決定落子的位置
        if turn == 0:  # 玩家
            if mc == 1:
                mc = 0
                if kaeseru(mx, my, color[turn]) > 0:
                    ishi_utsu(mx, my, color[turn])
                    space -= 1
                    proc = 3
        else:  # 電腦
            MONTE = [300, 300, 240, 180, 120, 60, 1]
            cx, cy = computer_2(color[turn], MONTE[int(space / 10)])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc == 3:  # 換邊下棋
        msg = ""
        turn = 1 - turn
        proc = 4
    elif proc == 4:  # 確認有沒有可以落子的棋格
        if space == 0:
            proc = 5
        elif uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            tk.messagebox.showinfo("", "雙方皆無處落子，對奕結束")
            proc = 5
        elif uteru_masu(color[turn]) == False:
            tk.messagebox.showinfo("", who[turn] + "沒有可落子之處，換邊下棋")
            proc = 3
        else:
            proc = 1
    elif proc == 5:  # 判斷勝負
        b, w = ishino_kazu()
        tk.messagebox.showinfo("對奕結束", "黑={}、白={}".format(b, w))
        if (color[0] == BLACK and b > w) or (color[0] == WHITE and w > b):
            tk.messagebox.showinfo("", "玩家獲勝！")
        elif (color[1] == BLACK and b > w) or (color[1] == WHITE and w > b):
            tk.messagebox.showinfo("", "電腦獲勝！")
        else:
            tk.messagebox.showinfo("", "平手")
        proc = 0
    root.after(100, main)


root = tk.Tk()
root.title("黑白棋8")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python遊戲開發講座_演算法篇\Chapter8\reversi_auto.py
print("黑白棋9")

import tkinter.messagebox

score = [0] * 3  # 對奕結果
match = 0  # 對奕次數

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 60)
BLACK = 1
WHITE = 2
proc = 0
turn = 0
msg = ""
space = 0
color = [0] * 2
board = []
back = []
for y in range(8):
    board.append([0] * 8)
    back.append([0] * 8)


def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x * 80
            Y = y * 80
            cvs.create_rectangle(X, Y, X + 80, Y + 80, outline="black")
            if board[y][x] == BLACK:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="black", width=0)
            if board[y][x] == WHITE:
                cvs.create_oval(X + 10, Y + 10, X + 70, Y + 70, fill="white", width=0)
    cvs.update()


def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE


# 下棋，讓對手的棋子翻面
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break


# 計算在這個位置下棋，對手的棋子會有幾顆翻面
def kaeseru(x, y, iro):
    if board[y][x] > 0:
        return -1  # 不能落子的棋格
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx < 0 or sx > 7 or sy < 0 or sy > 7:
                    break
                if board[sy][sx] == 0:
                    break
                if board[sy][sx] == 3 - iro:
                    k += 1
                if board[sy][sx] == iro:
                    total += k
                    break
    return total


# 確認有沒有可以落子的棋格
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                return True
    return False


# 計算黑棋與白棋各有幾顆
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == BLACK:
                b += 1
            if board[y][x] == WHITE:
                w += 1
    return b, w


# 電腦的思考邏輯
def computer_0(iro):  # 隨機落子
    while True:
        rx = random.randint(0, 7)
        ry = random.randint(0, 7)
        if kaeseru(rx, ry, iro) > 0:
            return rx, ry


point = [
    [6, 2, 5, 4, 4, 5, 2, 6],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [4, 3, 3, 0, 0, 3, 3, 4],
    [5, 3, 3, 3, 3, 3, 3, 5],
    [2, 1, 3, 3, 3, 3, 1, 2],
    [6, 2, 5, 4, 4, 5, 2, 6],
]


def computer_1(iro):  # 選擇該優先落子的棋格
    sx = 0
    sy = 0
    p = 0
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0 and point[y][x] > p:
                p = point[y][x]
                sx = x
                sy = y
    return sx, sy


# 以蒙地卡羅演算法撰寫的思考邏輯
def save():
    for y in range(8):
        for x in range(8):
            back[y][x] = board[y][x]


def load():
    for y in range(8):
        for x in range(8):
            board[y][x] = back[y][x]


def uchiau(iro):
    while True:
        if uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            break
        iro = 3 - iro
        if uteru_masu(iro) == True:
            while True:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if kaeseru(x, y, iro) > 0:
                    ishi_utsu(x, y, iro)
                    break


def computer_2(iro, loops):
    global msg
    win = [0] * 64
    save()
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro) > 0:
                msg += "."
                banmen()
                win[x + y * 8] = 1
                for i in range(loops):
                    ishi_utsu(x, y, iro)
                    uchiau(iro)
                    b, w = ishino_kazu()
                    if iro == BLACK and b > w:
                        win[x + y * 8] += 1
                    if iro == WHITE and w > b:
                        win[x + y * 8] += 1
                    load()
    m = 0
    n = 0
    for i in range(64):
        if win[i] > m:
            m = win[i]
            n = i
    x = n % 8
    y = int(n / 8)
    return x, y


def main():
    global proc, turn, msg, space, match
    banmen()
    if proc == 0:  # 標題畫面
        cvs.create_text(320, 200, text="Reversi AUTO", fill="gold", font=FL)
        ban_syokika()
        color[0] = BLACK
        color[1] = WHITE
        turn = 0
        proc = 1
    elif proc == 1:  # 顯示換誰下棋的訊息
        msg = "演算法 " + str(turn) + " 思考中"
        proc = 2
    elif proc == 2:  # 決定落子的棋格
        if turn == 0:  # 演算法 先攻
            cx, cy = computer_1(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
        else:  # 演算法 後攻
            cx, cy = computer_2(color[turn], 30)
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc == 3:  # 換邊下棋
        msg = ""
        turn = 1 - turn
        proc = 4
    elif proc == 4:  # 確認有沒有可以落子的棋格
        if space == 0:
            proc = 5
        elif uteru_masu(BLACK) == False and uteru_masu(WHITE) == False:
            msg = "雙方皆無處落子，對奕結束"
            proc = 5
        elif uteru_masu(color[turn]) == False:
            msg = "COM" + str(turn) + "沒有可落子之處，換邊下棋"
            proc = 3
        else:
            proc = 1
    elif proc == 5:  # 判斷勝負
        b, w = ishino_kazu()
        if (color[0] == BLACK and b > w) or (color[0] == WHITE and w > b):
            score[0] += 1
        elif (color[1] == BLACK and b > w) or (color[1] == WHITE and w > b):
            score[1] += 1
        else:
            score[2] += 1

        # 顯示結果
        match += 1
        print("--------------------")
        print("對奕次數", match)
        print("黑", b, "　白", w)
        print("COM(先攻) WIN", score[0])
        print("COM(後攻) WIN", score[1])
        print("DRAW", score[2])
        if match % 100 == 0:
            tk.messagebox.showinfo("", "每對奕100次，程式就暫停執行")
        proc = 0
    root.after(0, main)  # 演算法的對戰 將100msec設定為1msec


root = tk.Tk()
root.title("黑白棋9")
root.resizable(False, False)
cvs = tk.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
