"""
python_game02.py

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
'''
# air_hockey.py

FNT = ("Times New Roman", 60)
mx = 0
my = 0
mc = 0
proc = 0
tmr = 0
you_x = 750
you_y = 300
you_vx = 0
you_vy = 0
com_x = 250
com_y = 300
com_vx = 0
com_vy = 0
pu_x = 500
pu_y = 300
pu_vx = 10
pu_vy = 5
level = 0
point_you = 0
point_com = 0
POINT_WIN = 5
goal = [0, 0]


def click(e):
    global mc
    mc = 1


def move(e):
    global mx, my
    mx = e.x
    my = e.y


def draw_table():
    cvs.delete("all")
    for i in range(2):
        if goal[i] > 0:
            goal[i] -= 1
            if goal[i] % 2 == 0:
                cvs.create_rectangle(980 * i, 180, 980 * i + 20, 420, fill="yellow")
    cvs.create_image(500, 300, image=img_table)
    cvs.create_image(pu_x, pu_y, image=img_puck)
    cvs.create_image(you_x, you_y, image=img_sma_b)
    cvs.create_image(com_x, com_y, image=img_sma_r)
    cvs.create_text(
        500, 40, text=str(point_com) + " - " + str(point_you), font=FNT, fill="white"
    )
    if proc == 0:
        cvs.create_image(500, 160, image=img_title)
        cvs.create_text(250, 440, text="Normal", font=FNT, fill="lime")
        cvs.create_text(750, 440, text="Hard", font=FNT, fill="gold")
    if proc == 2:
        if point_you == POINT_WIN:
            cvs.create_text(
                1000 - tmr * 10, 300, text="YOU WIN!", font=FNT, fill="cyan"
            )
        else:
            cvs.create_text(tmr * 10, 300, text="COM WIN!", font=FNT, fill="red")


def smasher_you():
    global you_x, you_y, you_vx, you_vy
    you_vx = mx - you_x
    you_vy = my - you_y
    you_x = mx
    you_y = my


def smasher_com():
    global com_x, com_y, com_vx, com_vy
    dots = 20 + level * 10
    x = com_x
    y = com_y
    if get_dis(com_x, com_y, pu_x, pu_y) < 50 * 50:
        com_x -= dots
    elif pu_vx < 4 and com_x < 900:
        if com_y < pu_y - dots:
            com_y += dots
        if com_y > pu_y + dots:
            com_y -= dots
        if com_x < pu_x - dots:
            com_x += dots
        if com_x > pu_x + dots:
            com_x -= dots
    else:
        com_x += (60 - com_x) / (16 - level * 6)
        com_y += (300 - com_y) / (16 - level * 6)
    com_vx = com_x - x
    com_vy = com_y - y


def puck_comeout():
    global pu_x, pu_y, pu_vx, pu_vy
    pu_x = 500
    pu_y = 0
    pu_vx = 0
    pu_vy = 20


def puck():
    global pu_x, pu_y, pu_vx, pu_vy
    r = 20  # 碟盤的半徑
    pu_x += pu_vx
    pu_y += pu_vy
    if pu_y < r and pu_vy < 0:
        pu_vy = -pu_vy
    if pu_y > 600 - r and pu_vy > 0:
        pu_vy = -pu_vy
    if pu_x < r and pu_vx < 0:
        pu_vx = -pu_vx
    if pu_x > 1000 - r and pu_vx > 0:
        pu_vx = -pu_vx
    if pu_y < 0:
        pu_y = 0
    if pu_y > 600:
        pu_y = 600
    if pu_x < 0:
        pu_x = 0
    if pu_x > 1000:
        pu_x = 1000
    pu_vx = pu_vx * 0.95
    pu_vy = pu_vy * 0.95
    if get_dis(pu_x, pu_y, you_x, you_y) < 50 * 50:
        pu_vx = you_vx * 1.2
        pu_vy = you_vy * 1.2
    if get_dis(pu_x, pu_y, com_x, com_y) < 50 * 50:
        pu_vx = com_vx * 1.2
        pu_vy = com_vy * 1.2


def get_dis(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def judge():
    global point_you, point_com
    if pu_x < 20 and 200 < pu_y and pu_y < 400:
        point_you += 1
        goal[0] = 60
        return True
    if pu_x > 980 and 200 < pu_y and pu_y < 400:
        point_com += 1
        goal[1] = 60
        return True
    return False


def main():
    global mc, proc, tmr, level, point_you, point_com
    tmr += 1
    draw_table()
    if proc == 0 and mc == 1:  # 標題畫面
        mc = 0
        level = 0
        if mx > 500:
            level = 1
        point_you = 0
        point_com = 0
        puck_comeout()
        proc = 1
    if proc == 1:  # 遊戲進行中
        puck()
        smasher_you()
        smasher_com()
        if judge() == True:
            puck_comeout()
            if point_you == POINT_WIN or point_com == POINT_WIN:
                proc = 2
                tmr = 0
    if proc == 2 and tmr == 100:  # 勝負結果
        mc = 0
        proc = 0
    root.after(33, main)


root = tk.Tk()
img_title = tk.PhotoImage(file="title.png")
img_table = tk.PhotoImage(file="table.png")
img_puck = tk.PhotoImage(file="puck.png")
img_sma_r = tk.PhotoImage(file="smasher_r.png")
img_sma_b = tk.PhotoImage(file="smasher_b.png")
root.title("Python☆冰上曲棍球")
root.resizable(False, False)
root.bind("<Button>", click)
root.bind("<Motion>", move)
cvs = tk.Canvas(width=1000, height=600, bg="black")
cvs.pack()
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# list6_4.py

img = [None] * 14
card = [0] * 26
face = [0] * 26


def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 7) * 120 + 60
        y = int(i / 7) * 168 + 84
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        if face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])


def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]


def click(e):
    x = int(e.x / 120)
    y = int(e.y / 168)
    if 0 <= x and x <= 6 and 0 <= y and y <= 3:
        n = x + y * 7
        if n >= 26:
            return
        if face[n] == 0:
            face[n] = 1
        else:
            face[n] = 0
        draw_card()


root = tk.Tk()
root.title("翻牌配對遊戲2")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    img[i] = tk.PhotoImage(file="card/" + str(i) + ".png")
shuffle_card()
draw_card()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# list6_5.py

img = [None] * 14
card = [0] * 26
face = [0] * 26
proc = 0
tmr = 0
sel1 = 0
sel2 = 0


def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 7) * 120 + 60
        y = int(i / 7) * 168 + 84
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        if face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])


def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]


def click(e):
    global proc, tmr, sel1, sel2
    x = int(e.x / 120)
    y = int(e.y / 168)
    if 0 <= x and x <= 6 and 0 <= y and y <= 3:
        n = x + y * 7
        if n >= 26:
            return
        if face[n] == 0:
            if proc == 1:
                face[n] = 1
                sel1 = n
                proc = 2
            elif proc == 2:
                face[n] = 1
                sel2 = n
                proc = 3
                tmr = 0


def main():
    global proc, tmr
    tmr += 1
    draw_card()
    if proc == 0:
        shuffle_card()
        proc = 1
    if proc == 1:
        cvs.create_text(780, 580, text="請翻第1張撲克牌")
    if proc == 2:
        cvs.create_text(780, 580, text="請翻第2張撲克牌")
    if proc == 3 and tmr == 5:  # 判斷兩張撲克牌是否一致
        if card[sel1] == card[sel2]:
            face[sel1] = 2
            face[sel2] = 2
        else:
            face[sel1] = 0
            face[sel2] = 0
        proc = 1
    root.after(200, main)


root = tk.Tk()
root.title("翻牌配對遊戲3")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    img[i] = tk.PhotoImage(file="card/" + str(i) + ".png")
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# list6_6.py

img = [None] * 14
card = [0] * 26
face = [0] * 26
proc = 0
tmr = 0
sel1 = 0
sel2 = 0
you = 0
com = 0


def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 7) * 120 + 60
        y = int(i / 7) * 168 + 84
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        if face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])


def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]


def click(e):
    global proc, tmr, sel1, sel2
    x = int(e.x / 120)
    y = int(e.y / 168)
    if 0 <= x and x <= 6 and 0 <= y and y <= 3:
        n = x + y * 7
        if n >= 26:
            return
        if face[n] == 0:
            if proc == 1:
                face[n] = 1
                sel1 = n
                proc = 2
            elif proc == 2:
                face[n] = 1
                sel2 = n
                proc = 3
                tmr = 0


def main():
    global proc, tmr, sel1, sel2, you, com
    tmr += 1
    draw_card()
    if proc == 0:
        shuffle_card()
        proc = 1
    if proc == 1:
        cvs.create_text(780, 580, text="請翻第1張撲克牌")
    if proc == 2:
        cvs.create_text(780, 580, text="請翻第2張撲克牌")
    if proc == 3 and tmr == 15:  # 判斷兩張撲克牌是否一致
        if card[sel1] == card[sel2]:
            face[sel1] = 2
            face[sel2] = 2
            you += 2
            proc = 1
            if you + com == 26:
                proc = 7
        else:
            face[sel1] = 0
            face[sel2] = 0
            proc = 4
        tmr = 0
    if proc == 4 and tmr == 5:  # 電腦翻第1張撲克牌
        sel1 = random.randint(0, 25)
        while face[sel1] != 0:
            sel1 = (sel1 + 1) % 26
        face[sel1] = 1
        proc = 5
        tmr = 0
    if proc == 5 and tmr == 5:  # 電腦翻第2張撲克牌
        sel2 = random.randint(0, 25)
        while face[sel2] != 0:
            sel2 = (sel2 + 1) % 26
        face[sel2] = 1
        proc = 6
        tmr = 0
    if proc == 6 and tmr == 15:  # 判斷兩張撲克牌是否一致
        if card[sel1] == card[sel2]:
            face[sel1] = 2
            face[sel2] = 2
            com += 2
            proc = 4
            if you + com == 26:
                proc = 7
        else:
            face[sel1] = 0
            face[sel2] = 0
            proc = 1
        tmr = 0
    if proc == 7:
        cvs.create_text(780, 580, text="遊戲結束")
    root.after(200, main)


root = tk.Tk()
root.title("翻牌配對遊戲4")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=960, height=672)
cvs.pack()
for i in range(14):
    img[i] = tk.PhotoImage(file="card/" + str(i) + ".png")
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個

# list6_7.py

img = [None] * 14
card = [0] * 26
face = [0] * 26
proc = 0
tmr = 0
sel1 = 0
sel2 = 0
you = 0
com = 0
FNT = ("Times New Roman", 36)


def draw_card():
    cvs.delete("all")
    for i in range(26):
        x = (i % 7) * 120 + 60
        y = int(i / 7) * 168 + 84
        if face[i] == 0:
            cvs.create_image(x, y, image=img[0])
        if face[i] == 1:
            cvs.create_image(x, y, image=img[card[i]])


def shuffle_card():
    for i in range(26):
        card[i] = 1 + i % 13
        face[i] = 0
    for i in range(100):
        r1 = random.randint(0, 12)
        r2 = random.randint(13, 25)
        card[r1], card[r2] = card[r2], card[r1]


def click(e):
    global proc, tmr, sel1, sel2, you, com
    if proc == 0:
        shuffle_card()
        you = 0
        com = 0
        proc = 1
        return
    x = int(e.x / 120)
    y = int(e.y / 168)
    if 0 <= x and x <= 6 and 0 <= y and y <= 3:
        n = x + y * 7
        if n >= 26:
            return
        if face[n] == 0:
            if proc == 1:
                face[n] = 1
                sel1 = n
                proc = 2
            elif proc == 2:
                face[n] = 1
                sel2 = n
                proc = 3
                tmr = 0


def main():
    global proc, tmr, sel1, sel2, you, com
    tmr += 1
    draw_card()
    if proc == 0 and tmr % 10 < 5:  # 等待遊戲開始
        cvs.create_text(780, 580, text="Click to start.", fill="green", font=FNT)
    if 1 <= proc and proc <= 3:
        cvs.create_rectangle(840, 60, 960, 200, fill="blue", width=0)
    cvs.create_text(900, 100, text="YOU", fill="silver", font=FNT)
    cvs.create_text(900, 160, text=you, fill="white", font=FNT)
    if 4 <= proc and proc <= 6:
        cvs.create_rectangle(840, 260, 960, 400, fill="red", width=0)
    cvs.create_text(900, 300, text="COM", fill="silver", font=FNT)
    cvs.create_text(900, 360, text=com, fill="white", font=FNT)
    if proc == 3 and tmr == 15:  # 判斷兩張撲克牌是否一致
        if card[sel1] == card[sel2]:
            face[sel1] = 2
            face[sel2] = 2
            you += 2
            proc = 1
            if you + com == 26:
                proc = 7
        else:
            face[sel1] = 0
            face[sel2] = 0
            proc = 4
        tmr = 0
    if proc == 4 and tmr == 5:  # 電腦翻第1張撲克牌
        sel1 = random.randint(0, 25)
        while face[sel1] != 0:
            sel1 = (sel1 + 1) % 26
        face[sel1] = 1
        proc = 5
        tmr = 0
    if proc == 5 and tmr == 5:  # 電腦翻第2張撲克牌
        sel2 = random.randint(0, 25)
        while face[sel2] != 0:
            sel2 = (sel2 + 1) % 26
        face[sel2] = 1
        proc = 6
        tmr = 0
    if proc == 6 and tmr == 15:  # 判斷兩張撲克牌是否一致
        if card[sel1] == card[sel2]:
            face[sel1] = 2
            face[sel2] = 2
            com += 2
            proc = 4
            if you + com == 26:
                proc = 7
        else:
            face[sel1] = 0
            face[sel2] = 0
            proc = 1
        tmr = 0
    if proc == 7:
        if you > com:
            cvs.create_text(780, 580, text="YOU WIN!", fill="skyblue", font=FNT)
        if com > you:
            cvs.create_text(780, 580, text="COM WIN!", fill="pink", font=FNT)
        if tmr == 25:
            proc = 0
    root.after(200, main)


root = tk.Tk()
root.title("翻牌配對遊戲5")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tk.Canvas(width=960, height=672, bg="black")
cvs.pack()
for i in range(14):
    img[i] = tk.PhotoImage(file="card/" + str(i) + ".png")
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = 300
y = 100
xp = 10


def animation():
    global x, xp
    x = x + xp
    if x <= 30:
        xp = 5
    if x >= 770:
        xp = -5
    cvs.delete("all")
    cvs.create_image(400, 200, image=bg)
    if xp < 0:
        cvs.create_image(x, y, image=ap1)
    if xp > 0:
        cvs.create_image(x, y, image=ap2)
    root.after(50, animation)


root = tk.Tk()
root.title("即時處理")
cvs = tk.Canvas(width=800, height=400)
cvs.pack()
ap1 = tk.PhotoImage(file="airplane1.png")
ap2 = tk.PhotoImage(file="airplane2.png")
bg = tk.PhotoImage(file="bg.png")
animation()
root.mainloop()

print("------------------------------------------------------------")  # 60個

COL = ["red", "orange", "yellow", "lime", "cyan", "blue", "violet"]
bc = 0
bx = 0
by = 0
mx = 0
my = 0


def click(e):
    global bc
    bc = bc + 1
    if bc == 7:
        bc = 0


def move(e):
    global mx, my
    mx = e.x
    my = e.y


def main():
    global bx, by
    if bx < mx:
        bx += 5
    if mx < bx:
        bx -= 5
    if by < my:
        by += 5
    if my < by:
        by -= 5
    cvs.delete("all")
    cvs.create_oval(bx - 40, by - 60, bx + 40, by + 60, fill=COL[bc])
    cvs.create_oval(bx - 30, by - 45, bx - 5, by - 20, fill="white", width=0)
    cvs.create_line(
        bx, by + 60, bx - 10, by + 100, bx + 10, by + 140, bx, by + 180, smooth=True
    )
    root.after(50, main)


root = tk.Tk()
root.title("即時讓氣球移動")
root.bind("<Button>", click)
root.bind("<Motion>", move)
cvs = tk.Canvas(width=900, height=600, bg="skyblue")
cvs.pack()
main()
root.mainloop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
f = ("Times New Roman", 100)
n = 0
running = False

def counter():
    global n
    n = n + 1
    cvs.delete("all")
    cvs.create_text(300, 200, text=n, font=f, fill="blue")
    root.after(1000, counter)


root = tk.Tk()
root.title("即時處理")
cvs = tk.Canvas(width=640, height=480, bg="white")
cvs.pack()

def timer_start():
    global running
    if running == False:
        button2a.config(bg="blue")


button2a = tk.Button(
    root, text="啟動", width=28, height=3, command=timer_start
)
button2a.pack()

counter()
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
