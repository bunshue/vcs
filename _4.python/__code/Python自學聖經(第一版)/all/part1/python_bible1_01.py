"""
Python自學聖經(第二版)

"""

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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

# ch01\loop.py

sum = 0


def show(n):
    print("第 " + str(n) + " 次執行迴圈")


for i in range(1, 11):
    show(i)
    sum += i
print("1+2+...+10 = " + str(sum))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# ch02\format.py

print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%-2d   " % (i, j, product), end="")
    print()

print("------------------------------------------------------------")  # 60個

# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個


listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0, 3):
    print(
        listname[i].ljust(5),
        str(i + 1).rjust(3),
        str(listchinese[i]).rjust(5),
        str(listmath[i]).rjust(5),
        str(listenglish[i]).rjust(5),
    )

print("------------------------------------------------------------")  # 60個

import time as t

week = [" 一", " 二", " 三", " 四", " 五", " 六", " 日"]
dst = [" 無日光節約時間", " 有日光節約時間"]
time1 = t.localtime()
show = " 現在時刻：中華民國 " + str(int(time1.tm_year) - 1911) + " 年 "
show += str(time1.tm_mon) + " 月 " + str(time1.tm_mday) + " 日 "
show += str(time1.tm_hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒 星期" + week[time1.tm_wday] + "\n"
show += " 今天是今年的第 " + str(time1.tm_yday) + " 天，此地" + dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

# ch05\randint.py

import random as r

while True:
    inkey = input("按任意鍵再按[ENTER]鍵擲骰子，直接按[ENTER]鍵結束:")
    if len(inkey) > 0:
        num = r.randint(1, 6)
        print("你擲的骰子點數為：" + str(num))
    else:
        print("遊戲結束！")
        break

print("------------------------------------------------------------")  # 60個

# ch05\replace.py

date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# ch05\spenttime.py

import time

start = time.time()  # 開始執行時間
print("開始時間：{}".format(start))
for i in range(100):
    time.sleep(0.001)
end = time.time()  # 結束執行時間
print("結束時間：{}".format(end))
print("使用時間：%7.3f 秒" % (end - start))

print("------------------------------------------------------------")  # 60個

import msvcrt


def pwd_input():
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("請在cmd命令行下執行，否則密碼輸入將無法隱藏:")
        if newChar in "\r\n":  # 如果是換行，结束輸入
            break
        elif newChar == "\b":  # 如果是退格，删除密碼末尾一位並且删除一個星號
            if chars:
                del chars[-1]
                msvcrt.putch("\b".encode(encoding="utf-8"))  # 游標退回一格
                msvcrt.putch(" ".encode(encoding="utf-8"))  # 输出一個空格覆蓋原來的星號
                msvcrt.putch("\b".encode(encoding="utf-8"))  # 游標退回一格準備接受新的输入
        else:
            chars.append(newChar)
            msvcrt.putch("*".encode(encoding="utf-8"))  # 顯示 * 號
    return "".join(chars)


print("------------------------------------------------------------")  # 60個


def CheckSpeed(speed):  # 檢查速度
    if speed < 70:
        raise Exception("速度太慢了!")  # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!")  # 拋出 Exception 型別例外


for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)  # 檢查速度
    except Exception as e:  # 接收 Exception的例外
        print("現在速度：{}，{}".format(speed, e))
    else:
        print("目前時速：{}".format(speed))

print("------------------------------------------------------------")  # 60個

# ch07\raise2.py


class MyException(RuntimeError):
    def __init__(self, arg):
        self.args = arg


def CheckSpeed(speed):  # 檢查速度
    if speed < 70:
        raise Exception("速度太慢了!")  # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!")  # 拋出 Exception 型別例外
    else:
        raise MyException("快樂駕駛，平安返家!")  # 拋出 MyException 型別例外


def convertTuple(tup):  # tuple 轉換為字串
    str = "".join(tup)
    return str


for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)  # 檢查速度
    except MyException as e:  # 接收 MyException 的例外
        err = convertTuple(e.args)  # tuple 轉換為串字
        print("目前時速：{}，{}".format(speed, err))
    except Exception as e:  # 接收 Exception 的例外
        print("現在速度：{}，{}".format(speed, e))

print("------------------------------------------------------------")  # 60個

# ch07\Traceback.py

import traceback


def CheckSpeed(speed):  # 檢查速度
    if speed < 70:
        raise Exception("速度太慢了!")  # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!")  # 拋出 Exception 型別例外


for speed in (60, 100, 150):
    try:
        CheckSpeed(speed)  # 檢查速度
    except Exception as e:  # 接收 Exception的例外
        with open("tmp_error_message.txt", "a") as f:
            f.write(traceback.format_exc())  # 寫入例外過程
        print("錯誤資訊寫入完成!")
    else:
        print("目前時速：{}".format(speed))

print("------------------------------------------------------------")  # 60個

# ch08\bracket.py

import re

pat = r"[0-9+]+"
s = "Amy was 18 year old,she likes Python and C++."
m = re.findall(pat, s)
print(m)  # ['18', '++']

print("------------------------------------------------------------")  # 60個

# ch08\compile.py

import re

reobj = re.compile(r"[a-z]+")
m = reobj.findall("3tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\dotall.py

import re

pat = r".*"
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group())  # Do your best,
m2 = re.search(r".*", s, re.DOTALL)
print(m2.group())  # Do your best,\nGo Go Go!

print("------------------------------------------------------------")  # 60個

# ch08\findall.py

import re

pat = re.compile("[a-z]+")
m = pat.findall("tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\ignore.py

import re

pat = r"PYTHON|ANDROID"
s = "I like Python and Android!"
m = re.findall(pat, s, re.I)
print(m)  # ['Python', 'Android']

print("------------------------------------------------------------")  # 60個

# ch08\match.py

import re

pat = re.compile(r"[a-z]+")

m = pat.match("tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0,3)

print("------------------------------------------------------------")  # 60個

# ch08\not1.py

import re

pat = r"[^a-z. ]+"
s = "John was 18 year old."
m = re.findall(pat, s)
print(m)  # ['J', '18']

print("------------------------------------------------------------")  # 60個

# ch08\not2.py

import re

pat = r"^\d+"
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m)  # ['2020']
m2 = re.findall(r"\w+$", s)
print(m2)  # ['soon']

print("------------------------------------------------------------")  # 60個

# ch08\phone_check.py


def isTaiwanPhone(str):
    if len(str) != 11:  # 如果長度不是11
        return False  # 傳回非手機號碼格式
    # 檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != "-":  # 如果第5個字元不是'-'字元
                return False  # 傳回非手機號碼格式
        else:  # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False  # 傳回非手機號碼格式
    return True  # 傳回是正確手機號碼格式


print("0937-123456 是台灣手機號碼：", isTaiwanPhone("0937-123456"))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone("02-12345678"))

print("------------------------------------------------------------")  # 60個

# ch08\phone1.py

import re

numStr = "tel:04-12345678"
pat = r"(\d{2})-(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # 04-12345678
    print(phone.group(0))  # 04-12345678
    print(phone.group(1))  # 04
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# ch08\phone2.py

import re

numStr = "tel:(04)12345678"
pat = r"(\(\d{2}\))(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # (04)12345678
    print(phone.group(1))  # (04)
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# ch08\phone3.py

import re

phoneList = ["(04)12345678", "(04)-12345678"]
pat = r"(\(\d{2}\))-?(\d{8})"

for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\phone4.py

import re

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}"
for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\plus.py

import re

pat = re.compile(r"[aeiou]+")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)  # ['o', 'i', 'e', 'ie']

print("------------------------------------------------------------")  # 60個

# ch08\re_findall.py

import re

m = re.findall(r"[a-z]+", "tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch08\re_match.py

import re

pat = r"[a-z]+"
m = re.match(pat, "tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch08\re_search.py

import re

pat = "[a-z]+"
m = re.search(pat, "3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch08\re_verbose.py

import re

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"""
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
"""

for phone in phoneList:
    phoneNum = re.search(pat, phone, re.VERBOSE)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch08\regex.py

html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
"""

import re

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
for email in emails:  # 顯示 email
    print(email)

price = re.findall(r"[\d]+元", html)[0].split("元")[0]  # 價格
print(price)  # 顯示定價金額

imglist = re.findall(r"[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+", html)
for img in imglist:  #
    print(img)  # 顯示圖片網址

phonelist = re.findall(r"\(?\d{2,4}\)?\-\d{6,8}", html)
for phone in phonelist:
    print(phone)  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

# ch08\search.py

import re

pat = re.compile("[a-z]+")

m = pat.search("3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())  # 4
    print(m.span())  # (1,4)

print("------------------------------------------------------------")  # 60個

# ch08\star.py

import re

pat = re.compile(r"[aeiou]*")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)

print("------------------------------------------------------------")  # 60個

# ch08\sub1.py

import re

pat = r"\d+"
substr = "*"
s = "Password:1234,ID:5678"
result = re.sub(pat, substr, s)
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# ch08\sub2.py

import re


def multiply(m):
    v = int(m.group())
    return str(v * 2)


result = re.sub("\d+", multiply, "10 20 30 40 50", 3)
print(result)  # 20 40 60 40 50

print("------------------------------------------------------------")  # 60個

# ch08\wild.py

import re

pat = r".o"
s = "Do your best!"
m = re.findall(pat, s)
print(m)  # ['Do', 'yo']
m2 = re.findall(r".*o", s)
print(m2)  # ['Do yo']

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def click1():
    textvar.set("我已經被按過了！")


import tkinter as tk

win = tk.Tk()
textvar = tk.StringVar()
button1 = tk.Button(win, textvariable=textvar, command=click1)
textvar.set("按鈕")
button1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkbutton2.py


def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if btntext.get() == "按我！":
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")


import tkinter as tk

win = tk.Tk()
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()
button1 = tk.Button(win, textvariable=btntext, command=clickme)
btntext.set("按我！")
button1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkcheckbox1.py


def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if choice[i].get() == 1:
            str = str + ball[i] + " "
    msg.set(str)


import tkinter as tk

win = tk.Tk()
choice = []
ball = ["足球", "籃球", "棒球"]
msg = tk.StringVar()
label = tk.Label(win, text="選擇喜歡的球類運動：")
label.pack()
for i in range(0, len(ball)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(win, text=ball[i], variable=choice[i], command=choose)
    item.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkframe1.py

import tkinter as tk

win = tk.Tk()
frame1 = tk.Frame(win)
frame1.pack()
label1 = tk.Label(frame1, text="標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
frame2 = tk.Frame(win)
frame2.pack()
button1 = tk.Button(frame2, text="確定")
button2 = tk.Button(frame2, text="取消")
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkgrid1.py

import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = tk.Button(win, text="這是按鈕五", width=20)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = tk.Button(win, text="這是按鈕六", width=20)
button6.grid(row=1, column=2, padx=5, pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkgrid2.py

import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="e")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.grid(row=0, column=3, padx=5, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = tk.Button(win, text="這是按鈕五", width=20)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = tk.Button(win, text="這是按鈕六", width=20)
button6.grid(row=1, column=2, padx=5, pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tklabel1.py

import tkinter as tk

win = tk.Tk()
label1 = tk.Label(
    win, text="這是標籤元件！", fg="red", bg="yellow", font=("新細明體", 12), padx=20, pady=10
)
label1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkpack1.py

import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack()
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack()
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack()
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkpack2.py

import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5)
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkpack3.py

import tkinter as tk

win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5, side="right")
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5, side="left")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5, side="bottom")
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkpassword.py


def checkPW():
    if pw.get() == "1234":
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")


import tkinter as tk

win = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼：")
label.pack()
entry = tk.Entry(win, textvariable=pw)
entry.pack()
button = tk.Button(win, text="登入", command=checkPW)
button.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkplace1.py

import tkinter as tk

win = tk.Tk()
win.geometry("300x100")
label1 = tk.Label(win, text="輸入成績：")
label1.place(x=20, y=20)
score = tk.StringVar()
entryUrl = tk.Entry(win, textvariable=score)
entryUrl.place(x=90, y=20)
btnDown = tk.Button(win, text="計算成績")
btnDown.place(x=80, y=50)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkplace2.py

import tkinter as tk

win = tk.Tk()
win.geometry("400x150")
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.place(relx=0.5, rely=0.5, anchor="center")
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.place(relx=0.1, rely=0.1, anchor="nw")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.place(relx=0.1, rely=0.8, anchor="w")
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tkradio1.py


def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())


import tkinter as tk

win = tk.Tk()
choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(win, text="足球", value="足球", variable=choice, command=choose)
item1.pack()
item2 = tk.Radiobutton(win, text="籃球", value="籃球", variable=choice, command=choose)
item2.pack()
item3 = tk.Radiobutton(win, text="棒球", value="棒球", variable=choice, command=choose)
item3.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
item1.select()
choose()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch10\tktext1.py

import tkinter as tk

win = tk.Tk()
text = tk.Text(win)
text.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text.insert(tk.END, "不需另外安裝即可使用。")
text.pack()
text.config(state=tk.DISABLED)
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch11\bs1.py

import requests
from bs4 import BeautifulSoup

url = "http://www.ehappy.tw/bsdemo1.htm"
html = requests.get(url)
html.encoding = "UTF-8"
sp = BeautifulSoup(html.text, "html.parser")

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)

print("------------------------------------------------------------")  # 60個

# ch11\bs2.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.find("p"))
print(sp.find_all("p"))
print(sp.find("p", {"id": "p2", "class": "red"}))
print(sp.find("p", id="p2", class_="red"))

print("------------------------------------------------------------")  # 60個

# ch11\bs3.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.select("title"))
print(sp.select("p"))
print(sp.select("#p1"))
print(sp.select(".red"))

print("------------------------------------------------------------")  # 60個

# ch11\bs4.py

from bs4 import BeautifulSoup

html = """
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
"""
sp = BeautifulSoup(html, "html.parser")
print(sp.select("img")[0].get("src"))
print(sp.select("a")[0].get("href"))
print(sp.select("img")[0]["src"])
print(sp.select("a")[0]["href"])

print("------------------------------------------------------------")  # 60個

# ch11\bs5.py

html = """
<html><head><title>網頁標題</title></head>
<h1>文件標題</h1>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
"""

from bs4 import BeautifulSoup

sp = BeautifulSoup(html, "html.parser")

print(sp.title)  # <title>網頁標題</title>

print(sp.find("h1"))  # <h1>文件標題</h1>

print(sp.find_all("a"))
print(sp.find_all("a", {"class": "red"}))

data1 = sp.find("a", {"href": "http://example.com/one"})
print(data1.text)  # First

data2 = sp.select("#link1")
print(data2[0].text)  # First
print(data2[0].get("href"))  # http://example.com/one
print(data2[0]["href"])  # http://example.com/one

print(sp.find_all(["title", "h1"]))  # [<title>網頁標題</title>, <h1>文件標題</h1>]

print(sp.select("div img")[0]["src"])  # http://example.com/three.jpg


print("------------------------------------------------------------")  # 60個

# ch11\get.py

import requests

url = "http://www.ehappy.tw/demo.htm"
r = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if r.status_code == requests.codes.ok:
    print(r.text)

print("------------------------------------------------------------")  # 60個

# ch11\get_cookie.py

import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 設定cookies的值
cookies = {"over18": "1"}
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

# ch11\get_headers.py

import requests

url = "https://irs.thsrc.com.tw/IMINT/"
# 自訂表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}
# 自訂表頭
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
# 將自訂表頭加入 GET 請求中
r = requests.get(url, headers=headers)
print(r)

print("------------------------------------------------------------")  # 60個

# ch11\iplookup.py

import requests

# 設定查詢目前IP的api網址
url = "https://api.ipify.org"
r = requests.get(url)

print("我目前的IP是：", r.text)

print("------------------------------------------------------------")  # 60個

# ch11\loginFacebook.py

from selenium import webdriver

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個

# ch11\loginFacebook2.py

from selenium import webdriver

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options=chrome_options)
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

listx = [1, 2, 3, 4, 5]

listy1 = [15, 50, 80, 40, 70]
plt.axes([0.1, 0, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy1, "r-s")

listy2 = [80, 20, 60, 50, 20]
plt.axes([1, 0, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy2, "g--o")

plt.axes([0.1, 1, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy1, "r-s")

plt.axes([1, 1, 0.8, 0.8])
plt.ylim(0, 100)
plt.plot(listx, listy2, "g--o")

plt.show()

# plt.rcParams['figure.figsize'] = [10, 10]
# plt.rcParams['figure.dpi'] = 72
# plt.rcParams.keys

print("------------------------------------------------------------")  # 60個

# ch13\subplot1.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(211)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(212)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot2.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(121)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(122)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot3.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 8])
plt.subplot(221)
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.subplot(222)
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.subplot(223)
plt.title(label="Chart 3")
plt.plot([1, 2, 3], "b:o")

plt.subplot(224)
plt.title(label="Chart 4")
plt.plot([1, 2, 3], "y--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot4.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 4])
plt.axes([0, 0, 0.4, 1])
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.axes([0.5, 0, 0.4, 1])
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot5.py

import matplotlib.pyplot as plt

plt.figure(figsize=[8, 4])
plt.axes([0, 0, 0.8, 1])
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.axes([0.55, 0.1, 0.2, 0.2])
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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
