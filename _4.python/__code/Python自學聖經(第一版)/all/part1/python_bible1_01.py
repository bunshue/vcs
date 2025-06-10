"""
Python自學聖經(第一版)

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

# ch01\sum.py

a = 12
b = 34
sum = a + b
print("總和 = " + str(sum))

print("------------------------------------------------------------")  # 60個

# ch02\discount.py

money = int(input("請輸入購物金額："))
if money >= 10000:
    if money >= 100000:
        print(money * 0.8, end=" 元\n")  # 八折
    elif money >= 50000:
        print(money * 0.85, end=" 元\n")  # 八五折
    elif money >= 30000:
        print(money * 0.9, end=" 元\n")  # 九折
    else:
        print(money * 0.95, end=" 元\n")  # 九五折
else:
    print(money, end=" 元\n")  # 未打折

print("------------------------------------------------------------")  # 60個

# ch02\format.py

print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

print("------------------------------------------------------------")  # 60個

# ch02\grade.py

score = int(input("請輸入成績："))
if (score) >= 90:
    print("優等")
elif (score) >= 80:
    print("甲等")
elif (score) >= 70:
    print("乙等")
elif (score) >= 60:
    print("丙等")
else:
    print("丁等")

print("------------------------------------------------------------")  # 60個

# ch02\password1.py

pw = input("請輸入密碼：")
if pw == "1234":
    print("歡迎光臨！")

print("------------------------------------------------------------")  # 60個

# ch02\password2.py

pw = input("請輸入密碼：")
if pw == "1234":
    print("歡迎光臨！")
else:
    print("密碼錯誤！")

print("------------------------------------------------------------")  # 60個

# ch02\score.py

nat = input("請輸入國文成績：")
math = input("請輸入數學成績：")
eng = input("請輸入英文成績：")
sum = int(nat) + int(math) + int(eng)  # 輸入值需轉換為整數
average = sum / 3
print("成績總分：%d，平均成績：%5.2f" % (sum, average))

print("------------------------------------------------------------")  # 60個

# ch03\append1.py

score = []
total = inscore = 0
while inscore != -1:
    inscore = int(input("請輸入學生的成績："))
    score.append(inscore)
print("共有 %d 位學生" % (len(score) - 1))
for i in range(0, len(score) - 1):
    total += score[i]
average = total / (len(score) - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

# ch03\floor.py

n = int(input("請輸入大樓的樓層數："))
print("本大樓具有的樓層為：")
if n > 3:
    n += 1
for i in range(1, n + 1):
    if i == 4:
        continue
    print(i, end=" ")
print()

print("------------------------------------------------------------")  # 60個

# ch03\list1.py

score = [85, 79, 93]
print("國文成績：%d 分" % score[0])
print("數學成績：%d 分" % score[1])
print("英文成績：%d 分" % score[2])

print("------------------------------------------------------------")  # 60個

# ch03\ninenine.py

for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%-2d   " % (i, j, product), end="")
    print()

print("------------------------------------------------------------")  # 60個

# ch03\numtotal.py

sum = 0
n = int(input("請輸入正整數："))
for i in range(1, n + 1):
    sum += i
print("1 到 %d 的整數和為 %d" % (n, sum))

print("------------------------------------------------------------")  # 60個

# ch03\prime.py

n = int(input("請輸入大於 1 的整數："))
if n == 2:
    print("2 是質數！")
else:
    for i in range(2, n):
        if n % i == 0:
            print("%d 不是質數！" % n)
            break
    else:
        print("%d 是質數！" % n)

print("------------------------------------------------------------")  # 60個

# ch03\while1.py

total = person = score = 0
while score != -1:
    person += 1
    total += score
    score = int(input("請輸入第 %d 位學生的成績：" % person))
average = total / (person - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

# ch04\dictget.py

dict1 = {"A": "內向穩重", "B": "外向樂觀", "O": "堅強自信", "AB": "聰明自然"}
name = input("輸入要查詢的血型:")
blood = dict1.get(name)
if blood == None:
    print("沒有「" + name + "」血型！")
else:
    print(name + " 血型的個性為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

# ch04\enumerate.py

langs = {"Python", "Java", "Kotlin"}
enum_langs = enumerate(langs)  # 轉換為 enumerate 物件
print(type(enum_langs))  # <class 'enumerate'>

# 轉成串列
print(list(enum_langs))  # [(0, 'Python'), (1, 'Kotlin'), (2, 'Java')]
# 以迴圈輸出
for item in enumerate(langs):
    print(item)

for i, item in enumerate(langs):
    print(i, item)

print("------------------------------------------------------------")  # 60個

# ch04\in.py

dict1 = {"林小明": 85, "曾山水": 93, "鄭美麗": 67}
name = input("輸入學生姓名：")
if name in dict1:
    print(name + "的成績為 " + str(dict1[name]))
else:
    score = int(input("輸入學生分數："))
    dict1[name] = score
    print("字典內容：" + str(dict1))

print("------------------------------------------------------------")  # 60個

# ch04\item.py

dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
item1 = list(dict1.items())
for name, num in item1:
    print("得到的 %s 數目為 %d 面" % (name, num))

print("------------------------------------------------------------")  # 60個

# ch04\keyvalue.py

dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))

print("------------------------------------------------------------")  # 60個

# ch04\set.py

persons = ["林小明", "曾山水", "鄭美麗", "林小明", "曾山水", "林小明"]
s = set(persons)  # 串列轉集合
print(s)  # {'林小明', '曾山水', '鄭美麗'}
list1 = list(s)  # 集合轉串列
print(list1)  # ['林小明', '曾山水', '鄭美麗']
print(list1[0])  # 林小明

print("------------------------------------------------------------")  # 60個

# ch05\ctof.py


def ctof(c):  # 攝氏轉華氏
    f = c * 1.8 + 32
    return f


inputc = float(input("請輸入攝氏溫度："))
print("華氏溫度為：%5.1f 度" % ctof(inputc))

print("------------------------------------------------------------")  # 60個

# ch05\divmod.py

person = int(input("請輸入學生人數: "))
apple = int(input("請輸入蘋果總數: "))
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

print("------------------------------------------------------------")  # 60個

# ch05\just.py

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

# ch05\localtime.py

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

# ch05\sample.py

import random as r

list1 = r.sample(range(1, 50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0, 6):
    if i == 5:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print("------------------------------------------------------------")  # 60個

# ch05\sorted.py

innum = 0
list1 = []
while innum != -1:
    innum = int(input("請輸入電費 (-1：結束)："))
    list1.append(innum)
list1.pop()
print("共輸入 %d 個數" % len(list1))
print("最多電費為：%d" % max(list1))
print("最少電費為：%d" % min(list1))
print("電費總和為：%d" % sum(list1))
print("電費由大到小排序為：{}".format(sorted(list1, reverse=True)))

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

# ch05\startswith.py

web = input("請輸入網址：")
if web.startswith("http://") or web.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")

print("------------------------------------------------------------")  # 60個

# ch07\Area.py


class Rectangle:  # 定義父類別
    def __init__(self, width, height):
        self.width = width  # 定義共用屬性
        self.height = height  # 定義共用屬性

    def area(self):  # 定義共用方法
        return self.width * self.height


class Triangle(Rectangle):  # 定義子類別
    def area2(self):  # 定義子類別的共用方法
        return (self.width * self.height) / 2


triangle = Triangle(5, 6)  # 建立 triangle 物件
print("矩形面積=", triangle.area())  # 30
print("三角形面積=", triangle.area2())  # 15

print("------------------------------------------------------------")  # 60個

# ch07\calculate.py


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


print("------------------------------------------------------------")  # 60個

# ch07\CallModule.py

from areapackage2.Rectangle import Rectangle
from areapackage2.Triangle import Triangle

triangle = Triangle(5, 6)  # 建立 triangle 物件
print("矩形面積=", triangle.area())  # 30
print("三角形面積=", triangle.area2())  # 15.0

print("------------------------------------------------------------")  # 60個

# ch07\class01.py


class Animal:  # 定義類別
    name = "小鳥"  # 定義屬性

    def sing(self):  # 定義方法
        print("很會唱歌!")


bird = Animal()  # 以 Animal 類別，建立一個名叫小鳥的 bird物件
print(bird.name)  # 小鳥
bird.sing()  # 很會唱歌!

print("------------------------------------------------------------")  # 60個

# ch07\class02.py


class Animal:  # 定義類別
    def __init__(self, name):
        self.name = name  # 定義屬性

    def sing(self):  # 定義方法
        print(self.name + "，很會唱歌!")


bird = Animal("鸚鵡")  # 以 Animal 類別，建立一個名叫鸚鵡的 bird物件
print(bird.name)  # 鸚鵡
bird.sing()  # 鸚鵡，很會唱歌!

print("------------------------------------------------------------")  # 60個

# ch07\class03.py


class Animal:  # 定義類別
    def __init__(self, name, age):
        self.name = name  # 定義屬性
        self.age = age

    def sing(self):  # 定義方法
        print(self.name + str(self.age) + "歲，很會唱歌!")

    def grow(self, year):  # 定義方法
        self.age += year


bird = Animal("鸚鵡", 1)  # 以 Animal 類別，建立一個名叫鸚鵡、1歲大的 bird物件
bird.grow(1)  # 長大1歲
bird.sing()  # 鸚鵡2歲，很會唱歌!

print("------------------------------------------------------------")  # 60個

# ch07\class04.py


class Animal:  # 定義類別
    def __init__(self, name, age):
        self.__name = name  # 定義私用屬性
        self.__age = age

    def __sing(self):  # 定義私用方法
        print(self.__name + str(self.__age), end="歲，很會唱歌，")

    def talk(self):  # 定義共用方法
        self.__sing()  # 使用私用方法
        print("也會模仿人類說話!")


bird = Animal("灰鸚鵡", 2)  # 以 Animal 類別，建立一個名叫灰鸚鵡、2歲大的 bird物件
bird.talk()  # 灰鸚鵡2歲，很會唱歌，也會模仿人類說話!

bird.__age = -1  # 設定無效
bird.talk()  # 灰鸚鵡2歲，很會唱歌，也會模仿人類說話!
# bird.__sing()   #執行出現錯誤

print("------------------------------------------------------------")  # 60個

# ch07\class05.py


class Animal:  # 定義父類別
    def __init__(self, name):
        self.name = name  # 定義共用屬性

    def fly(self):  # 定義共用方法
        print(self.name + "很會飛!")


class Bird(Animal):  # 定義子類別
    def __init__(self, name):
        self.name = "粉紅色" + name  # 覆寫父類別的建構式

    def sing(self):  # 定義子類別的方法
        print(self.name + "也愛唱歌!")


pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  # 小白鴿很會飛!

parrot = Bird("小鸚鵡")  # 以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
parrot.fly()  # 粉紅色小鸚鵡很會飛!
parrot.sing()  # 粉紅色小鸚鵡也愛唱歌!

print("------------------------------------------------------------")  # 60個

# ch07\class06.py


class Animal:  # 定義父類別
    def __init__(self, name):
        self.name = name  # 定義共用屬性

    def fly(self):  # 定義共用方法
        print(self.name + "很會飛!")


class Bird(Animal):  # 定義子類別
    def __init__(self, name, age):
        super().__init__(name)  # 執行父類別的 __init__()方法
        self.age = age  # 定義子類別共用屬性

    def fly(self):  # 定義子類別共用方法
        print(str(self.age), end="歲")
        super().fly()  # 執行父類別的 fly方法


pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  # 小白鴿很會飛!

parrot = Bird("小鸚鵡", 2)  # 以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
parrot.fly()  # 2歲小鸚鵡很會飛!

print("------------------------------------------------------------")  # 60個

# ch07\class07.py


class Animal:  # 定義父類別
    def fly(self):  # 定義共用方法
        print("時速 20公里!")


class Bird(Animal):  # 定義子類別
    def fly(self, speed):  # 定義共用方法
        print("時速 " + str(speed) + "公里!")


class Plane:  # 定義類別
    def fly(self):  # 定義共用方法
        print("時速 1000公里!")


def fly(speed):  # 定義函式
    print("時速 " + str(speed) + "英哩!")


animal = Animal()  # 以 Animal 類別建立 animal 物件
animal.fly()  # 時速 20公里!

bird = Bird()  # 以 Bird 類別建立 bird 物件
bird.fly(60)  # 時速 60公里!

plane = Plane()  # 以 Plane 類別建立 plane 物件
plane.fly()  # 時速 1000公里!

fly(5)  # 時速 5英哩!

print("------------------------------------------------------------")  # 60個

# ch07\class08.py


class Father:  # 定義父類別
    def say(self):  # 定義共用方法
        print("明天會更好!")


class Mother:  # 定義父類別
    def say(self):  # 定義共用方法
        print("包容、尊重!")


class Child(Father, Mother):  # 定義子類別
    pass


child = Child()  # 建立 child 物件
child.say()  # 明天會更好!

print("------------------------------------------------------------")  # 60個

# ch07\getPrivateAttribute.py


class Father:  # 定義父類別
    def __init__(self, name):
        self.name = name
        self.__eye = "黑色"  # 定義私用屬性

    def getEye(self):  # 定義共用方法傳回私用屬性
        return self.__eye


class Child(Father):  # 定義子類別
    def __init__(self, name, eye):
        super().__init__(name)
        self.eye = eye
        self.fatherEye = super().getEye()  # 取得私用屬性


joe = Child("小華", "棕色")  # 建立子類別物件 joe
print(joe.name + "眼睛是" + joe.eye + "，他的父親則是" + joe.fatherEye)
# 執行結果：小華眼睛是棕色，他的父親則是黑色

print("------------------------------------------------------------")  # 60個

# ch07\module-1.py


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


print(add(5, 2))  # 7
print(sub(5, 2))  # 3

print("------------------------------------------------------------")  # 60個

# ch07\module-2.py

import calculate  # 匯入 calculate 模組

print(calculate.add(5, 2))  # 7
print(calculate.sub(5, 2))  # 3

print("------------------------------------------------------------")  # 60個

# ch07\module-3.py

from calculate import add, sub

print(add(5, 2))  # 7
print(sub(5, 2))  # 3

print("------------------------------------------------------------")  # 60個

# ch07\module-4.py

from calculate import add

print(add(5, 2))  # 7
print(sub(5, 2))  # NameError: name 'sub' is not defined

print("------------------------------------------------------------")  # 60個

# ch07\module-5.py

from calculate import *

print(add(5, 2))  # 7
print(sub(5, 2))  # 3

print("------------------------------------------------------------")  # 60個

# ch07\module-6.py

from calculate import add as a

print(a(5, 2))  # 7

print("------------------------------------------------------------")  # 60個

# ch07\module-7.py

import calculate as cal  # 匯入 calculate 模組，並取別名為 cal

print(cal.add(5, 2))  # 7
print(cal.sub(5, 2))  # 3

print("------------------------------------------------------------")  # 60個

# ch07\password.py

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

# ch08\Assert.py


class Car:
    def __init__(self, speed):
        self.speed = speed

    def Turbo(self, n):  # 增加速度 n
        assert speed >= 0, "速度不可能為負!"
        self.speed += n


for speed in (60, -20):
    bus = Car(speed)
    print("初速=", bus.speed, end=" ")
    bus.Turbo(50)
    print("加速後，速度=", bus.speed)

print("------------------------------------------------------------")  # 60個

# ch07\div.py


def div(a, b):
    return a / b


print(div(6, 2))  # 3.0
print(div(3, 0))  # 中止程式
print(div(4, 2))  # 未被執行

print("------------------------------------------------------------")  # 60個

# ch07\raise1.py


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
        with open("err.txt", "a") as f:
            f.write(traceback.format_exc())  # 寫入例外過程
        print("錯誤資訊寫入完成!")
    else:
        print("目前時速：{}".format(speed))

print("------------------------------------------------------------")  # 60個

# ch07\try1.py

try:
    print(n)
except:
    print("變數 n 不存在!")

print("------------------------------------------------------------")  # 60個

# ch07\try2.py

n = 2
try:
    n += 1
except:
    print("變數 n 不存在!")
else:
    print("n=", n)  # n=3

print("------------------------------------------------------------")  # 60個

# ch07\try3.py

try:
    print(n)
except Exception as e:
    print(e)  # name 'n' is not defined

print("------------------------------------------------------------")  # 60個

# ch07\try4.py

try:
    print(n)
except:
    print("變數 n 不存在!")
finally:
    print("一定會執行的程式區塊")

print("------------------------------------------------------------")  # 60個

# ch07\tryadd.py

try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a + b
    print("r=", r)
except:
    print("發生輸入非數值的錯誤!")

print("------------------------------------------------------------")  # 60個

# ch07\trymod.py

try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
except ValueError:
    print("發生輸入非數值的錯誤!")
except Exception as e:
    print("發生", e, "的錯誤，包括分母為 0 的錯誤!")
else:
    print("r=", r)
finally:
    print("一定會執行的程式區塊")

print("------------------------------------------------------------")  # 60個

# ch07\trymod2.py

try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
except (ValueError, ZeroDivisionError):
    print("發生輸入非數值的錯誤或分母為 0 的錯誤!")
else:
    print("r=", r)

print("------------------------------------------------------------")  # 60個

# ch07\trymod3.py

try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
except (ValueError, ZeroDivisionError) as e:
    print("發生{} 0 的錯誤!".format(e))
else:
    print("r=", r)

print("------------------------------------------------------------")  # 60個

# ch09\eword_tkinter.py


def First():  # 首頁
    global page
    page = 0
    disp_data()


def Prev():  # 上一頁
    global page
    if page > 0:
        page -= 1
        disp_data()


def Next():  # 下一頁
    global page
    if page < pagesize:
        page += 1
        disp_data()


def Bottom():  # 最後頁
    global page
    page = pagesize
    disp_data()


def disp_data():
    if datas != None:
        sep1 = tk.Label(frameShow, text="\t", fg="white", width="20", font=("新細明體", 10))
        label1 = tk.Label(
            frameShow,
            text="單字".ljust(30),
            fg="white",
            bg="black",
            width=30,
            font=("新細明體", 10),
        )
        label2 = tk.Label(
            frameShow,
            text="中文翻譯".ljust(175),
            fg="white",
            bg="black",
            width=80,
            font=("新細明體", 10),
        )
        sep1.grid(row=0, column=0, sticky="w")  # 加第一列空白，讓版面美觀些
        label1.grid(row=1, column=0, sticky="w")
        label2.grid(row=1, column=1, sticky="w")

        n = 0  # 資料從索引 0 開始
        row = 2  # 資料從第二列開始
        start = page * pagesize + row
        for eword, cword in datas.items():
            # 顯示目前 page頁的資料
            if n >= start and n < start + pagesize:
                label1 = tk.Label(
                    frameShow,
                    text="\t" + "{0:30}".format(eword),
                    fg="blue",
                    font=("新細明體", 10),
                )
                label2 = tk.Label(
                    frameShow, text="{0:30}".format(cword), fg="blue", font=("新細明體", 10)
                )
                label1.grid(row=row, column=0, sticky="w")
                label2.grid(row=row, column=1, sticky="w")
                row += 1
            n += 1


### 主程式從這裡開始 ###

import tkinter as tk
import math

win = tk.Tk()
win.geometry("500x300")
win.title("英文單字王")

page, pagesize = 0, 10
datas = dict()

with open("eword.txt", "r", encoding="UTF-8-sig") as f:
    for line in f:
        eword, cword = line.rstrip("\n").split(",")
        datas[eword] = cword
print("轉換完畢!")

datasize = len(datas)  # 資料筆數
totpage = math.ceil(datasize / pagesize)  # 總頁數

# 單字顯示區
frameShow = tk.Frame(win)
frameShow.pack()
labelwords = tk.Label(win, text="")
labelwords.pack()

frameCommand = tk.Frame(win)  # 翻頁按鈕容器
frameCommand.pack()
btnFirst = tk.Button(frameCommand, text="第一頁", width=8, command=First)
btnPrev = tk.Button(frameCommand, text="上一頁", width=8, command=Prev)
btnNext = tk.Button(frameCommand, text="下一頁", width=8, command=Next)
btnBottom = tk.Button(frameCommand, text="最末頁", width=8, command=Bottom)
btnFirst.grid(row=0, column=0, padx=5, pady=5)
btnPrev.grid(row=0, column=1, padx=5, pady=5)
btnNext.grid(row=0, column=2, padx=5, pady=5)
btnBottom.grid(row=0, column=3, padx=5, pady=5)

First()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch09\tk.py

import tkinter as tk

win = tk.Tk()
win.geometry("450x100")
win.title("這是主視窗")
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch09\tkbutton1.py


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

# ch09\tkbutton2.py


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

# ch09\tkcheckbox1.py


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

# ch09\tkframe1.py

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

# ch09\tkgrid1.py

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

# ch09\tkgrid2.py

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

# ch09\tklabel1.py

import tkinter as tk

win = tk.Tk()
label1 = tk.Label(
    win, text="這是標籤元件！", fg="red", bg="yellow", font=("新細明體", 12), padx=20, pady=10
)
label1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

# ch09\tkpack1.py

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

# ch09\tkpack2.py

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

# ch09\tkpack3.py

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

# ch09\tkpassword.py


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

# ch09\tkplace1.py

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

# ch09\tkplace2.py

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

# ch09\tkradio1.py


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

# ch09\tktext1.py

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

# ch10\bracket.py

import re

pat = r"[0-9+]+"
s = "Amy was 18 year old,she likes Python and C++."
m = re.findall(pat, s)
print(m)  # ['18', '++']

print("------------------------------------------------------------")  # 60個

# ch10\compile.py

import re

reobj = re.compile(r"[a-z]+")
m = reobj.findall("3tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch10\dotall.py

import re

pat = r".*"
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group())  # Do your best,
m2 = re.search(r".*", s, re.DOTALL)
print(m2.group())  # Do your best,\nGo Go Go!

print("------------------------------------------------------------")  # 60個

# ch10\findall.py

import re

pat = re.compile("[a-z]+")
m = pat.findall("tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch10\ignore.py

import re

pat = r"PYTHON|ANDROID"
s = "I like Python and Android!"
m = re.findall(pat, s, re.I)
print(m)  # ['Python', 'Android']

print("------------------------------------------------------------")  # 60個

# ch10\match.py

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

# ch10\not1.py

import re

pat = r"[^a-z. ]+"
s = "John was 18 year old."
m = re.findall(pat, s)
print(m)  # ['J', '18']

print("------------------------------------------------------------")  # 60個

# ch10\not2.py

import re

pat = r"^\d+"
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m)  # ['2020']
m2 = re.findall(r"\w+$", s)
print(m2)  # ['soon']

print("------------------------------------------------------------")  # 60個

# ch10\phone_check.py


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

# ch10\phone1.py

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

# ch10\phone2.py

import re

numStr = "tel:(04)12345678"
pat = r"(\(\d{2}\))(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # (04)12345678
    print(phone.group(1))  # (04)
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# ch10\phone3.py

import re

phoneList = ["(04)12345678", "(04)-12345678"]
pat = r"(\(\d{2}\))-?(\d{8})"

for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# ch10\phone4.py

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

# ch10\plus.py

import re

pat = re.compile(r"[aeiou]+")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)  # ['o', 'i', 'e', 'ie']

print("------------------------------------------------------------")  # 60個

# ch10\re_findall.py

import re

m = re.findall(r"[a-z]+", "tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ch10\re_match.py

import re

pat = r"[a-z]+"
m = re.match(pat, "tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch10\re_search.py

import re

pat = "[a-z]+"
m = re.search(pat, "3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>

print("------------------------------------------------------------")  # 60個

# ch10\re_verbose.py

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

# ch10\regex.py

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

# ch10\search.py

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

# ch10\star.py

import re

pat = re.compile(r"[aeiou]*")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)

print("------------------------------------------------------------")  # 60個

# ch10\sub1.py

import re

pat = r"\d+"
substr = "*"
s = "Password:1234,ID:5678"
result = re.sub(pat, substr, s)
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# ch10\sub2.py

import re


def multiply(m):
    v = int(m.group())
    return str(v * 2)


result = re.sub("\d+", multiply, "10 20 30 40 50", 3)
print(result)  # 20 40 60 40 50

print("------------------------------------------------------------")  # 60個

# ch10\wild.py

import re

pat = r".o"
s = "Do your best!"
m = re.findall(pat, s)
print(m)  # ['Do', 'yo']
m2 = re.findall(r".*o", s)
print(m2)  # ['Do yo']

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

print("------------------------------------------------------------")  # 60個

# ch13\bar1.py

import matplotlib.pyplot as plt

listx = ["c", "c++", "c#", "java", "python"]
listy = [45, 28, 38, 32, 50]
plt.bar(listx, listy, width=0.5, color="rgb")
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\bar2.py

import matplotlib.pyplot as plt

listy = ["c", "c++", "c#", "java", "python"]
listx = [45, 28, 38, 32, 50]
plt.barh(listy, listx, height=0.5, color="rgb")
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\bar3.py

import matplotlib.pyplot as plt

listx = ["c", "c++", "c#", "java", "python"]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx, listy1, width=0.5, label="男")
plt.bar(listx, listy2, width=0.5, bottom=listy1, label="女")
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\bar4.py

import matplotlib.pyplot as plt

width = 0.25
listx = ["c", "c++", "c#", "java", "python"]
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx1, listy1, width, label="男")
plt.bar(listx2, listy2, width, label="女")
plt.xticks(range(len(listx)), labels=listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\figure2.py

import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 2, 3])
plt.grid(axis="y")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot1.py

import matplotlib.pyplot as plt

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]
plt.plot(listx, listy, "g--*", markersize=12)
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot2.py

import matplotlib.pyplot as plt

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title", fontsize=20)  # 圖表標題
plt.xlabel("X-Label", fontsize=14)  # x座標標題
plt.ylabel("Y-Label", fontsize=14)  # y座標標題
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot3.py

import matplotlib.pyplot as plt

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")  # 圖表標題
plt.xlabel("X-Label")  # x座標標題
plt.ylabel("Y-Label")  # y座標標題
plt.xlim(0, 20)  # 設定x座標範圍
plt.ylim(0, 100)  # 設定y座標範圍
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot4.py

import matplotlib.pyplot as plt

listx = [1, 5, 7, 9, 13, 18]
listy = [15, 50, 80, 40, 70, 50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")  # 圖表標題
plt.xlabel("X-Label")  # x座標標題
plt.ylabel("Y-Label")  # y座標標題
plt.xlim(0, 20)  # 設定x座標範圍
plt.ylim(0, 100)  # 設定y座標範圍
plt.grid(color="black", linestyle=":", linewidth="1", alpha=0.5)
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot5.py

import matplotlib.pyplot as plt

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1, "r-.s")
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2, "y-s")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot5_.py

import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listy1 = [128, 210, 199, 121, 105, 98, 152, 107, 150, 122, 180, 220]
plt.plot(month, listy1, "r-.s", lw=2, ms=10, label="Taipei")
listy2 = [150, 200, 180, 110, 100, 80, 80, 100, 130, 120, 110, 200]
plt.plot(month, listy2, "g--*", lw=2, ms=10, label="Taichung")
plt.legend()
plt.xticks(month)
plt.ylim(50, 250)
plt.title("Sales Report", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot6.py

import matplotlib.pyplot as plt

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx1, listy1, "r-.s", listx2, listy2, "y-s")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot6_.py

import matplotlib.pyplot as plt

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1, "r-.s", lw=2, ms=10, label="Male")
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2, "g--*", lw=2, ms=10, label="Female")
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("費用", fontsize=18)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Money", fontsize=12)
plt.tick_params(axis="y", color="red")
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot7.py

import matplotlib.pyplot as plt

listx = [1000, 2000, 3000, 4000, 5000]
listy = [15, 50, 80, 70, 50]
plt.plot(listx, listy)
plt.xticks(listx)
plt.tick_params(axis="both", labelsize=16, color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot8.py

import matplotlib.pyplot as plt

year = [2015, 2016, 2017, 2018, 2019]
city1 = [128, 150, 199, 180, 150]
plt.plot(year, city1, "r-.s", lw=2, ms=10, label="Taipei")
city2 = [120, 145, 180, 170, 120]
plt.plot(year, city2, "g--*", lw=2, ms=10, label="Taichung")
plt.legend()
plt.ylim(50, 250)
plt.xticks(year)
plt.title("Sales Report", fontsize=18)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.grid(color="k", ls=":", lw=1, alpha=0.5)
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\plot9.py

import matplotlib.pyplot as plt

year = [2015, 2016, 2017, 2018, 2019]
city1 = [128, 150, 199, 180, 150]
plt.plot(year, city1, "r-.s", lw=2, ms=10, label="台北")
city2 = [120, 145, 180, 170, 120]
plt.plot(year, city2, "g--*", lw=2, ms=10, label="台中")
plt.legend()
plt.ylim(50, 250)
plt.xticks(year)
plt.title("銷售報表", fontsize=18)
plt.xlabel("年度", fontsize=12)
plt.ylabel("百萬", fontsize=12)
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False
plt.show()

print("------------------------------------------------------------")  # 60個

# ch13\subplot_1.py

import matplotlib.pyplot as plt

listx = [1, 2, 3, 4, 5]

listy1 = [15, 50, 80, 40, 70]
plt.subplot(2, 1, 1)
plt.ylim(0, 100)
plt.plot(listx, listy1, "r-s")

listy2 = [80, 20, 60, 50, 20]
plt.subplot(2, 1, 2)
plt.ylim(0, 100)
plt.plot(listx, listy2, "g--o")

plt.show()

# plt.rcParams['figure.figsize'] = [10, 10]
# plt.rcParams['figure.dpi'] = 72
# plt.rcParams.keys

print("------------------------------------------------------------")  # 60個

# ch13\subplot_2.py

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
