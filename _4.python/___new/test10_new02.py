"""
準備清除
#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_9.py

# ch8_9.py


準備撈出

class bank  class Banks():

def

import traceback




"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

# Python 舊式字串格式化

errno = 50159747054
name = "鮑勃"

print("嘿, %s, 有錯誤 0x%x 發生了!" % (name, errno))

print("嘿, %(name)s, 有錯誤 0x%(errno)x 發生了!" % {"name": name, "errno": errno})

# Python 新式字串格式化

errno = 50159747054
name = "鮑勃"

print("嘿, {}, 有錯誤 0x{:x} 發生了!".format(name, errno))

print("嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!".format(name=name, errno=errno))


# f-string 字串格式化 (Python 3.6+)

errno = 50159747054
name = "鮑勃"

print(f"嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!")

a = 5
b = 10

print(f"5 加 10 等於 {a + b} 而非 {2 * (a + b)}")

# 樣板字串格式化

from string import Template

errno = 50159747054
name = "鮑勃"

templ_string = "嘿 $name, 有錯誤 $error 發生了!"
print(Template(templ_string).substitute(name=name, error=hex(errno)))

print("------------------------------------------------------------")  # 60個

# 5-2-2 array.array - C 語言格式數值陣列

import array

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

print(arr)

print(arr[1])

arr[1] = 23.0

print(arr)

del arr[1]

print(arr)

arr.append(42.0)

print(arr)

# arr[1] = 'hello'

print("------------------------------------------------------------")  # 60個

# 5-2-3 str - 不可變 Unicode 字元陣列

arr = "abcd"

print(arr)

print(arr[1])

print(type(arr))

print(type(arr[1]))

arr_list = list(arr)

print(arr_list)

print("".join(arr_list))

# arr[1] = 'e'

print("------------------------------------------------------------")  # 60個

# 5-2-4 bytes - 不可變位元組陣列

arr = bytes((0, 1, 2, 3))

print(type(arr))

print(arr)

print(arr[1])

data = "this is data"
arr = str.encode(data)

print(arr)
print(bytes.decode(arr))

# arr = bytes((0, 300))

print("------------------------------------------------------------")  # 60個

# 5-2-5 bytearray - 可變位元組陣列

arr = bytearray((0, 1, 2, 3))

print(arr)

print(arr[1])

arr[1] = 23

print(arr)

del arr[1]

print(arr)

arr.append(42)

print(arr)

print(bytes(arr))

# arr[1] = 300

print("------------------------------------------------------------")  # 60個

# 5-5-4 LifoQueue - 可用於多執行緒的堆疊 (2)

import threading, queue, time

source = ["吃飯", "睡覺", "寫程式", "散步", "聽音樂", "打牌", "玩電動"]
threads_num = 3

q = queue.LifoQueue()
for item in source:
    q.put(item)


def worker():
    print("執行緒開始")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個

# 5-6-2 Queue - 可用於多執行緒的佇列

import threading, queue, time

source = ["吃飯", "睡覺", "寫程式", "散步", "聽音樂", "打牌", "玩電動"]
threads_num = 3

q = queue.Queue()
for item in source:
    q.put(item)


def worker():
    print("執行緒開始")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個

# 5-6-3 multiprocessing.Queue - 給多核運算用的佇列

import multiprocessing, time


def worker(queue):
    print("process 開始")
    while True:
        item = queue.get()
        if item == "STOP":
            print("process 結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)


source = ["吃飯", "睡覺", "寫程式", "散步", "聽音樂", "打牌", "玩電動"]
process_num = 3

q = multiprocessing.Queue()
for item in source:
    q.put(item)

processes = []
for _ in range(process_num):
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    processes.append(p)

for _ in range(process_num):
    q.put("STOP")

for p in processes:
    p.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個

# 5-7-3 PriorityQueue - 可用於多執行緒的 heapq

import threading, queue, time

source = ["2-吃飯", "1-睡覺", "3-寫程式", "7-散步", "5-聽音樂", "6-打牌", "4-玩電動"]
threads_num = 3

q = queue.PriorityQueue()
for item in source:
    q.put(item)


def worker():
    print("執行緒開始")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個
import threading, time


def wakeUp():
    print("threadObj執行緒開始")
    time.sleep(10)  # threadObj執行緒休息10秒
    print("女朋友生日")
    print("threadObj執行緒結束")


print("程式階段1")
threadObj = threading.Thread(target=wakeUp)
threadObj.start()  # threadObj執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading, time


def wakeUp(name, blessingWord):
    print("threadObj執行緒開始")
    time.sleep(10)  # threadObj執行緒休息10秒
    print(name, " ", blessingWord)
    print("threadObj執行緒結束")


print("程式階段1")
threadObj = threading.Thread(target=wakeUp, args=["NaNa", "生日快樂"])
threadObj.start()  # threadObj執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading
import time


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
m.start()
w.start()

print("------------------------------------------------------------")  # 60個

import threading
import time


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
w2 = threading.Thread(name="Manager", target=worker)
m.start()
w.start()
w2.start()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    mydict = {wd:songList.count(wd) for wd in set(songList)}

filename = "AreYouSleeping.txt"
with open(filename) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
song = modifySong(data.lower())

wordCount(song)                     # 執行歌曲單字計數

dictList = sorted(mydict.items(), key=lambda item:item[1], reverse=True)
for key, val in dictList:
    print(key,':',val)
"""

print("------------------------------------------------------------")  # 60個

import os

files = ["c1.py", "c2.py", "c3.py"]
for file in files:
    print(os.path.join("D:\\test", file))

print("------------------------------------------------------------")  # 60個

print("串列 裡面都是字典")
animal0 = {
    "cname": "鼠",
    "ename": "mouse",
    "weight": 3,
}

animal1 = {
    "cname": "牛",
    "ename": "ox",
    "weight": 48,
}
animal2 = {
    "cname": "虎",
    "ename": "tiger",
    "weight": 33,
}

animal = [animal0, animal1, animal2]
print(type(animal0))
print(type(animal1))
print(type(animal2))
print(type(animal))

for ani in animal:
    for key, value in ani.items():
        print(f"Key: {key}", end="\t")
        print(f"Value: {value}")

print("------------------------------------------------------------")  # 60個


print("字典 裡面都是字典")

animal = {
    "mouse": {
        "cname": "鼠",
        "ename": "mouse",
        "weight": 3,
    },
    "ox": {
        "cname": "牛",
        "ename": "ox",
        "weight": 48,
    },
}

print(animal)
print(type(animal))

for animal_name, animal_info in animal.items():
    print(f"\nAnimalName: {animal_name}")
    name = f"{animal_info['cname']} {animal_info['ename']}"
    weight = animal_info["weight"]
    print(f"\tName: {name}")
    print(f"\tweight: {weight}")

print("------------------------------------------------------------")  # 60個

# 建立空白串列
animals = []

# 建立30隻動物
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    animals.append(new_alien)

# 顯示前5隻動物
for alien in animals[:5]:
    print(alien)
print("...")

# 前3隻改資料
for alien in animals[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# 顯示前5隻動物
for alien in animals[:5]:
    print(alien)
print("...")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 利用 表2-2所列的內建函數將輸入數值做轉換

# int()函式將number轉為整數型別
number = 1234
print("型別：", type(number))
print("二進位：", bin(number))
print("八進位", oct(number))
print("十六進位", hex(number))
print("10進位：", number)

# 配合format函式去除前綴字元
print("二進位：", format(number, "b"))
print("八進位：", format(number, "o"))
print("十六進位：", format(number, "x"))

print("------------------------------------------------------------")  # 60個

# 將兩個數值以decimal型別來處理

# 匯入decimal模組的Decimal()方法
from decimal import Decimal

num1 = Decimal("0.5534")
num2 = Decimal("0.427")
num3 = Decimal("0.37")
print("相加", num1 + num2 + num3)
print("相減", num1 - num2 - num3)
print("相乘", num1 * num2 * num3)
print("相除", num1 / num2)

print("------------------------------------------------------------")  # 60個

# 將代數轉為算術運算式
x = 23
y = 7
# 指定變數x、y的值
"""
   1. 先算出(x-5)/(y+9)
   2. 再加上 12/x 之值
   3. 最後乘 數值9 再給變數z儲存
"""
z = 9 * (12 / x + (x - 5) / (y + 9))
print("z = ", z)

print("------------------------------------------------------------")  # 60個

# for/in廻圈配合range()函式做數值累加

total = 0  # 儲存加總結果
count = 0  # 計數器
for count in range(1, 11):  # 數值1~10
    total += count  # 將數值累加
    print("累加值", total)  # 觀看累加結果
else:
    print("數值累加完畢...")

print("------------------------------------------------------------")  # 60個

# 雙層for建立九九乘法表

# 建立表頭
print("  |", end="")
for k in range(1, 10):
    # 不自動換行，只留空白字元
    print(format(k, "3d"), end="")
print()  # 換行
print("-" * 32)

# 第一層 for/in
for one in range(1, 10):
    print(one, "|", end="")  # 輸出表頭
    # 第二層 for/in
    for two in range(1, 10):
        print(format(one * two, "3d"), end="")  # 3d 表示欄寬為3
    print()  # 換行

print("------------------------------------------------------------")  # 60個

# while廻圈
number = 200
a, b = 2, 2  # 宣告變數
result = a**2

# while廻圈 變數result小於number時，輸出運算結果
print("運算結果-->")
while result < number:
    result *= b
    print(result)  # 輸出後換行
    # print(result, end =', ') #輸出後不換行

print("------------------------------------------------------------")  # 60個

# 兩個數值的區間累加

total = 0

string = "3, 5"

# 輸人兩個數值做區間累加

count, number = eval(string)
# print('數值', count, end = '')

while count <= number:
    total += count  # 儲存累加值
    print(count, total)
    count += 1  # 計數器

else:
    # print(' ~', number, '累計: ', total)
    # print('結束廻圈...')
    pass

print("------------------------------------------------------------")  # 60個

# while廻圈做分數加總

# total儲存總分，score儲存分數設，初值為0.0
total = score = 0.0
count = 0  # 計數器
# score = float(input('輸入分數，按-1結束-> '))

score = 60
total = total + score
count = count + 1

score = 70
total = total + score
count = count + 1

score = 90
total = total + score
count = count + 1

score = 70
total = total + score
count = count + 1

score = 60
total = total + score
count = count + 1

average = total / count  # 計算平均值
print("共", count, "科，總分:", total, ", 平均:", average)

print("------------------------------------------------------------")  # 60個

# break敘述中斷廻圈的執行
print("數值：", end="")
result = 0
for x in range(1, 11):
    result = x**2
    # 如果result的值大於就中斷廻圈的執行
    if result > 20:
        break
    print(result, end=", ")

print("------------------------------------------------------------")  # 60個

word = "Python"

# continue敘述
print("Continue: ", end=" ")
for cha in word:
    if cha == "t":
        continue  # 只中斷此次的執行
    print(cha, end="")

# break敘述
print("\nBreak: ", end=" ")
for cha in word:
    if cha == "t":
        break  # 中斷廻圈的執行
    print(cha, end="")

print("------------------------------------------------------------")  # 60個

# for/in廻圈讀取字串，enumerate()加入索引
name = "Python"
print("%5s" % "index", "%5s" % "char")
print("-" * 12)
for item in enumerate(name):
    print(" ", item)

print("------------------------------------------------------------")  # 60個

# format()函式, f-string

# {}格式碼，欄寬分別為3，6，8 靠右對齊
print("{:>3}{:>6}{:>8}".format("x", "x*x", "x*x*x"))

print("-" * 20)
for item in range(1, 11):
    print(f"{item:3d} {item**2:5d} {item**3:7,d}")

print("------------------------------------------------------------")  # 60個

# 建立Tuple，+運算子串接
tp1 = 22, 44
tp2 = (11, 33)
print("串接兩個Tuple", tp1 + tp2)

tp3 = "Mary", "look" + " at", " Tom"
print(tp3)

print("\n數值     索引")
print("-" * 14)

# 建立Tuple，使用index()方法
data = 38, 14, 45, 14, 117
print(f"第1個14{data.index(14):5}")

# index()方法從索引編號2開始
print(f"第2個14{data.index(14, 2):5}")

# 搜尋最後一個要加入邊界值
print(f"   117{data.index(117, 0, 5):5}")

print("------------------------------------------------------------")  # 60個

item = 0
name = "Mary", "Joson", "Eric", "Judy"  # Tuple

# while廻圈讀取元素
while item < len(name):
    print(item, name[item])
    item += 1

print("------------------------------------------------------------")  # 60個

# Tuple物件配合Packing, Unpacking
score = [78, 56, 33]  # List
chin, math, eng = score  # Unpacking

print(f"國文：{chin:2d} 數學：{math:2d} 英文：{eng:2d}")
print(f"總分：{sum(score)}")

n = "Eric"
b = "1998/4/17"
t = 175
tp = (n, b, t)  # Packing
name, birth, tall = tp  # Unpacking

print(f"名字：{name:>4s}")
print(f"生日：{birth:9s}, 身高：{tall}")

print("------------------------------------------------------------")  # 60個

# Packing和Unpacking的用法(2)

name = "Tom", "Mary"  # Tuple
t, m = name  # Unpacking
print(f"置換前:{t}, {m}")
t, m = m, t  # Swap
print(f"置換後:{t}, {m}")

print("------------------------------------------------------------")  # 60個

# list.sort()做遞增、遞減排序
name = ["Tom", "Judy", "Anthea", "Charles"]

# 省略參數，依字母做遞增
name.sort()
print(f"依字母遞增排序：\n{name}")

number = [49, 131, 85, 247]
number.sort(reverse=True)  # 遞減排序
print("遞減排序：", number)

print("------------------------------------------------------------")  # 60個

# BIF sorted()方法將Tuple元素排序
number = 447, 152, 814, 39, 211  # Tuple
print("原始資料：", number)

# 預設排序 -- 由小而大
print("遞增排序：", sorted(number))

# 遞減排序
print("遞減排序：", sorted(number, reverse=True))
print("原來Tuple：", number)

print("------------------------------------------------------------")  # 60個

# 呼叫list.sort()方法將Tuple元素排序

name = "Tom", "Charles", "Vicky", "Judy"
print("Tuple排序前：")
print(name)

# 1.Tuple以list()函式轉為List物件，再做排序
covlt = list(name)
covlt.sort()

# 2.排序後再以tuple()函式轉為Tuple
covtp = tuple(covlt)
print("Tuple排序後：")
print(covtp)

print("------------------------------------------------------------")  # 60個

"""
# 將輸入的分數先儲存於List，再以sum()函式加總

score = [] # 建立List來存放成績

# for廻圈建立輸入成績的list
for item in range(5):
   data = int(input('分數%2d ' %(item + 1)))
   score += [data]
print('%5s %5s ' % ('index', 'score'))

ind = 0 #計數器，每讀取一個元素就位移一個

#while廻圈讀取成績並輸出
while ind < len(score):
   print(f'{ind:3d} {score[ind]:4d}')
   ind += 1

print('-' * 12)
# 內建函式sum()計算總分
print(f'總分 = {sum(score)}, 平均 = {sum(score) / 5}')
score.sort(reverse = True) # score()方法遞減排序
print('遞減排序：', score)
print('遞增排序：', sorted(score)) # 使用BIF
"""

print("------------------------------------------------------------")  # 60個

# List生成式 找出10~65之間被7整除的數字

num = []  # 建立空的List

for item in range(10, 65):
    if item % 13 == 0:
        num.append(item)  # 整除的數放入List中
print("10~65被13整除之數：", num)


print("------------------------------------------------------------")  # 60個

# List生成式(2)
num = []  # 空的List
num = [item for item in range(10, 65) if (item % 13 == 0)]
print("10~65被13整除之數：", num)

print("------------------------------------------------------------")  # 60個

# 應用一：計算分數平均
score = [(85, 75, 46, 91), (49, 76, 87), (76, 93, 67)]
avg = [sum(item) / len(item) for item in score]
print(
    f"平均: {avg[0]:.3f}, {avg[1]:.3f},\
      {avg[2]:.3f}"
)
print()  # 換行

# 應用二：讀取字串長度
fruit = ["lemon", "apple", "orange", "blueberry"]
print("%9s" % "字串", "%2s" % "長度")
print("*----------------*")
print("\n".join(["%10s:%2d" % (item, len(item)) for item in fruit]))

print("------------------------------------------------------------")  # 60個

# 自訂函式 情形一：無參數，無回傳值


# step 1. 定義函式
def message():
    zen = """
        Beautiful is better than ugly.
        Explicit is better than implicit.
    """
    print(zen)


# step 2. 呼叫函式
message()

print("------------------------------------------------------------")  # 60個


# 定義函式
def funcTest(name, score):
    print("定義函式的。。。")
    name = "Judy"  # 情形一
    score.append(83)  # 情形二
    print(name, "id =", id(name))
    print(score, "id =", id(score))


# 呼叫函式
one = "Mary"
two = [75, 68]
funcTest(one, two)

print("\n呼叫函式時...")
print(one, "分數：", two)

# name不可變物件, score為可變物件
print("one", "id =", id(one))
print("two", "id =", id(two))

print("------------------------------------------------------------")  # 60個

# *運算式 Unpacking
pern = ("Vicky", "Female", 65, 75, 93)  # Tuple
# Tuple做Unpacking
name, sex, *score = pern
# 輸出相關的name & score
print(f"{name}: {score}")

print("------------------------------------------------------------")  # 60個


# 定義函式
def funTest(*number):
    outcome = 1
    for item in number:
        outcome *= item
    return outcome


# 呼叫函式
print("1個引數:", funTest(7))
print("2個引數:", funTest(12, 3))
print("4個引數:", funTest(3, 5, 9, 14))

print("------------------------------------------------------------")  # 60個


# 自訂函式
def student(name, *score, subject=4):
    if subject >= 1:
        print(f"{name:6}{subject} 科", end="")
        # print(f'{name}{subject}{*score}')
        print("分數 ", *score)
    total = sum(score)  # 合計分數
    print(f"總分: {total}", f"平均: {total / subject:.4f}")


# 呼叫函式
student("Peter", 65, 93, 82, 47)
print()
student("Judy", 85, 69, 79, subject=3)

print("------------------------------------------------------------")  # 60個


# 定義函式
def funcData(n1, n2, n3, n4, n5):
    print("基本資料:\n", n1, n2, n3, n4, n5)


# 呼叫函式，使用*運算子拆解「可迭代物件
data = [1988, 3, 18]
funcData("Mary", "Birth", *data)

print("------------------------------------------------------------")  # 60個


# 定義函式
def person(name, salary, s2, s3):
    print(name)
    # format()函式分設欄寬為10, 6 並加千位符號
    print(f"扣除額：{(s2 + s3):11,}")
    salary = salary - s2 - s3
    print(f"實領金額 NT$ {salary:6,}")


income = [28800, 605, 405]
# 呼叫函式 -- number串列物件，可迭代
person("Tomas", *income)

print("------------------------------------------------------------")  # 60個

fruit = "Apple"


# 定義函式
def Favorite():
    global fruit
    print("Favorite fruit is", fruit)
    fruit = "Blueberry"
    print("I like", fruit, "ice cream.")


# 呼叫函式
Favorite()

print("------------------------------------------------------------")  # 60個

from random import randint, randrange


# 產生某個區間的整數亂數
def numRand(x, y):
    cout = 1  # 計數器
    while cout <= 10:
        number = randint(x, y)
        print(number, end=" ")
        cout += 1
    print()


# 將產生以append()方法加至List
def numRand2(x, y):
    cout = 1
    result = []  # 存放亂數
    while cout <= 10:
        number = randint(x, y)
        result.append(number)
        cout += 1
    return result


print("------------------------------------------------------------")  # 60個

import inspect

# 輸出內建函數名
builtin_functions = [
    name for name, obj in inspect.getmembers(__builtins__) if inspect.isbuiltin(obj)
]
for function_name in builtin_functions:
    print(function_name)

print("------------------------------------------------------------")  # 60個

# 輸出內建函數名
builtin_functions = dir(__builtins__)
for function_name in builtin_functions:
    print(function_name)

print("------------------------------------------------------------")  # 60個

x1 = "22"
x2 = "33"
x3 = x1 + x2
print("type(x3) = ", type(x3))
print("x3 = ", x3)  # 列印字串相加
x4 = int(x1) + int(x2)
print("type(x4) = ", type(x4))
print("x4 = ", x4)  # 列印整數相加
x5 = "1100"
print("2進位  '1100' = ", int(x5, 2))
print("8進位  '22'   = ", int(x1, 8))
print("16進位 '22'   = ", int(x1, 16))
print("16進位 '5A'   = ", int("5A", 16))

print("------------------------------------------------------------")  # 60個

x1 = "A"
x2 = x1 * 10
print(x2)  # 列印字串乘以整數
x3 = "ABC"
x4 = x3 * 5
print(x4)  # 列印字串乘以整數

print("------------------------------------------------------------")  # 60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)

print("------------------------------------------------------------")  # 60個

x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出字元x3的Unicode(10進位)碼值
x4 = "魁"
print(hex(ord(x4)))  # 輸出字元'魁'的Unicode(16進位)碼值

print("------------------------------------------------------------")  # 60個

print("2 進位整數運算")
x = 0b1101  # 這是2進位整數
print(x)  # 列出10進位的結果
y = 13  # 這是10進位整數
print(bin(y))  # 列出轉換成2進位的結果
print("8 進位整數運算")
x = 0o57  # 這是8進位整數
print(x)  # 列出10進位的結果
y = 47  # 這是10進位整數
print(oct(y))  # 列出轉換成8進位的結果
print("16 進位整數運算")
x = 0x5D  # 這是16進位整數
print(x)  # 列出10進位的結果
y = 93  # 這是10進位整數
print(hex(y))  # 列出轉換成16進位的結果


print("------------------------------------------------------------")  # 60個
x = -10
print("以下輸出abs( )函數的應用")
print("x = ", x)  # 輸出x變數
print("abs(-10) = ", abs(x))  # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print("pow(5,3) = ", pow(x, y))  # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print("x = ", x)  # 輸出x變數
print("round(47.5) = ", round(x))  # 輸出round(x)
x = 48.5
print("x = ", x)  # 輸出x變數
print("round(48.5) = ", round(x))  # 輸出round(x)
x = 49.5
print("x = ", x)  # 輸出x變數
print("round(49.5) = ", round(x))  # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print("x = ", x)  # 輸出x變數
print("round(2.15,1) = ", round(x, 1))  # 輸出round(x,1)
x = 2.25
print("x = ", x)  # 輸出x變數
print("round(2.25,1) = ", round(x, 1))  # 輸出round(x,1)
x = 2.151
print("x = ", x)  # 輸出x變數
print("round(2.151,1) = ", round(x, 1))  # 輸出round(x,1)
x = 2.251
print("x = ", x)  # 輸出x變數
print("round(2.251,1) = ", round(x, 1))  # 輸出round(x,1)

print("------------------------------------------------------------")  # 60個

str1 = "明志科技大學"
str2 = "明志工專"
print(str1, str2, sep=" $$$ ")  # 以 $$$ 值位置分隔資料輸出

print(str1, str2, sep="\t")  # 以Tab鍵值位置分隔資料輸出

print("------------------------------------------------------------")  # 60個

x = 12345678
print("/%10.1e/" % x)
print("/%10.2E/" % x)
print("/%-10.2E/" % x)
print("/%+10.2E/" % x)
print("=" * 60)
string = "abcdefg"
print("/%10.3s/" % string)

print("------------------------------------------------------------")  # 60個

""" 不可用 會讓後面出現 TypeError: 'str' object is not callable
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
print(url + city + '&radius=' + str(r) + '&type=' + type)
print(url + "{}&radius={}&type={}".format(city, r, type))
"""

print("------------------------------------------------------------")  # 60個

""" 不可用 會讓後面出現 TypeError: 'str' object is not callable
name = '洪錦魁'
message = f"我是{name}"
print(message)

url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
my_url = url + f"{city}&radius={r}&type={type}"
print(my_url)

"""

print("------------------------------------------------------------")  # 60個

sp = " " * 40
print("%s   1231 Delta Rd" % sp)
print("%s   Oxford, Mississippi" % sp)
print("%s   USA\n\n\n" % sp)
print("Dear Ivan")
print("I am pleased to inform you that your application for fall 2025 has")
print("been favorably reviewed by the Electrical and Computer Engineering")
print("Office.\n\n")
print("Best Regards")
print("Peter Malong")

print("------------------------------------------------------------")  # 60個

fobj1 = open("tmp_out24w.txt", mode="w")  # 取代先前資料
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close()
fobj2 = open("tmp_out24a.txt", mode="a")  # 附加資料後面
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close()

print("------------------------------------------------------------")  # 60個

fobj1 = open("tmp_out25w.txt", mode="w", encoding="utf-8")
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close()
fobj2 = open("tmp_out25a.txt", mode="a", encoding="cp950")
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close()

print("------------------------------------------------------------")  # 60個

"""
loan = eval(input("請輸入貸款金額："))
year = eval(input("請輸入年限："))
rate = eval(input("請輸入年利率："))
monthrate = rate / (12*100)             # 改成百分比的月利率

# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator    # 每月還款金額
totalPay = monthlyPay * year * 12       # 總共還款金額

print(f"每月還款金額 {int(monthlyPay)}")
print(f"總共還款金額 {int(totalPay)}")

"""

print("------------------------------------------------------------")  # 60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

x = 100
print("x=/%6d/" % x)
y = 10.5
print("y=/%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留格數空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_7.py

# ch4_7.py
x = 100
print("x=/%-8d/" % x)
y = 10.5
print("y=/%-8.2f/" % y)
s = "Deep"
print("s=/%-8s/" % s)

print("------------------------------------------------------------")  # 60個

x = 10
print("x=/%+8d/" % x)
y = 10.5
print("y=/%+8.2f/" % y)

print("------------------------------------------------------------")  # 60個

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print("------------------------------------------------------------")  # 60個

print("判斷輸入字元類別")
ch = "C"
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("這是大寫字元")
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("這是小寫字元")
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("這是數字")
else:
    print("這是特殊字元")


print("------------------------------------------------------------")  # 60個

flag = None
if not flag:
    print("尚未定義flag")
if flag:
    print("有定義")
else:
    print("尚未定義flag")

print("------------------------------------------------------------")  # 60個

james = [23, 19, 22, 31, 18]  # 定義james串列
print("列印james串列", james)
James = ["Lebron James", 23, 19, 22, 31, 18]  # 定義James串列
print("列印James串列", James)
fruits = ["apple", "banana", "orange"]  # 定義fruits串列
print("列印fruits串列", fruits)
cfruits = ["蘋果", "香蕉", "橘子"]  # 定義cfruits串列
print("列印cfruits串列", cfruits)
ielts = [5.5, 6.0, 6.5]  # 定義IELTS成績串列
print("列印IELTS成績", ielts)
# 列出串列資料型態
# print("串列james資料型態是: ",type(james))    fail

print("------------------------------------------------------------")  # 60個

cars = ["Benz", "BMW", "Honda"]
nums = [1, 3, 5]
carslist = cars * 3  # 串列乘以數字
print(carslist)
numslist = nums * 5  # 串列乘以數字
print(numslist)

print("------------------------------------------------------------")  # 60個

warriors = ["Curry", "Durant", "Iquodala", "Bell", "Thompson"]
print("2025年初NBA勇士隊主將陣容", warriors)
del warriors[3]  # 不明原因離隊
print("2025年末NBA勇士隊主將陣容", warriors)

print("------------------------------------------------------------")  # 60個

nums1 = [1, 3, 5]
print(f"刪除nums1串列索引1元素前   = {nums1}")
del nums1[1]
print(f"刪除nums1串列索引1元素後   = {nums1}")
nums2 = [1, 2, 3, 4, 5, 6]
print(f"刪除nums2串列索引[0:2]前   = {nums2}")
del nums2[0:2]
print(f"刪除nums2串列索引[0:2]後   = {nums2}")
nums3 = [1, 2, 3, 4, 5, 6]
print(f"刪除nums3串列索引[0:6:2]前 = {nums3}")
del nums3[0:6:2]
print(f"刪除nums3串列索引[0:6:2]後 = {nums3}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_14.py

# ch6_14.py
cars = ["Toyota", "Nissan", "Honda"]
print(f"cars串列長度是 = {len(cars)}")
if len(cars) != 0:  # 一般寫法
    del cars[0]
    print("刪除cars串列元素成功")
    print(f"cars串列長度是 = {len(cars)}")
else:
    print("cars串列內沒有元素資料")
nums = []
print(f"nums串列長度是 = {len(nums)}")
if len(nums):  # 更好的寫法
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_15.py

# ch6_15.py
cars = ["bmw", "benz", "audi"]
carF = "我開的第一部車是 " + cars[1].title()
carN = "我現在開的車子是 " + cars[0].upper()
print(carF)
print(carN)

print("------------------------------------------------------------")  # 60個

strN = " DeepWisdom       "
strL = strN.lstrip()  # 刪除字串左邊多餘空白
strR = strN.rstrip()  # 刪除字串右邊多餘空白
strB = strN.strip()  # 一次刪除頭尾端多餘空白
print(f"/{strN}/")
print(f"/{strL}/")
print(f"/{strR}/")
print(f"/{strB}/")


print("------------------------------------------------------------")  # 60個

title = "Ming-Chi Institute of Technology"
print(f"/{title.center(50)}/")
dt = "Department of ME"
print(f"/{dt.ljust(50)}/")
site = "JK Hung"
print(f"/{site.rjust(50)}/")
print(f"/{title.zfill(50)}/")

print("------------------------------------------------------------")  # 60個

james = [23, 19, 22, 31, 18]  # 定義james串列
print("列印james第1場得分", james[0])
print("列印james第2場得分", james[1])
print("列印james第3場得分", james[2])
print("列印james第4場得分", james[3])
print("列印james第5場得分", james[4])

print("------------------------------------------------------------")  # 60個

cars = []
print(f"目前串列內容 = {cars}")
cars.append("Honda")
print(f"目前串列內容 = {cars}")
cars.append("Toyota")
print(f"目前串列內容 = {cars}")

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "Toyota", "Ford"]
print(f"目前串列內容 = {cars}")
print("在索引1位置插入Nissan")
cars.insert(1, "Nissan")
print(f"新的串列內容 = {cars}")
print("在索引0位置插入BMW")
cars.insert(0, "BMW")
print(f"最新串列內容 = {cars}")

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "Toyota", "Ford", "BMW"]
print("目前串列內容 = ", cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop()  # 刪除串列末端值
print(f"所刪除的串列內容是 : {popped_car}")
print("新的串列內容 = ", cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)  # 刪除串列索引為1的值
print(f"所刪除的串列內容是 : {popped_car}")
print("新的串列內容 = ", cars)

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "bmw", "Toyota", "Ford", "bmw"]
print(f"目前串列內容 = {cars}")
print("使用remove( )刪除串列元素")
expensive = "bmw"
cars.remove(expensive)  # 刪除第一次出現的元素bmw
print(f"所刪除的內容是 : {expensive.upper()} 因為重複了")
print(f"新的串列內容 = {cars}")

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "bmw", "Toyota", "Ford", "bmw"]
print(f"目前串列內容 = {cars}")
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print(f"列印使用[::-1]顛倒排序\n{cars[::-1]}")
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse()  # 顛倒排序串列
print(f"新的串列內容 = {cars}")

print("------------------------------------------------------------")  # 60個

# 基本排序
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers)  # 輸出：[1, 2, 3, 4, 5]

# 降序排序
numbers = [3, 5, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)  # 輸出：[5, 4, 3, 2, 1]

# 使用函數定義排序
words = ["banana", "apple", "strawberry"]
words.sort(key=len)
print(words)  # 輸出：['apple', 'banana', 'strawberry]

print("------------------------------------------------------------")  # 60個

# 基本排序
numbers = [3, 5, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 輸出：[1, 2, 3, 4, 5]

# 按降序排序
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # 輸出：[5, 4, 3, 2, 1]

# 使用 key 函數排序
words = ["banana", "apple", "strawberry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # 輸出：['apple', 'banana', 'strawberry]

# 對字串排序
string = "hello"
sorted_chars = sorted(string)
print(sorted_chars)  # 輸出：['e', 'h', 'l', 'l', 'o']

print("------------------------------------------------------------")  # 60個

# 在串列中使用 index()
fruits = ["apple", "banana", "cherry", "date"]
index = fruits.index("cherry")
print(index)  # 輸出：2

# 指定搜索範圍, 搜尋的起始索引是 1
fruits = ["apple", "banana", "cherry", "date", "apple"]
index_range = fruits.index("apple", 1)
print(index_range)  # 輸出：4

print("------------------------------------------------------------")  # 60個

James = ["Lebron James", 23, 19, 22, 31, 18]  # 定義James串列
games = len(James)  # 求元素數量
score_Max = max(James[1:games])  # 最高得分
i = James.index(score_Max)  # 場次
print(f"{James[0]} 在第 {i} 場得最高分 {score_Max}")

print("------------------------------------------------------------")  # 60個

# 在串列中使用 count()
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
apple_count = fruits.count("apple")
print(apple_count)  # 輸出：2

# 在字串中使用 count()
text = "Hello, how are you? How can I help you?"
how_count = text.count("how")
print(how_count)  # 輸出：1

# 在字串中指定搜索範圍
how_count_range = text.count("how", 0, 15)
print(how_count_range)  # 輸出：1

print("------------------------------------------------------------")  # 60個

james = [23, 19, 22, 31, 18]  # 定義james串列
# 傳統設計方式
game1 = james[0]
game2 = james[1]
game3 = james[2]
game4 = james[3]
game5 = james[4]
print("列印james各場次得分", game1, game2, game3, game4, game5)
# Python高手好的設計方式
game1, game2, game3, game4, game5 = james
print("列印james各場次得分", game1, game2, game3, game4, game5)

print("------------------------------------------------------------")  # 60個

James = [["Lebron James", "SF", "12/30/84"], 23, 19, 22, 31, 18]  # 定義James串列
games = len(James)  # 求元素數量
score_Max = max(James[1:games])  # 最高得分
i = James.index(score_Max)  # 場次
name, position, born = James[0]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print(f"在第 {i} 場得最高分 {score_Max}")

print("------------------------------------------------------------")  # 60個

cars1 = ["toyota", "nissan", "honda"]
cars2 = ["ford", "audi"]
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.append(cars2)
print(f"執行append()後串列cars1內容 = {cars1}")
print(f"執行append()後串列cars2內容 = {cars2}")

print("------------------------------------------------------------")  # 60個

cars1 = ["toyota", "nissan", "honda"]
cars2 = ["ford", "audi"]
cars1.extend(cars2)
print(f"執行extend()後串列cars1內容 = {cars1}")
print(f"執行extend()後串列cars2內容 = {cars2}")

print("------------------------------------------------------------")  # 60個

sc = [
    ["洪錦魁", 80, 95, 88, 0],
    ["洪冰儒", 98, 97, 96, 0],
]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append("football")
friendsports.append("soccer")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append("football")
friendsports.append("soccer")
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports[:]
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append("football")
friendsports.append("soccer")
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports.copy()
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append("football")
friendsports.append("soccer")
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")

print("------------------------------------------------------------")  # 60個

string = "Abc"
# 正值索引
print(f" {string[0] = }", f"\n {string[1] = }", f"\n {string[2] = }")
# 負值索引
print(f" {string[-1] = }", f"\n {string[-2] = }", f"\n {string[-3] = }")
# 多重指定觀念
s1, s2, s3 = string
print(f"多重指定觀念的輸出測試 {s1}{s2}{s3}")

print("------------------------------------------------------------")  # 60個

string = "Deep Learning"  # 定義字串
print(f"列印string第0-2元素     = {string[0:3]}")
print(f"列印string第1-3元素     = {string[1:4]}")
print(f"列印string第1,3,5元素   = {string[1:6:2]}")
print(f"列印string第1到最後元素 = {string[1:]}")
print(f"列印string前3元素       = {string[0:3]}")
print(f"列印string後3元素       = {string[-3:]}")
print("=" * 60)
print(f"列印string第1-3元素     = {'Deep Learning'[1:4]}")

print("------------------------------------------------------------")  # 60個

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"串列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:2]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::-1]     = {x[::-1]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")
print(f"x[-1]       = {x[-1]}")  # 這是取單一元素

print("------------------------------------------------------------")  # 60個

str1 = "Silicon Stone Education"
str2 = "D:\Python\ch6"

sList1 = str1.split()  # 字串轉成串列
sList2 = str2.split("\\")  # 字串轉成串列
print(f"{str1} 串列內容是 {sList1}")  # 列印串列
print(f"{str1} 串列字數是 {len(sList1)}")  # 列印字數
print(f"{str2} 串列內容是 {sList2}")  # 列印串列
print(f"{str2} 串列字數是 {len(sList2)}")  # 列印字數

print("------------------------------------------------------------")  # 60個

path = ["D:", "ch6", "ch6_41.py"]
connect = "\\"  # 路徑分隔字元
print(connect.join(path))
connect = "*"  # 普通字元
print(connect.join(path))

print("------------------------------------------------------------")  # 60個

msg = """CIA Mark told CIA Linda that the secret USB had given to CIA Peter"""
print(f"字串開頭是CIA : {msg.startswith('CIA')}")
print(f"字串結尾是CIA : {msg.endswith('CIA')}")
print(f"CIA出現的次數 : {msg.count('CIA')}")
msg = msg.replace("Linda", "Lxx")
print(f"新的msg內容 : {msg}")


print("------------------------------------------------------------")  # 60個

# 比較兩個指向相同物件的變數
a = [1, 2, 3]
b = a
print(a is b)  # 輸出: True

# 比較兩個指向不同物件的變數, 即使它們的值相等
c = [1, 2, 3]
print(a is c)  # 輸出: False

# 比較兩個指向不同物件的變數
d = [4, 5, 6]
e = [4, 5, 6]
print(d is not e)  # 輸出: True

# 比較兩個指向相同物件的變數
f = d
print(d is not f)  # 輸出: False

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")
r = x  # r的值將變為10
print(f"{x = }, {y = }, {z = }, {r = }")
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = z - 5
print("is測試")
boolean = x is y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")
print("=" * 60)
print("is not測試")
boolean = x is not y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is not z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is not r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)  # 數值初始是0
print("轉成串列輸出, 初始索引值是 0 = ", list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start=10)  # 數值初始是10
print("轉成串列輸出, 初始索引值是10 = ", list(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

warriors = ["Curry", "Durant", "Iquodala", "Bell", "Thompson"]
first3 = warriors[:3]
print("前3名球員", first3)
n_to_last = warriors[1:]
print("球員索引1到最後", n_to_last)
last3 = warriors[-3:]
print("後3名球員", last3)

print("------------------------------------------------------------")  # 60個
james = [23, 19, 22, 31, 18]  # 定義james的得分
print(f"James比賽場次 = {len(james)}")
print(f"最高得分 = {max(james)}")
print(f"最低得分 = {min(james)}")
print(f"得分總計 = {sum(james)}")

print("------------------------------------------------------------")  # 60個

James = ["Lebron James", 23, 19, 22, 31, 18]  # 比賽得分
print(f"James比賽場次 = {len(James[1:])}")
print(f"最高得分 = {max(James[1:])}")
print(f"最低得分 = {min(James[1:])}")
print(f"得分總計 = {sum(James[1:])}")

print("------------------------------------------------------------")  # 60個

cars = ["Toyota", "Nissan", "Honda"]
print("舊汽車銷售品牌", cars)
cars[1] = "Ford"  # 更改第二筆元素內容
print("新汽車銷售品牌", cars)

print("------------------------------------------------------------")  # 60個

cars1 = ["Toyota", "Nissan", "Honda"]
print("舊汽車銷售品牌", cars1)
cars2 = ["Audi", "BMW"]
cars1 += cars2
print("新汽車銷售品牌", cars1)

print("------------------------------------------------------------")  # 60個

celsius = [21, 25, 29]
fahrenheit = [(x * 9 / 5 + 32) for x in celsius]
print(fahrenheit)

print("------------------------------------------------------------")  # 60個

x = [
    [a, b, c]
    for a in range(1, 20)
    for b in range(a, 20)
    for c in range(b, 20)
    if a**2 + b**2 == c**2
]
print(x)

print("------------------------------------------------------------")  # 60個

colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square", "Line"]
result = [[color, shape] for color in colors for shape in shapes]
print(result)

print("------------------------------------------------------------")  # 60個

colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square"]
result = [[color, shape] for color in colors for shape in shapes]
for color, shape in result:
    print(color, shape)

print("------------------------------------------------------------")  # 60個

for x in range(0x2160, 0x216A):
    print(chr(x), end=" ")

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "香蕉", "西瓜"]
print("目前fruits串列 : ", fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print(f"刪除 {fruit}")
    print("目前fruits串列 : ", fruits)

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
    print()  # 換列輸出

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()  # 換列輸出

print("------------------------------------------------------------")  # 60個

scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse=True)  # 從大到小排列
count = 0
for sc in scores:
    count += 1
    print(sc, end=" ")
    if count == 5:  # 取前5名成績
        break  # 離開for迴圈

print("------------------------------------------------------------")  # 60個

scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:  # 小於30則不往下執行
        continue
    games += 1  # 場次加1
print(f"有{games}場得分超過30分")

print("------------------------------------------------------------")  # 60個

players = [
    ["James", 202],
    ["Curry", 193],
    ["Durant", 205],
    ["Jordan", 199],
    ["David", 211],
]
for player in players:
    if player[1] < 200:
        continue
    print(player)


print("------------------------------------------------------------")  # 60個

i = 1  # 設定i初始值
while i <= 9:  # 當i大於9跳出外層迴圈
    j = 1  # 設定j初始值
    while j <= 9:  # 當j大於9跳出內層迴圈
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
        j += 1  # 內層迴圈加1
    print()  # 換列輸出
    i += 1  # 外層迴圈加1

print("------------------------------------------------------------")  # 60個

index = 0
while index <= 10:
    index += 1
    if index % 2:  # 測試是否奇數
        continue  # 不往下執行
    print(index)  # 輸出偶數

print("------------------------------------------------------------")  # 60個

fruits = ["apple", "orange", "apple", "banana", "apple"]
fruit = "apple"
print("刪除前的fruits", fruits)
while fruit in fruits:  # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)

print("------------------------------------------------------------")  # 60個

buyers = [
    ["James", 1030],  # 建立買家購買紀錄
    ["Curry", 893],
    ["Durant", 2050],
    ["Jordan", 990],
    ["David", 2110],
]
goldbuyers = []  # Gold買家串列
vipbuyers = []  # VIP買家串列
while buyers:  # 買家分類完成,迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:  # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)  # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]
# 解析enumerate物件
for drink in enumerate(drinks):  # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")
# 解析enumerate物件
for drink in enumerate(drinks, 10):  # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

scores = [21, 29, 18, 33, 12, 17, 26, 28, 15, 19]
# 解析enumerate物件
for count, score in enumerate(scores, 1):  # 初始值是 1
    if score >= 20:
        print(f"場次 {count} : 得分 {score}")

print("------------------------------------------------------------")  # 60個

sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 80, 0, 0, 0],
]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])  # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)  # 填入平均
    print(sc[i])
sc.sort(key=lambda x: x[5], reverse=True)  # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):  # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x: x[0])  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 90, 0, 0, 0],
]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])  # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)  # 填入平均
    print(sc[i])
sc.sort(key=lambda x: x[5], reverse=True)  # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):  # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x: x[0])  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

x = 1000000
pi = 0
for i in range(1, x + 1):
    pi += 4 * ((-1) ** (i + 1) / (2 * i - 1))
    if i % 100000 == 0:  # 隔100000執行一次
        print(f"當 {i = :7d} 時 PI = {pi:20.19f}")

print("------------------------------------------------------------")  # 60個

chicken = 0
while True:
    rabbit = 35 - chicken  # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:  # 腳的總數
        print(f"雞有 {chicken} 隻, 兔有 {rabbit} 隻")
        break
    chicken += 1

print("------------------------------------------------------------")  # 60個

sum = 0
for i in range(64):
    if i == 0:
        wheat = 1
    else:
        wheat = 2**i
    sum += wheat
print(f"麥粒總共 = {sum}")

print("------------------------------------------------------------")  # 60個

print("電影院劃位系統")
sc = [
    [" ", " 1", " 2", " 3", " 4"],
    ["A", "□", "□", "□", "□"],
    ["B", "■", "□", "□", "□"],
    ["C", "□", "■", "■", "□"],
    ["D", "□", "□", "□", "□"],
]
for seatrow in sc:  # 輸出目前座位表
    for seat in seatrow:
        print(seat, end="  ")
    print()

print("=" * 60)
for seatrow in sc:  # 輸出最後座位表
    for seat in seatrow:
        print(seat, end="  ")
    print()

print("------------------------------------------------------------")  # 60個

fib = []
n = 9
fib.append(0)  # fib[0] = 0
fib.append(1)  # fib[1] = 1
for i in range(2, n + 1):
    f = fib[i - 1] + fib[i - 2]  # fib[i] = fib[i-1]+fib[i-2]
    fib.append(f)  # 加入費式數列
for i in range(n + 1):
    print(fib[i], end=", ")  # 輸出費式數列

print("------------------------------------------------------------")  # 60個

players = ["Curry", "Jordan", "James", "Durant", "Obama"]
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)

print("------------------------------------------------------------")  # 60個

files = ["da1.c", "da2.py", "da3.py", "da4.java"]
py = []
for file in files:
    if file.endswith(".py"):  # 以.py為副檔名
        py.append(file)  # 加入串列
print(py)

print("------------------------------------------------------------")  # 60個

money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= 1 + rate
    print(f"第 {i+1} 年本金和 : {int(money)}")

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)  # 定義元組元素是整數
fruits = ("apple", "orange")  # 定義元組元素是字串
mixed = ("James", 50)  # 定義元組元素是不同型態資料
val_tuple = (10,)  # 只有一個元素的元祖
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元組資料型態
# print("元組mixed資料型態是: ",type(mixed)) fail

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
list_keys = list(keys)  # 將元組改為串列
list_keys.append("secret")  # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)

print("------------------------------------------------------------")  # 60個

keys = ["magic", "xaab", 9099]  # 定義串列元素是字串與數字
tuple_keys = tuple(keys)  # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)
# tuple_keys.append('secret')         # 增加元素 --- 錯誤錯誤

print("------------------------------------------------------------")  # 60個

tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))

print("------------------------------------------------------------")  # 60個

"""
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
lst = list(enumerate_drinks)
print("轉成串列輸出, 初始索引值是 0 = ", lst)
print(type(lst[0]))
"""

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)  # 數值初始是0
print("轉成元組輸出, 初始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start=10)  # 數值初始是10
print("轉成元組輸出, 初始值是10 = ", tuple(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):  # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")
# 解析enumerate物件
for drink in enumerate(drinks, 10):  # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)  # 定義元組元素是整數
fruits = ("apple", "orange")  # 定義元組元素是字串
val_tuple = (10,)  # 只有一個元素的元祖
print(numbers1[0])  # 以中括號索引值讀取元素內容
print(numbers1[4])
print(fruits[0], fruits[1])
print(val_tuple[0])
x, y = ("apple", "orange")
print(x, y)
x, y = fruits
print(x, y)

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
for key in keys:
    print(key)

print("------------------------------------------------------------")  # 60個

fruits = ("apple", "orange")  # 定義元組元素是字串
print(fruits[0])  # 列印元組fruits[0]
# fruits[0] = 'watermelon'            # 將元素內容改為watermelon  fail
print(fruits[0])  # 列印元組fruits[0]

print("------------------------------------------------------------")  # 60個

fruits = ("apple", "orange")  # 定義元組元素是水果
print("原始fruits元組元素")
for fruit in fruits:
    print(fruit)

fruits = ("watermelon", "grape")  # 定義新的元組元素
print("\n新的fruits元組元素")
for fruit in fruits:
    print(fruit)

print("------------------------------------------------------------")  # 60個

fruits = ("apple", "orange", "banana", "watermelon", "grape")
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])

print("------------------------------------------------------------")  # 60個

fruits = ("apple", "banana", "cherry", "date", "cherry")
print(f"fruits 元組長度是 {len(fruits)}")  # 輸出 5

index = fruits.index("cherry")
print(f"cherry 索引位置是 {index}")  # 輸出 2

cherry_count = fruits.count("cherry")
print(f"cherry 出現次數是 {cherry_count}")  # 輸出 2

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
print(keys)
# print(type(keys))
# key = keys.pop( )                   # 錯誤 無此方法

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
# keys.append('secret')               # 錯誤 無此方法


print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
print(fruits)
print(noodles)
# 列出字典資料型態
print("字典fruits資料型態是: ", type(fruits))

print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
print("舊fruits字典內容:", fruits)
valueTup = fruits.popitem()
print("新fruits字典內容:", fruits)
print("刪除內容:", valueTup)

print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
print("舊fruits字典內容:", fruits)
fruits.clear()
print("新fruits字典內容:", fruits)

print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)

print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
print(f"Stephen Curry是 {players['Stephen Curry']} 的球員")
print(f"Kevin Durant是 {players['Kevin Durant']} 的球員")
print(f"Paul Gasol是 {players['Paul Gasol']} 的球員")

print("------------------------------------------------------------")  # 60個

dealerA = {1: "Nissan", 2: "Toyota", 3: "Lexus"}
dealerB = {11: "BMW", 12: "Benz"}
dealerA.update(dealerB)
print(dealerA)

print("------------------------------------------------------------")  # 60個

dealerA = {1: "Nissan", 2: "Toyota", 3: "Lexus"}
dealerB = {3: "BMW", 4: "Benz"}
dealerA.update(dealerB)
print(dealerA)

print("------------------------------------------------------------")  # 60個

nation = [["日本", "東京"], ["泰國", "曼谷"], ["英國", "倫敦"]]
nationDict = dict(nation)
print(nationDict)

print("------------------------------------------------------------")  # 60個

mydict = {"name": "Hung", "age": 25, "city": "New York"}
for key in mydict:
    print(f"{key} : {mydict[key]}")

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for name, team in players.items():
    print(f"姓名:{name}")
    print(f"隊名:{team}")


print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for name in players.keys():
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_19.py

# ch9_19.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for name in players:
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_19_1.py

# ch9_19_1.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
keys_list = [key for key in players]
print(keys_list)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_2.py

# ch9_2.py
fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
print("水蜜桃一斤 = ", fruits["水蜜桃"], "元")
print("牛肉麵一碗 = ", noodles["牛肉麵"], "元")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_20.py

# ch9_20.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for name in sorted(players):
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21.py

# ch9_21.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for team in players.values():
    print(team)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_1.py

# ch9_21_1.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for team in players:
    print(players[team])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_2.py

# ch9_21_2.py
players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
}
for team in set(players.values()):
    print(team)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_3.py

# ch9_21_3.py
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item: item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_4.py

# ch9_21_4.py
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item: item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_22.py

# ch9_22.py
soldier0 = {"tag": "red", "score": 3, "speed": "slow"}  # 建立小兵
soldier1 = {"tag": "blue", "score": 5, "speed": "medium"}
soldier2 = {"tag": "green", "score": 10, "speed": "fast"}
armys = [soldier0, soldier1, soldier2]  # 小兵組成串列
for army in armys:  # 列印小兵
    print(army)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_23.py

# ch9_23.py
armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {"tag": "red", "score": 3, "speed": "slow"}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print(f"小兵數量 = {len(armys)}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_24.py

# ch9_24.py
armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {"tag": "red", "score": 3, "speed": "slow"}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier["tag"] == "red":
        soldier["tag"] = "blue"
        soldier["score"] = 5
        soldier["speed"] = "medium"
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_25.py

# ch9_25.py
# 建立內含字串的字典
sports = {"Curry": ["籃球", "美式足球"], "Durant": ["棒球"], "James": ["美式足球", "棒球", "籃球"]}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items():
    print(f"{name} 喜歡的運動是: ")
    # 列印value,這是串列
    for sport in favorite_sport:
        print(f"   {sport}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_26.py

# ch9_26.py
# 建立內含字典的字典
wechat_account = {
    "cshung": {"last_name": "洪", "first_name": "錦魁", "city": "台北"},
    "kevin": {"last_name": "鄭", "first_name": "義盟", "city": "北京"},
}
# 列印內含字典的字典
for account, account_info in wechat_account.items():
    print("使用者帳號 = ", account)  # 列印鍵(key)
    name = account_info["last_name"] + " " + account_info["first_name"]
    print(f"姓名       = {name}")  # 列印值(value)
    print(f"城市       = {account_info['city']}")  # 列印值(value)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_27.py

# ch9_27.py
# 建立內含字典的字典
wechat = {
    "cshung": {"last_name": "洪", "first_name": "錦魁", "city": "台北"},
    "kevin": {"last_name": "鄭", "first_name": "義盟", "city": "北京"},
}
# 列印字典元素個數
print(f"wechat字典元素個數       {len(wechat)}")
print(f"wechat['cshung']元素個數 {len(wechat['cshung'])}")
print(f"wechat['kevin']元素個數  {len(wechat['kevin'])}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_28.py

# ch9_28.py
# 將串列轉成字典
seq1 = ["name", "city"]  # 定義串列
list_dict1 = dict.fromkeys(seq1)
print(f"字典1 {list_dict1}")
list_dict2 = dict.fromkeys(seq1, "Chicago")
print(f"字典2 {list_dict2}")
# 將元組轉成字典
seq2 = ("name", "city")  # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print(f"字典3 {tup_dict1}")
tup_dict2 = dict.fromkeys(seq2, "New York")
print(f"字典4 {tup_dict2}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_29.py

# ch9_29.py
fruits = {"Apple": 20, "Orange": 25}
ret_value1 = fruits.get("Orange")
print(f"Value = {ret_value1}")
ret_value2 = fruits.get("Grape")
print(f"Value = {ret_value2}")
ret_value3 = fruits.get("Grape", 10)
print(f"Value = {ret_value3}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_3.py

# ch9_3.py
fruits = {0: "西瓜", 1: "香蕉", 2: "水蜜桃"}
print(fruits[0], fruits[1], fruits[2])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_30.py

# ch9_30.py
# key在字典內
my_dict = {"apple": 1, "banana": 2}

# 使用 setdefault() 獲取 'apple' 的值
value1 = my_dict.setdefault("apple", 0)
print(value1)

# 使用 setdefault() 獲取 'orange' 的值
value2 = my_dict.setdefault("orange", 3)
print(value2)

# 輸出更新後的字典
print(my_dict)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_31.py

# ch9_31.py
person = {"name": "John"}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault("age")
print(f"增加age鍵 {person}")
print(f"age = {age}")
# 'sex'鍵不存在
sex = person.setdefault("sex", "Male")
print(f"增加sex鍵 {person}")
print(f"sex = {sex}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_31_1.py

# ch9_31_1.py
things = {
    "iWatch手錶": (15000, 0.1),  # 定義商品
    "Asus  筆電": (35000, 0.7),
    "iPhone手機": (38000, 0.3),
    "Acer  筆電": (40000, 0.8),
    "Go Pro攝影": (12000, 0.1),
}

# 商品依價值排序
th = sorted(things.items(), key=lambda item: item[1][0])
print("所有商品依價值排序如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_32.py

# ch9_32.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}  # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()  # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch, "")
print("不再有標點符號的歌曲")
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()
print("以下是歌曲串列")
print(songList)  # 列印歌曲串列

# 將歌曲串列處理成字典
for wd in songList:
    if wd in mydict:  # 檢查此字是否已在字典內
        mydict[wd] += 1  # 累計出現次數
    else:
        mydict[wd] = 1  # 第一次出現的字建立此鍵與值

print("以下是最後執行結果")
print(mydict)  # 列印字典


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_33.py

# ch9_33.py
word = "deepmind"
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
print(alphabetCount)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_34.py

# ch9_34.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
# mydict = {}                         # 省略,空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()  # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch, "")
print("不再有標點符號的歌曲")
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()
print("以下是歌曲串列")
print(songList)  # 列印歌曲串列

# 將歌曲串列處理成字典
mydict = {wd: songList.count(wd) for wd in songList}
print("以下是最後執行結果")
print(mydict)  # 列印字典


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_35.py

# ch9_35.py
season = {
    "水瓶座": "1月20日 - 2月18日, 需警惕小人",
    "雙魚座": "2月19日 - 3月20日, 凌亂中找立足",
    "白羊座": "3月21日 - 4月19日, 運勢比較低迷",
    "金牛座": "4月20日 - 5月20日, 財運較佳",
    "雙子座": "5月21日 - 6月21日, 運勢好可錦上添花",
    "巨蟹座": "6月22日 - 7月22日, 不可鬆懈大意",
    "獅子座": "7月23日 - 8月22日, 會有成就感",
    "處女座": "8月23日 - 9月22日, 會有挫折感",
    "天秤座": "9月23日 - 10月23日, 運勢給力",
    "天蠍座": "10月24日 - 11月22日, 中規中矩",
    "射手座": "11月23日 - 12月21日, 可羨煞眾人",
    "魔羯座": "12月22日 - 1月19日, 需保有謙虛",
}

wd = "雙魚座"
if wd in season:
    print(wd, " 本月運勢 : ", season[wd])
else:
    print("星座輸入錯誤")

print("------------------------------------------------------------")  # 60個

print("摩斯密碼")
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

wd = "ABCDEFG"
for c in wd:
    print(morse_code[c])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_4.py

# ch9_4.py
fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
fruits["橘子"] = 18
print(fruits)
print("橘子一斤 = ", fruits["橘子"], "元")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_5.py

# ch9_5.py
fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
print("舊價格香蕉一斤 = ", fruits["香蕉"], "元")
fruits["香蕉"] = 12
print("新價格香蕉一斤 = ", fruits["香蕉"], "元")


print("------------------------------------------------------------")  # 60個

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
print("舊fruits字典內容:", fruits)
del fruits
# print("新fruits字典內容:", fruits)       # 錯誤! 錯誤!


print("------------------------------------------------------------")  # 60個

""" test locals()
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var_dict = input("請輸入要刪除的變數 : ")
if var_dict in locals():    # 檢查變數是否存在
    print(f"{var_dict} 變數存在")
    del fruits
    print(f"刪除 {var_dict} 變數成功")
else:
    print(f"{var_dict} 變數不存在")
  

print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var = input("請輸入要刪除的字典變數 : ")
if var in locals():
    var = eval(var)
    if isinstance(var, dict):
        print(f"'fruits' 字典變數存在")
        del fruits
        print(f"刪除字典變數成功")
    else:
        print(f"字典變數不存在")
else:
    print(f"{var} 變數不存在")

"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_9.py

# ch9_9.py
fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
print("舊fruits字典內容:", fruits)
objKey = "西瓜"
value = fruits.pop(objKey)
print("新fruits字典內容:", fruits)
print("刪除內容:", objKey + ":" + str(value))

print("------------------------------------------------------------")  # 60個

"""
集合 的 方法
.discard()
.pop()
.clear()

ret_element = animals.pop( )        
print("刪除後的animals集合 ", animals)
print("所刪除的元素是      ", ret_element)

boolean = A.isdisjoint(B)       # 有共同的元素'c'
boolean = A.isdisjoint(C)       # 沒有共同的元素
print("沒有共同的元素傳回值是 ", boolean)


boolean = A.issubset(B)         # 所有A的元素皆是B的元素
boolean = C.issubset(B)         # 有共同的元素k


fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)







print("------------------------------------------------------------")  # 60個

boolean = A.issuperset(B)           # 測試
boolean = A.issuperset(C)           # 測試
print("A集合是C集合的父集合傳回值是 ", boolean)

cars1.update(cars2)

myset = {5, 3, 8, 1, 2}

print(f"集合元素數量   : {len(myset)}")
print(f"集合元素最大值 : {max(myset)}")
print(f"集合元素最小值 : {min(myset)}")
print(f"集合元素總和   : {sum(myset)}")

# 使用 sorted() 函數對集合進行排序
sorted_list = sorted(myset)
print(f"小到大排序 : {sorted_list}")         # 輸出: [1, 2, 3, 5, 8]
sorted_list_desc = sorted(myset, reverse=True)
print(f"大到小排序 : {sorted_list_desc}")    # 輸出: [8, 5, 3, 2, 1]

X = frozenset([1, 3, 5])
Y = frozenset([5, 7, 9])
print(X)
print(Y)
print("交集  = ", X & Y)
print("聯集  = ", X | Y)
A = X & Y
print("交集A = ", A)
A = X.intersection(Y)
print("交集A = ", A)

"""
print("------------------------------------------------------------")  # 60個

students = {
    "Peter",
    "Norton",
    "Kevin",
    "Mary",
    "John",
    "Ford",
    "Nelson",
    "Damon",
    "Ivan",
    "Tom",
}

Math = {"Peter", "Kevin", "Damon"}  # 數學夏令營參加人員
Physics = {"Nelson", "Damon", "Tom"}  # 物理夏令營參加人員

MorP = Math | Physics
print("有 %d 人參加數學或物理夏令營名單  : " % len(MorP), MorP)
unAttend = students - MorP
print("沒有參加任何夏令營有 %d 人名單是 : " % len(unAttend), unAttend)

A = {n for n in range(1, 100, 2)}
print(type(A))
print(A)

print("------------------------------------------------------------")  # 60個

A = {n for n in range(1, 100, 2) if n % 11 == 0}
print(type(A))
print(A)

print("------------------------------------------------------------")  # 60個

word = "deepmind"
alphabetCount = {alphabet: word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_28.py

# ch10_28.py
cocktail = {
    "Blue Hawaiian": {"Rum", "Sweet Wine", "Cream", "Pineapple Juice", "Lemon Juice"},
    "Ginger Mojito": {"Rum", "Ginger", "Mint Leaves", "Lime Juice", "Ginger Soda"},
    "New Yorker": {"Whiskey", "Red Wine", "Lemon Juice", "Sugar Syrup"},
    "Bloody Mary": {"Vodka", "Lemon Juice", "Tomato Juice", "Tabasco", "little Sale"},
}
# 列出含有Vodka的酒
print("含有Vodka的酒 : ")
for name, formulas in cocktail.items():
    if "Vodka" in formulas:
        print(name)
# 列出含有Lemon Juice的酒
print("含有Lemon Juice的酒 : ")
for name, formulas in cocktail.items():
    if "Lemon Juice" in formulas:
        print(name)
# 列出含有Rum但是沒有薑的酒
print("含有Rum但是沒有薑的酒 : ")
for name, formulas in cocktail.items():
    if "Rum" in formulas and not ("Ginger" in formulas):
        print(name)
# 列出含有Lemon Juice但是沒有Cream或是Tabasco的酒
print("含有Lemon Juice但是沒有Cream或是Tabasco的酒 : ")
for name, formulas in cocktail.items():
    if "Lemon Juice" in formulas and not formulas & {"Cream", "Tabasco"}:
        print(name)

print("------------------------------------------------------------")  # 60個

# 練習 02 加總一系列數字


def my_sum(*numbers):
    output = 0
    for n in numbers:
        output += n
    return output


print(my_sum(10, 20, 30, 40, 50))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 練習 04 將 16 進位數轉為 10 進位


def hex_to_dec():
    hexnum = "ff"
    decnum = 0

    for power, digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            digit_num = int(digit)
        else:
            digit_num = ord(digit.upper()) - ord("A") + 10
        decnum += digit_num * (16**power)

    print("十進位結果:", decnum)


hex_to_dec()

print("------------------------------------------------------------")  # 60個

# 練習 05 豬拉丁文


def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


print(pig_latin("python"))

print("------------------------------------------------------------")  # 60個

# 練習 06 豬拉丁文 --- 句子翻譯機


def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        if word[0] in "aeiou":
            output.append(f"{word}way")
        else:
            output.append(f"{word[1:]}{word[0]}ay")
    return " ".join(output)


print(pl_sentence("this is a test"))


print("------------------------------------------------------------")  # 60個

# 練習 07 ROT13 加密法


def rot13(word):
    output = []
    for c in word.lower():
        new_ord = ord(c) + 13
        if new_ord > ord("z"):
            new_ord -= 26
        output.append(chr(new_ord))
    return "".join(output)


print(rot13("apple"))

print("------------------------------------------------------------")  # 60個

# 練習 08 字元排序


def strsort(s):
    return "".join(sorted(s))


print(strsort("python"))

print("------------------------------------------------------------")  # 60個

# 練習 09 擷取和合併多種容器的頭尾元素


def first_last(seq):
    return seq[:1] + seq[-1:]


print(first_last("abcde"))
print(first_last([1, 2, 3, 4, 5]))

print("------------------------------------------------------------")  # 60個

# 練習 10 萬用加總函式


def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum("abc", "d", "e"))
print(mysum([10, 20, 30], [40, 50], [60]))

print("------------------------------------------------------------")  # 60個

# 練習 11 依姓名排序聯絡資料

people = [
    ("Joe", "Biden", "president@usa.gov"),
    ("Emmanuel", "Macron", "president@france.gov"),
    ("Justin", "Trudeau", "primeminister@canada.gov"),
    ("Angela", "Merkel", "primeminister@germany.gov"),
    ("Jacinda", "Ardern", "primeminister@newzealand.gov"),
]

for person in sorted(people, key=lambda d: (d[1], d[0])):
    print(f"{person[1]}, {person[0]}: {person[2]}")

print("------------------------------------------------------------")  # 60個

# 練習 12 用排版格式輸出容器資料

import operator


def sorted_grades(grades):
    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for first, last, grade in grades:
        output.append(f"{last:12s}{first:10s}{grade:.1f}")
    return "\n".join(output)


grades = [
    ("Alice", "Wooding", 89),
    ("Bob", "Johnson", 86),
    ("Cindy", "Letterman", 93),
    ("David", "Moor", 86),
    ("Eddie", "Williams", 91),
]

print(sorted_grades(grades))

print("------------------------------------------------------------")  # 60個

# 練習 13 尋找單字中重複最多次的字母

import operator


def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f"{result[0]} 重複了 {result[1]} 次")


most_repeated_letter("independence")

print("------------------------------------------------------------")  # 60個

# 練習 14 餐廳點餐機

menu = {"三明治": 50, "咖啡": 40, "沙拉": 30}

price = menu["三明治"]
print(price)

print("------------------------------------------------------------")  # 60個

# 練習 15 降雨量資料庫

rainfall = {}
city_name = "AAA"
rain_mm = 123
rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
city_name = "BBB"
rain_mm = 123
rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
city_name = "CCC"
rain_mm = 789
rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)

for city, rain in rainfall.items():
    print(f"{city}: {rain} mm")

print("------------------------------------------------------------")  # 60個

# 練習 16 有幾個不重複的數字?


def unique_num_len(numbers):
    return len(set(numbers))


numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(unique_num_len(numbers))

print("------------------------------------------------------------")  # 60個

# 練習 17 比較兩個 dict 的差異


def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys() | second.keys())

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output


d1 = {"a": 1, "b": 2, "c": 3, "d": 5}
d2 = {"a": 1, "b": 2, "d": 4, "e": 6}
print(dict_diff(d1, d2))

print("------------------------------------------------------------")  # 60個

# 練習 25 XML 產生器


def myxml(tag, content="", **kwargs):
    attrs_list = []
    for key, value in kwargs.items():
        attrs_list.append(f' {key}="{value}"')
    attrs = "".join(attrs_list)
    return f"<{tag}{attrs}>{content}</{tag}>"


print(myxml("foo", "bar", a=1, b=2, c=3))

print("------------------------------------------------------------")  # 60個

# 練習 26 簡易前序式計算機

import operator


def prefix_cal(to_solve):
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    op, num1, num2 = to_solve.split()
    return operation[op](float(num1), float(num2))


print(prefix_cal("+ 2 3"))

print("------------------------------------------------------------")  # 60個

# 練習 27 自訂密碼產生器

import random


def set_password_source(source):
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))
        return "".join(output)

    return password_gen


my_password_gen = set_password_source("0123456789abcdefghij")
print(my_password_gen(10))

print("------------------------------------------------------------")  # 60個

# 練習 28 輸出一組數字的絕對值


def abs_numbers(numbers):
    # return [abs(x) for x in numbers]
    return list(map(abs, numbers))


print(abs_numbers([1, -2, 3, -4, 5]))

print("------------------------------------------------------------")  # 60個

# 練習 29 只加總資料中的數字


def sum_numbers(data):
    return sum([int(d) for d in data.split() if d.isdigit()])


print(sum_numbers("10 abc 20 de44 30 55fg 40"))

print("------------------------------------------------------------")  # 60個

# 練習 30 用巢狀生成式『壓平』二維 list


def flatten(data):
    return [sub_element for element in data for sub_element in element]


print(flatten([[1, 2], [3, 4]]))

print("------------------------------------------------------------")  # 60個

# 顛倒一個 dict 的鍵與值


def flipped_dict(my_dict):
    return {value: key for key, value in my_dict.items()}


print(flipped_dict({"a": 1, "b": 2, "c": 3}))

print("------------------------------------------------------------")  # 60個

# 以字串為鍵的自訂 dict


class StrDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

    def __getitem__(self, key):
        if not str(key) in self:
            self[key] = None
        return dict.__getitem__(self, str(key))


sd = StrDict()
sd[1] = 1
sd[3.14] = 3.14
sd["10"] = "test"

print(sd[1])
print(sd["3.14"])
print(sd[10])
print(sd["a"])
print(sd)

print("------------------------------------------------------------")  # 60個

# 練習 43 動物類別


class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num

    def __repr__(self):
        return f"{self.species}(color={self.color!r}, leg_num={self.leg_num})"


class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


elephant = Elephant("灰")
zebra = Zebra("黑白")
snake = Snake("綠")
parrot = Parrot("灰")

print(elephant)
print(zebra)
print(snake)
print(parrot)

print("------------------------------------------------------------")  # 60個

# 練習 44 動物展示區類別


class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num

    def __repr__(self):
        return f"{self.color}色 {self.species} ({self.leg_num} 條腿)"


class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Exhibit:
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []

    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)

    def __repr__(self):
        return (
            f"展示區編號 {self.id_num}: "
            + f'{", ".join([str(animal) for animal in self.animals])}'
        )


ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant("灰"), Zebra("黑白"))
ex2.add_animals(Snake("綠"), Parrot("灰"))

print(ex1)
print(ex2)

print("------------------------------------------------------------")  # 60個

# 練習 45 動物園類別


class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num

    def __repr__(self):
        return f"{self.color}色 {self.species} ({self.leg_num} 條腿)"


class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Exhibit:
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []

    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)

    def __repr__(self):
        return (
            f"展示區編號 {self.id_num}: "
            + f'{", ".join([str(animal) for animal in self.animals])}'
        )


class Zoo:
    def __init__(self):
        self.exhibits = []

    def add_exhibits(self, *new_exhibits):
        for exhibit in new_exhibits:
            self.exhibits.append(exhibit)

    def __repr__(self):
        return "動物園:\n" + "\n".join([str(exhibit) for exhibit in self.exhibits])

    def animals_by_color(self, color):
        return [
            animal
            for exhibit in self.exhibits
            for animal in exhibit.animals
            if animal.color == color
        ]

    def animal_by_leg_num(self, leg_num):
        return [
            animal
            for exhibit in self.exhibits
            for animal in exhibit.animals
            if animal.leg_num == leg_num
        ]

    def animal_total_leg_num(self):
        return sum(
            [animal.leg_num for exhibit in self.exhibits for animal in exhibit.animals]
        )


zoo = Zoo()
ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant("灰"), Zebra("黑白"))
ex2.add_animals(Snake("綠"), Parrot("灰"))
zoo.add_exhibits(ex1, ex2)

print(zoo)
print("灰色動物:", zoo.animals_by_color("灰"))
print("4 條腿動物:", zoo.animal_by_leg_num(4))
print("腿的總數:", zoo.animal_total_leg_num())

print("------------------------------------------------------------")  # 60個

# 練習 46 自訂列舉容器


class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value


myEnum = MyEnumerate("abcde")
for index, letter in myEnum:
    print(f"{index} -> {letter}")

print("------------------------------------------------------------")  # 60個

# 練習 47 循環取值器


class CycleIterator:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value


class CycleList:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)


clist = CycleList(["a", "b", "c"], 5)
for c in clist:
    print(c)

print("------------------------------------------------------------")  # 60個

# 練習 49 產生器運算式


def num_generator(num):
    return (int(digit) for digit in str(num) if digit.isnumeric())


numbers = num_generator(3.14159)

for num in numbers:
    print(num)

print("------------------------------------------------------------")  # 60個

# 練習 50 能計算時間長度的產生器

import time
import random


def elapsed_time_gen():
    last_time = time.perf_counter()
    while True:
        now = time.perf_counter()
        yield now - last_time
        last_time = now


elapsed_time = elapsed_time_gen()

for _ in range(5):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))

print("------------------------------------------------------------")  # 60個


def sum_of_two(data, k):
    for a_index, a_value in enumerate(data):
        for b_index, b_value in enumerate(data):
            if a_index != b_index and a_value + b_value == k:
                return [a_index, b_index]
    return []


print(sum_of_two([2, 7, 11, 15], 9))

print("------------------------------------------------------------")  # 60個


def find_majority_num(data):
    counter = [(data.count(i), i) for i in set(data)]
    return sorted(counter, reverse=True)[0][1]

print(find_majority_num([1, 2, 2, 3, 2, 3, 1]))

print("------------------------------------------------------------")  # 60個


def find_missing_nums(data):
    all_data = set(range(1, len(data) + 1))
    return list(all_data - set(data))


print(find_missing_nums([1, 2, 8, 5, 1, 6, 4, 9, 5]))

print("------------------------------------------------------------")  # 60個


class Stack:
    def __init__(this):
        this.data = []

    def push(this, x):
        this.data.append(x)

    def pop(this):
        if this.data:
            return this.data.pop()

    def top(this):
        return this.data[-1]

    def min_num(this):
        return min(this.data)

    def max_num(this):
        return max(this.data)


stack = Stack()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(5)
print(stack.pop())
print(stack.top())
print(stack.min_num())
print(stack.max_num())

print("------------------------------------------------------------")  # 60個


def are_brackets_valid(s):
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for b in s:
        if b in brackets:
            stack.append(brackets[b])
        else:
            if not (stack and b == stack.pop()):
                return False
    return True if not stack else False


print(are_brackets_valid("[()]"))

print("------------------------------------------------------------")  # 60個


def zeroes_to_the_end(data):
    for _ in range(data.count(0)):
        idx = data.index(0)
        data = data[:idx] + data[idx + 1 :] + data[idx : idx + 1]
    return data


print(zeroes_to_the_end([2, 3, 0, 1, 0, 5]))

print("------------------------------------------------------------")  # 60個


def reverse_num_digits(x):
    answer = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
    return answer


print(reverse_num_digits(-123))

print("------------------------------------------------------------")  # 60個


def reverse_binary(n):
    binary = f"{n:08b}"
    return int(binary[::-1], 2)


print(reverse_binary(121))

print("------------------------------------------------------------")  # 60個


def roman_num_to_int(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    roman_special = {
        "IV": -2,
        "IX": -2,
        "XL": -20,
        "XC": -20,
        "CD": -200,
        "CM": -200,
    }
    normal_value = sum([roman[c] for c in s if c in roman])
    special_value = sum([value for key, value in roman_special.items() if key in s])
    return normal_value + special_value


print(roman_num_to_int("MMCDXIX"))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


'''
names = ["A太","B介","C子","D郎"]
for i, name in enumerate(names):
    if name == "C子":
        print(i, "號的", name, "找到了。")

print("------------------------------------------------------------")  # 60個

def search(findname):
    names = ["A太","B介","C子","D郎"]
    for i, name in enumerate(names):
        if name == findname:
            return i, name
    return -1, "找不到該名稱。"

n, name = search("C子")
print(name, n, "號")
n, name = search("A子")
print(name, n, "號")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def human_size(size):
    units = ["位元組","KB","MB","GB","TB","PB","EB"]
    n = 0
    while size > 1024:
        size = size / 1024.0
        n += 1
    return str(int(size)) + " " + units[n]

print(human_size(123))
print(human_size(123456))
print(human_size(123456789))
print(human_size(123456789012))

print("------------------------------------------------------------")  # 60個


text = "abcde.txt"
word1 = "abc"
word2 = "xyz"

count1 = text.count(word1)
print(word1, ":", count1, "個")
count2 = text.count(word2)
print(word2, ":", count2, "個")

print("------------------------------------------------------------")  # 60個

def compareString(string):
    """檢查是否是搜尋的字串"""
    if string == searchStr:
        return True
    else:
        return False

def parseString(string):
    global num
    # notFoundSignal = True     # 註記沒有找到電話號碼為True
    for i in range(len(data)):  # 用迴圈逐步抽取字串長度做測試
        msg = data[i:i+len(string)]
        if compareString(msg):
            num += 1

#filename = 'C:/_git/vcs/_4.python/_data/射鵰英雄傳.big5.txt'
filename = 'C:/_git/vcs/_4.python/_data/python_word_count1.txt'
#filename = 'data/ex16_2.txt'
with open(filename) as file_obj:      # 讀取ex21_2.txt
    data = file_obj.read()
    #print(data)

searchStr = "包含"
num = 0
parseString(searchStr)
print("所搜尋字串 %s 共出現 %d 次" % (searchStr, num))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import re

files = os.listdir("_data")
txtList = []
# 測試1
pattern = '(.*).txt'
print("列印*.txt")
for filename in files:
    #print(filename)
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        txtList.append(filename)
print(txtList)

pyList = []  
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = '(ch14_1(\d).py)'
for filename in files:
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        pyList.append(filename)
print(pyList)

print("------------------------------------------------------------")  # 60個

"""
localtime()返回元組的日期與時間資料結構 用索引方式獲得個別內容
索引	名稱	說明
0	tm_year	年 	2020
1	tm_mon	月 	1-12
2	tm_mday 日	1-31
3	tm_hour	時	0-23
4	tm_min	分	0-59
5	tm_sec	秒	0-59
6	tm_wday	星期	0:一, 1:二...
7	tm_yday	年第幾天
8	tm_isdst 夏令時間 0:不是, 1:是
"""

import time                         # 導入模組time

xtime = time.localtime()            #使用localtime()方法列出目前時間的結構
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

print("------------------------------------------------------------")  # 60個

print("列出所有python關鍵字")
import keyword
print(keyword.kwlist)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 函數文件字串 docstring 註明此函數的功能與用法
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')


#用help(函數名稱)列出此函數的文件字串

help(greeting)


print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))  # 建立串列
total = 0  # 總計
for i in number:
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
total = 0  # 總計
for i in range(1, n + 1):
    total += i
print("從1到%d的總和是 = " % n, total)

'''
print("------------------------------------------------------------")  # 60個

import numpy as np
import math

print("------------------------------------------------------------")  # 60­э

num = 3.2
print("數值{0:2.1f} 取log10 {1:4.3f}".format(num, np.log10(num)))

print("------------------------------------------------------------")  # 60­э

num = 1234
print("¨數值 = {0:10d},  數值 = {0:10d}".format(num, num))

num = 123.456789

print("¨數值 = {1:6.3f},  數值 = {1:6.3f}".format(num, num))

print("------------------------------------------------------------")  # 60­э

degrees = [x * 30 for x in range(13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print(
        "角度{0:3d}, 弧度{1:5.2f}, sin{2:3d}={3:5.2f}, cos{4:3d}={5:5.2f}".format(
            d, rad, d, sin, d, cos
        )
    )

print("------------------------------------------------------------")  # 60­э

print("arctan 3.4")
rad = np.arctan(3.4)
print(rad)
th = np.degrees(rad)
print(th)

print("------------------------------------------------------------")  # 60­э

rand = []
for i in range(10):
    rand.append(random.randint(0, 100))
print(rand)

print("------------------------------------------------------------")  # 60­э

# The card suit characters:
HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'
# A list of chr() codes is at https://inventwithpython.com/chr


for _ in range(20):
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    print(suit, end=" ")
print()


def getRandomCard():
    rank = random.choice(list("23456789JQKA") + ["10"])
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    return (rank, suit)


cc = getRandomCard()
print(cc)


print("------------------------------------------------------------")  # 60個

# 宣告迷宮陣列
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

print("[迷宮的路徑(0的部分)]")
for i in range(10):
    for j in range(12):
        print(MAZE[i][j], end="")
    print()

print("------------------------------------------------------------")  # 60個


move = "   aaa     , bbb   , ccc   ,   ddd    "
n1, n2, n3, n4 = move.split(",")

print(n1.strip(), end="|\n")
print(n2.strip(), end="|\n")
print(n3.strip(), end="|\n")
print(n4.strip(), end="|\n")

print("------------------------------------------------------------")  # 60個

print("assert的語法")

# Set up the constants:
SUSPECTS = [
    "DUKE HAUTDOG",
    "MAXIMUM POWERS",
    "BILL MONOPOLIS",
    "SENATOR SCHMEAR",
    "MRS. FEATHERTOSS",
    "DR. JEAN SPLICER",
    "RAFFLES THE CLOWN",
    "ESPRESSA TOFFEEPOT",
    "CECIL EDGAR VANDERTON",
]
ITEMS = [
    "FLASHLIGHT",
    "CANDLESTICK",
    "RAINBOW FLAG",
    "HAMSTER WHEEL",
    "ANIME VHS TAPE",
    "JAR OF PICKLES",
    "ONE COWBOY BOOT",
    "CLEAN UNDERPANTS",
    "5 DOLLAR GIFT CARD",
]
PLACES = [
    "ZOO",
    "OLD BARN",
    "DUCK POND",
    "CITY HALL",
    "HIPSTER CAFE",
    "BOWLING ALLEY",
    "VIDEO GAME MUSEUM",
    "UNIVERSITY LIBRARY",
    "ALBINO ALLIGATOR PIT",
]
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

print("------------------------------------------------------------")  # 60個

text = "王之渙涼州詞黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"
word1 = "春風"
word2 = "白雲"

count1 = text.count(word1)
print(word1, ":", count1, "個")

count2 = text.count(word2)
print(word2, ":", count2, "個")

print(text)

print("將", word1, "改成", word2)
text = text.replace(word1, word2)

print(text)


print("------------------------------------------------------------")  # 60個

import re

text = "這個是、那個是、那個是、哪個是"
word1 = "這.是"
word2 = ".個是"

pattern = re.compile(word1)
count = len(re.findall(pattern, text))
print(word1, ":", count, "個")

pattern = re.compile(word2)
count = len(re.findall(pattern, text))
print(word2, ":", count, "個")


import re

text = "這個是測試資料。"
word1 = ".個是"
word2 = "那個是"

print("置換前 :", text)
pattern = re.compile(word1)
text = re.sub(pattern, word2, text)
print("置換後 :", text)

print("------------------------------------------------------------")  # 60個

# 使用 json.dumps() 美觀列印 dict

import json

animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
    "蛇": 16,
}

print(type(animals))

print(json.dumps(animals, indent=4, sort_keys=True))


print("------------------------------------------------------------")  # 60個


"""
跟著阿才學Python從基礎到網路爬蟲應用


"""
print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch01\first.py

# -*- 第一個 Python 範例 -*-
"""
撰寫日期：2019-12-18
開發人員: 蔡文龍
程式版本：v1.0
"""
print("歡迎光臨 Python 的世界")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\in.py

print("1" in "123")  # 字串搜尋：判斷 "1" 是否在 "123" 內，成立顯示True
print("13" in "123")  # 字串搜尋：判斷 "13" 是否在 "123" 內，不成立顯示False
print("M" in "ASP.NET MVC")  # 字串搜尋：判斷 "M" 是否在 "ASP.NET MVC" 內，成立顯示True
print(7 not in [1, 2, 3])  # 串列搜尋：判斷 7 是否不在串列內，成立顯示True
print(1 not in [1, 2, 3])  # 串列搜尋：判斷 1 是否不在串列內，不成顯示False

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type01.py

num = 15  # 以十進制表示15
num0b = 0b1111  # 以二進制表示15
num0o = 0o17  # 以八進制表示15
num0x = 0xF  # 以十六進制表示15
print(num)  # 印出15，print()函式可印出指定的資料
print(num0b)  # 印出15
print(num0o)  # 印出15
print(num0x)  # 印出15

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type02.py

name = "小明"  # 也可以撰寫成 name="小明"，name為字串變數
score = 87.5  # score為浮點數變數
gender = True  # gender為布林變數
print("姓名 =", name)
print("分數 =", score)
print("性別(男:True, 女:False) =", gender)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type03.py

name = "小明"  # 也可以撰寫成 name="小明"，name為字串變數
score = 87.5  # score為浮點數變數
gender = True  # gender為布林變數
print("姓名 =", name)
print("分數 =", score)
print("性別(男:True, 女:False) =", gender)
print("姓名name變數型別 =", type(name))
print("分數score變數型別 =", type(score))
print("性別gender變數型別 =", type(gender))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format01.py

print("{:<5}".format(123))  # 顯示123ΔΔ
print("{:>5}".format(123))  # 顯示ΔΔ123
print("{:^6}".format(123))  # 顯示Δ123ΔΔ
print("{:@<6}".format(123))  # 顯示123@@@

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format02.py

print("{:#b}".format(12345))  # 顯示0b11000000111001
print("{:#o}".format(12345))  # 顯示0o30071
print("{:#x}".format(12345))  # 顯示0x3039

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format03.py

print("{:d}".format(12345))  # 顯示整數資料12345
print("{:7d}".format(12345))  # 設寬度為7,寬度有剩時補空格，顯示ΔΔ12345
print("{:s}".format("ABCDE"))  # 顯示字串資料，顯示ABCDE
print("{:>7s}".format("ABCDE"))  # 設寬度為7,寬度有剩時補空格，顯示ΔΔABCDE
print("{:f}".format(1234.567))  # 小數位數預設6位，顯示1234.567000
print("{:f}".format(-123.45))  # 小數位數預設6位，顯示-123.450000
print("{:.2f}".format(12.345))  # 指定小數位數2位,第3位四捨五入，顯示12.35
print("{:8.2f}".format(-12.3456))  # 指定總寬度8位,小數3位，顯示ΔΔ-12.35
print("{:3.1f}".format(123.45))  # 指定寬度為3且小數1位，寬度不足時全部顯示123.5
print("{:8.0f}".format(-1234.56))  # 指定小數位數0位,第1位四捨五入，顯示ΔΔΔ-1235
print("{:8.0f}".format(1234.56))  # 指定小數位數0位,第1位四捨五入，顯示ΔΔΔΔ1235
print("{:e}".format(123.4))  # 科學記號小數部分6位,小數位數不足補0 顯示1.234000e+02
print("{:10.2e}".format(12345.6))  # 指定總寬度10,小數2位，顯示ΔΔ1.23e+04


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\input01.py

name = input("輸入姓名：")
print("Hi!{}您好!".format(name))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\input02.py

amount = int(input("請輸入需繳費金額:"))
money = int(input("請輸入付款金額:"))

change = temp = money - amount  # change與temp為找零
n500 = change // 500  # change除於500取得500元張數再指定給n500
change = change % 500  # 求500元張數後剩於的找零
n100 = change // 100  # change除於100取得100元張數再指定給n100
change = change % 100  # 求100元張數後剩於的找零
n50 = change // 50  # change除於50取得50元個數再指定給n50
change = change % 50  # 求50元張數後剩於的找零
n10 = change // 10  # change除於10取得10元個數再指定給n10
change = change % 10  # 求10元張數後剩於的找零
n5 = change // 5  # change除於5取得5元個數再指定給n5
change = change % 5  # 求5元張數後剩於的找零
n1 = change // 1  # change除於1取得1元個數再指定給n1
print("收您{}元，找您{}元".format(money, temp))  # 顯示繳費金額與找零金額
print(
    "500元{}張\n100元{}張\n 50元{}個\n 10元{}個\n  5元{}個\n  1元{}個".format(
        n500, n100, n50, n10, n5, n1
    )
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print01.py

print("HOW", "ARE", "YOU")  # 顯示 "HOW ARE YOU"
greeting = "HOW ARE YOU?"
print(greeting)  # 顯示greeting變數的結果 "HOW ARE YOU?"
print("1+1=", 1 + 1)  # 顯示 1+1 運算式結果 2
print("HOW", "ARE", "YOU", sep="!")  # 顯示"HOW!ARE!YOU"
print("HOW", "ARE", "YOU", end="?")  # 顯示"HOW ARE YOU?"

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print02.py

print("早起的鳥兒'有蟲吃'\n")
print('晚起的鳥兒"被蟲吃"')
print("火影忍者\t博人傳")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print03.py

print("%07d" % 12345)  # 空格補零		ð 0012345
print("%-7d" % 12345)  # 靠左對齊		ð 12345ΔΔ
print("%#o" % 12345)  # 顯示八進制符號	ð 0x30071
print("%#x" % 12345)  # 顯示十六進制符號	ð 0x3039
print("% d" % 12345)  # 保留一個空格		ð Δ12345

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print04.py

print("%d" % (12345))  # 顯示整數資料		ð12345
print("%7d" % (12345))  # 設寬度為7,寬度有剩時補空格	ðΔΔ12345
print("%-7d" % (-12345))  # 靠左對齊,寬度有剩時補空格	ð-12345Δ
print("%07d" % (12345))  # 設寬度為7,寬度有剩時補0	ð0012345
print("%4d" % (-12345))  # 設寬度為3,寬度不足時全部顯示ð-12345
print("%c" % ("Y"))  # 顯示字元「Y」	ð Y
print("%4c" % ("Y"))  # 寬度為4有剩補空格	ðΔΔΔY
print("%c" % (97))  # 97的ASCII碼為a	ð a
print("%s" % ("ABCDE"))  # 顯示字串資料	ð ABCDE
print("%7s" % ("ABCDE"))  # 設寬度為7,寬度有剩時補空格	ðΔΔABCDE
print("%4s" % ("ABCDE"))  # 設寬度為4,寬度不足時全部顯示ð ABCDE
print("%6.3s" % ("ABCDE"))  # 設寬度為6並只顯示3字元	ðΔΔΔABC

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print05.py

print("%f" % 1234.567)  # 小數位數預設6位	ð1234.567000
print("%f" % -123.45)  # 小數位數預設6位	ð-123.450000
print("%.2f" % 12.345)  # 設小數位數2位,第3位四捨五入	ð12.35
print("%8.2f" % -12.3456)  # 設總寬度8位,小數3位		ðΔΔ-12.35
print("%3.1f" % 123.45)  # 設寬度為3且小數1位，寬度不足時全部顯示	ð123.5
print("%8.0f" % -1234.56)  # 設小數位數0位,第1位四捨五入	ðΔΔΔ-1235
print("%8.0f" % 1234.56)  # 設小數位數0位,第1位四捨五入	ðΔΔΔΔ1235
print("%e" % 123.4)  # 科學記號小數部分6位,小數位數不足補0 ð1.234000e+02
print("%10.2e" % 12345.6)  # 設總寬度10,小數2位	ðΔΔ1.23e+04


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print06.py

print("%4s%6s%4s%4s" % ("玩家", "體力", "職業", "技能"))
print("=========================")
print("%3s%8d%4s%4s" % ("王大明", 88, "騎士", "劈砍"))
print("%3s%8d%4s%4s" % ("李小王", 10, "新手", "無"))
print("%3s%8d%4s%4s" % ("林老大", 100, "團長", "斬殺"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if01.py

score = 89
show = "不及格"  # 預設show字串變數是"不及格"
if score > 60:
    show = "Pass"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if02.py

score = 59
if score >= 60:
    show = "Pass"  # score大於等於60，show指定為 "Pass"
else:
    show = "不及格"  # score小於60，show指定為 "不及格"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if03.py

uid = input("請輸入帳號：")
pw = input("請輸入密碼：")
if uid == "dtc" and pw == "168":
    show = "帳密正確，歡迎進入系統"
else:
    show = "帳密錯誤，無法使用系統"
print(show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if04.py

score = int(input("請輸入成績："))  # 輸入成績再轉成整數並指定給score
if score >= 0 and score <= 100:  # 判斷score是否介於0~100之間
    if score >= 60:
        show = "Pass"  # score大於等於60 指定show為 "Pass"
    else:
        show = "不及格"  # score小於60 指定show為 "不及格"
else:
    show = "應介於0~100之間"  # score沒有介於0~100之間 ， show指定為 "應介於0~100之間
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if05.py

score = int(input("請輸入成績："))  # 輸入成績再轉成整數並指定給score
if score >= 0 and score <= 100:  # 判斷score是否介於0~100之間
    if score >= 90:
        show = "優等"  # score介於100~90時，show指定 "優等"
    elif score >= 80:
        show = "甲等"  # score介於89~80時，show指定 "甲等"
    elif score >= 70:
        show = "乙等"  # score介於79~70時，show指定 "乙等"
    elif score >= 60:
        show = "丙等"  # score介於69~60時，show指定 "丙等"
    else:
        show = "不及格"  # score介於59~0時，show指定 "不及格"
else:
    show = "應介於0~100之間"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if06.py

print("==動物英文單字查詢==")
print("1. 獅子")
print("2. 老虎")
print("3. 大象")
print("4. 免子")
num = int(input("請輸入選項編號："))  # 輸入數字轉成整數並指定給num

if num >= 1 and num <= 4:  # 判斷num是否介於1~4之間
    if num == 1:
        show = "獅子：lion"  # num等於1，show指定 "獅子：lion"
    elif num == 2:
        show = "老虎：tiger"  # num等於2，show指定 "老虎：tiger""
    elif num == 3:
        show = "大象：elephant"  # num等於3，show指定 "大象：elephant"
    elif num == 4:
        show = "免子：rabbit"  # num等於4，show指定 "免子：rabbit"
else:
    show = "選項應介於1~4之間"

print(show)  # 顯示show的結果

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list01.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
print(name)  # 印出 ['小明', '小華', '小強', '小莉']
print(score)  # 印出 [67, 56, 12, 99]


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list02.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
print("{}的成績 {}".format(name[0], score[0]))
print("{}的成績 {}".format(name[1], score[1]))
print("{}的成績 {}".format(name[2], score[2]))
print("{}的成績 {}".format(name[3], score[3]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list03.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
for i in range(4):
    print("{}的成績 {}".format(name[i], score[i]))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list04.py

listSport = ["爬山", "游泳", "跑步"]
print(listSport[0])  # 顯示"爬山"
print(listSport[-3])  # listSport[-3] 表示串列listSport倒數第3個串列元素，顯示 "爬山"
print(listSport[2])  # listSport[2] 表示串列listSport第3個串列元素，顯示 "跑步"
print(listSport[-1])  # listSport[-1] 表示l串列istSport倒數第1個串列元素，顯示 "跑步"

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list05.py

listSport = ["爬山", "游泳", "跑步", "舉重", "飛輪", "跳水", "瑜珈"]
print(listSport[1:5])  # [1:5] 表示第2到第5個串列元素，顯示 ['游泳', '跑步', '舉重', '飛輪']
print(listSport[:4])  # [:4] 表示第1到第4個串列元素，顯示['爬山', '游泳', '跑步', '舉重']
print(listSport[1:6:2])  # [1:6:2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']
print(listSport[6:1:-2])  # [6:1:-2] 表示第7、5、3個串列元素，顯示['瑜珈', '飛輪', '跑步']
print(listSport[1::2])  # [1::2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\listfunc01.py

listScore = [78, 45, 99, 56, 96]
count = len(listScore)
avg = sum(listScore) / count
print("%d 位學生成績：%s" % (count, listScore))
print("最高成績： %d" % max(listScore))
print("最低成績： %d" % min(listScore))
print("加總成績： %d" % sum(listScore))
print("平均成績： %d" % avg)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\listfunc02.py

listScore = []
listScore.append(int(input("第 1 位學生成績：")))
listScore.append(int(input("第 2 位學生成績：")))
listScore.append(int(input("第 3 位學生成績：")))
listScore.append(int(input("第 4 位學生成績：")))

print("成績列表：", listScore)
listScore.sort()
print("遞增排序：", listScore)
listScore.reverse()
print("遞減排序：", listScore)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\product01.py

pid = ["E01", "E02", "E03", "E04"]
name = ["碁峰可樂", "阿才肉乾", "龍哥豆漿", "五香牛肉"]
price = [100, 690, 25, 300]
num = int(input("查詢第幾項產品(1~4)："))
if num >= 1 and num <= 4:
    index = num - 1
    print("編號：%s" % pid[index])
    print("品名：%s" % name[index])
    print("單價：%d" % price[index])
else:
    print("無第 %d 項產品" % num)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\product02.py

product = [
    ["E01", "碁峰可樂", 100],
    ["E02", "阿才肉乾", 690],
    ["E03", "龍哥豆漿", 25],
    ["E04", "五香牛肉", 300],
]
num = int(input("查詢第幾項產品(1~4)："))
if num >= 1 and num <= 4:
    index = num - 1
    print("編號：%s" % product[index][0])
    print("品名：%s" % product[index][1])
    print("單價：%d" % product[index][2])
else:
    print("無第 %d 項產品" % num)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist01.py

member = [
    ["E01", "王小明", "男", 25000],
    ["E02", "曾美麗", "女", 18000],
    ["E03", "莊聰明", "男", 20000],
]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0])  # 印出第1筆會員記錄
print(member[1])  # 印出第2筆會員記錄
print(member[2])  # 印出第3筆會員記錄


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist02.py

member = [None, None, None]  # 建立member二維串列，串列中的三個元素為None
member[0] = ["E01", "王小明", "男", 25000]
member[1] = ["E02", "曾美麗", "女", 18000]
member[2] = ["E03", "莊聰明", "男", 20000]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0])
print(member[1])
print(member[2])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist03.py

member = [
    ["E01", "王小明", "男", 25000],
    ["E02", "曾美麗", "女", 18000],
    ["E03", "莊聰明", "男", 20000],
]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0][0], member[0][1], member[0][2], member[0][3])
print(member[1][0], member[1][1], member[1][2], member[1][3])
print(member[2][0], member[2][1], member[2][2], member[2][3])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\break01.py

# pid串列存放產品編號
pid = ["A01", "A02", "A03"]
# name串列存放產品名稱
name = ["PS4 特價包", "Switch", "Xbox One"]
# price串列存放產品單價
price = [9980, 12999, 11000]

inputId = input("請輸入欲查詢的產品編號：")

index = -1  # index串列索引為-1表示找不到
count = len(pid)  # len()函式取得name串列個數並指定給count
# count等於3，因此range(count)會產生[0, 1, 2]串列
# for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):
    if inputId == pid[i]:
        index = i  # 若有找到資料將i指定給index
        break  # 離開迴圈
# 若index等於-1表示找不到資料
if index == -1:
    print("找不到資料")
else:
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" % (pid[index], name[index], price[index]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\continue01.py

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print("%d不是3的倍數" % (i))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\createProduct.py

product = []
count = int(input("請輸入產品建檔數量："))

i = 0
while i < count:
    print("第 %d 項產品資訊" % (i + 1))
    temp = []
    temp.append((input("編號：")))
    temp.append((input("品名：")))
    temp.append((input("單價：")))
    product.append(temp)
    i += 1

print("\n產品資訊如下：")
for row in product:  # 印出每列
    for col in row:  # 印出每欄
        print(col, end="\t")
    print()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for01.py

for i in range(1, 6):
    print(i, end=",")
print()

for i in range(5, 0, -1):
    print(i, end=",")
print()

sum = 0
for i in range(1, 100, 2):
    sum += i
print("1+3+5+...<100=%d" % sum)

program = ["Python", "Java", "C#", "C++"]
for s in program:
    print(s, end=",")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for02.py

name = [
    "PS4 Slim主機 CUH-2117",
    "任天堂 Nintendo Switch",
    "Xbox One S 500G同捆組",
]  # name串列存放產品名稱
price = [9980, 12999, 11000]  # price串列存放產品單價
# len()函式取得name串列個數並指定給count
count = len(name)
# count等於3，因此range(count)會產生[0, 1, 2]串列
# for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):
    print("%s \t" % name[i], end="")  # 印出產品
    print("單價%d元" % price[i])  # 印出單價


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for03.py

listScore = []  # 建立listScore為空串列
count = int(input("請輸入學生數："))  # 指定學生數
# 輸入學生成績並逐一放入listScore串列，append()方法可將資料附加到串列中
for i in range(count):
    print("第 %d 位學生：" % (i + 1), end="")
    listScore.append(int(input("")))

print("成績列表：", listScore)  # 顯示listScore所有元素
listScore.sort()  # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)  # 印出listScore由小到大排序的結果
listScore.reverse()  # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)  # 印出listScore由大到小排序的結果


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\forelse01.py

# 執行三次
for i in range(3):
    print("第 %d 次帳密驗證：" % (i + 1), end="")
    uid = input(" 帳號：")  # 將帳號指定給uid
    pw = input(" 密碼：")  # 將密碼指定給pw
    if uid == "dtc" and pw == "168":
        print("帳密正確，歡迎進入系統")
        break
else:
    print()
    print("3 次帳密錯誤，無法使用系統")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\nestLoop01.py

for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%2d" % (i, j, (i * j)), end=";  ")
    print()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\nestLoop02.py

name = ["小明", "小華", "小莉", "小呆"]  # 姓名
score = [[77, 66, 88], [83, 92, 56], [90, 98, 79], [89, 81, 70]]  # 成績
print("姓名   國文   英文   數學   總分")
print("================================")
for i in range(len(name)):
    print("%s" % name[i], end="   ")
    sum = 0
    for j in range(len(score[i])):
        print("%3d" % score[i][j], end="    ")
        sum += score[i][j]
    print("%3d" % sum)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\while01.py

# name串列存放產品名稱
name = ["PS4 Slim主機 CUH-2117", "任天堂 Nintendo Switch", "Xbox One S 500G同捆組"]
# price串列存放產品單價
price = [9980, 12999, 11000]
# len()函式取得name串列個數並指定給count
count = len(name)
# count等於3，range(count)會產生0, 1, 2串列，for迴圈中的i會逐一被指定為0, 1, 2
i = 0  # i起始為0
while i < count:
    print("%s \t" % name[i], end="")  # 印出產品
    print("單價%d元" % price[i])  # 印出單價
    i += 1

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\while02.py

listScore = []  # 建立listScore為空串列
count = int(input("請輸入學生數："))  # 指定學生數
# 輸入學生成績並逐一放入listScore串列，append()方法可將資料附加到串列中
i = 0
while i < count:
    print("第 %d 位學生：" % (i + 1), end="")
    listScore.append(int(input("")))
    i += 1

print("成績列表：", listScore)  # 顯示listScore所有元素
listScore.sort()  # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)  # 印出listScore由小到大排序的結果
listScore.reverse()  # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)  # 印出listScore由大到小排序的結果


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\whileelse01.py

i = 1  # i起始值為1
# 執行三次
while i <= 3:
    print("第 %d 次帳密驗證：" % i, end="")
    uid = input(" 帳號：")  # 將帳號指定給uid
    pw = input(" 密碼：")  # 將密碼指定給pw
    if uid == "dtc" and pw == "168":
        print("帳密正確，歡迎進入系統")
        break
    i += 1
else:
    print()
    print("3 次帳密錯誤，無法使用系統")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\callReference.py


def CallReference(x):
    for i in range(len(x)):
        x[i] += 10
    print("函式呼叫中：x位址={}, x={}".format(id(x), x))


a = [1, 2, 3, 4]
print("函式呼叫前：a位址={}, a={}".format(id(a), a))
CallReference(a)
print("函式呼叫後：a位址={}, a={}".format(id(a), a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\callValue.py


def CallValue(x):
    x += 10
    print("函式呼叫中：x位址=%d, x=%d" % (id(x), x))


a = 6
print("函式呼叫前：a位址=%d, a=%d" % (id(a), a))
CallValue(a)
print("函式呼叫後：a位址=%d, a=%d" % (id(a), a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func01.py


# 定義Hello()函式
def Hello():
    print("Hello!大家好")


Hello()  # 呼叫Hello()函式，結果顯示 “Hello!大家好”


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func02.py


# 定義HelloByName()函式，可接收name參數
def HelloByName(name):
    print("Hello!大家好, 我是", name)


HelloByName("王小明")  # 呼叫Hello()函式並傳入 "王小明" 參數
HelloByName("李小華")  # 呼叫Hello()函式並傳入 "李小華" 參數


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func03.py


# 定義HelloByName()函式，可接收name和gender參數
def HelloByName(name, gender):
    if gender:
        str = "先生"
    else:
        str = "小姐"
    print("Hello!大家好, 我是", name, str)


HelloByName("王小明", True)  # 呼叫Hello()函式並傳入 "王小明" 和 True 參數
HelloByName("李小華", False)  # 呼叫Hello()函式並傳入 "李小華" 和 False 參數


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func04.py


# 定義GetRoundArea函式，可傳入radius半徑，並傳回圓面積
def GetRoundArea(radius):
    # 傳回圓面積，圓面積公式為 半徑 *  半徑 * 3.14
    return radius * radius * 3.14


r = int(input("請輸入半徑："))
RoundArea = GetRoundArea(r)
print("圓形半徑 %d，面積為 %d" % (r, RoundArea))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func05.py


# 定義GetMax()函式，可傳回n1和n2兩數的最大數
def GetMax(n1, n2):
    if n1 > n2:
        vMax = n1
    else:
        vMax = n2
    return vMax


Max = GetMax(70, 9)
print("70和 9最大值為", Max)
print("17和30最大值為", GetMax(17, 30))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func06.py


# 定義Sort()函式，此函式可將傳入的三個數值進行由小到大排序， 並將排序後的結果傳回
def Sort(x, y, z):
    # 判斷三個數的大小，並做調整
    if x > y:
        t = x
        x = y
        y = t
    if y > z:
        t = y
        y = z
        z = t
    if x > z:
        t = x
        x = z
        z = t
    return x, y, z


# 將輸入的數值1~數值3依序放到a, b, c三個變數
a = int(input("數值1："))
b = int(input("數值2："))
c = int(input("數值3："))
# 呼叫Sort()函式傳入a, b, c三個數，最後將由小到大排序的結果依序指定給a, b, c
a, b, c = Sort(a, b, c)
print("\n由小到大排序：%d %d %d" % (a, b, c))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\funcAry01.py


def GetMax(ary):
    maxNum = ary[0]
    index = 0
    for i in range(len(ary)):
        if maxNum < ary[i]:
            index = i
            maxNum = ary[index]
    return index


listName = ["阿才肉乾", "恐龍餅乾", "快樂汽水", "天天豆干"]
listPrice = [70, 230, 400, 240]

for i in range(len(listName)):
    print("%s %d" % (listName[i], listPrice[i]))
print()
n = GetMax(listPrice)
print("最貴產品：%s, 單價：%d" % (listName[n], listPrice[n]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\random01.py

import random

for i in range(5):
    print("第 %d 個亂數：%d" % (i + 1, random.randint(1, 10)))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\random02.py

import random  # 引用random亂數套件

#  將 1~49 的整數放入num串列中
num = []
for i in range(49):
    num.append(i + 1)
# 使用 random套件的sample函式由num中隨機取得不重複的7個元素
lot = random.sample(num, 7)

print("大樂透  號碼：", end="")
# 印出 lot[0]~lot[5]
for i in range(6):
    print(lot[i], end=", ")

print()
print("大樂透特別號：%2d" % (lot[6]))  # 印出 lot[6]


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\var01.py


def func():
    n = 10
    print("區域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
func()
print("全域變數n 位址=%d, 值=%d" % (id(n), n))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\var02.py


def func():
    global n
    n = 10
    print("函式內 全域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))
func()
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))


print("------------------------------------------------------------")  # 60個

# dict01.py

dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print(dictBook)
# 印出 dictBook所有元素
print("書號A001：", dictBook["A001"])  # 印出dictBook字典鍵A001的值 ['木偶奇遇記', 199]
print("書號A002：", dictBook["A002"])  # 印出dictBook字典鍵A002的值 ['三隻小豬', 120]
print("書號A003：", dictBook["A003"])  # 印出dictBook字典鍵A003的值 ['白雪公主', 99]


print("------------------------------------------------------------")  # 60個

# dict02.py

tupleBookId = ("A001", "A002", "A003")
dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print("書號\t書名\t單價")
print("========================")

for key in list(tupleBookId):
    print(key, end="\t")
    for col in dictBook[key]:
        print(col, end="\t")
    print()


print("------------------------------------------------------------")  # 60個

# dict03.py

dictBook = {"A001": ["木偶奇遇記", 199]}
print("編輯前字典內容：", dictBook)

dictBook["A002"] = ["三隻小豬", 120]
print("新增後字典內容：", dictBook)

dictBook["A002"] = ["白雪公主", 120]
print("修改後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)

del dictBook["A001"]
print("刪除後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)


print("------------------------------------------------------------")  # 60個

# dictGame.py

import random

bossHp = 100
listPcCard = [["青眼白龍", 20], ["紅髮女妖", 11], ["白骷髏王", 9], ["碧眼狐怪", 12]]
random.shuffle(listPcCard)
dictMyCard = dict(listPcCard)

while True:
    n = int(input("功能選項：1.抽卡攻擊 2.補齊卡牌 3.目前卡牌 4.離開遊戲："))
    if n == 1:
        if not dictMyCard:
            print("目前沒有卡牌，請補卡牌")
            continue
        card = dictMyCard.popitem()
        listCard = list(card)
        cardName = listCard[0]
        cardAttack = listCard[1]
        bossHp -= cardAttack
        if bossHp <= 0:
            bossHp = 0
            print("%s最後一擊 %d 點\t魔王血量歸 %d，成功過關" % (cardName, cardAttack, bossHp))
            break
        print("使用%s攻擊 %d 點\t魔王目前血量：%d" % (cardName, cardAttack, bossHp))
    elif n == 2:
        random.shuffle(listPcCard)
        dictMyCard = dict(listPcCard)
        print("完成補齊卡牌!")
    elif n == 3:
        print("目前卡牌：", dictMyCard)
    elif n == 4:
        break
    else:
        print("無此選項功能!")

print("------------------------------------------------------------")  # 60個

# ProductSys.py


# 新增
def fnCreate():
    uid = input("編號：")
    if uid in dictProduct:
        print("編號重複，無法新增產品記錄")
        return
    name = input("品名：")
    price = int(input("單價："))
    newProduct = {uid: [name, price]}
    dictProduct.update(newProduct)
    print("產品新增成功!")


# 修改
def fnUpdate():
    uid = input("編號：")
    if uid not in dictProduct:
        print("無此編號，無法修改產品記錄")
        return
    name = input("品名：")
    price = int(input("單價："))
    dictProduct[uid] = [name, price]
    print(dictProduct)
    print("產品修改成功!")


# 刪除
def fnDelete():
    uid = input("編號：")
    if uid not in dictProduct:
        print("無此編號，無法刪除產品記錄")
        return
    dictProduct.pop(uid)
    print("產品刪除成功!")


# 依編號查詢產品
def fnGetProductById():
    uid = input("編號：")
    if uid not in dictProduct:
        print("查無此編號")
        return
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" % (uid, dictProduct[uid][0], dictProduct[uid][1]))


# 將所有產品列出
def fnGetProductList():
    print("編號\t品名\t單價")
    listKey = dictProduct.keys()
    for uid in listKey:
        print("%s\t%s\t%d" % (uid, dictProduct[uid][0], dictProduct[uid][1]))


# 主程式
dictProduct = {}
print("======= DTC產品管理系統 =======")
while True:
    option = int(input("系統功能->1.新增 2.修改 3.刪除 4.查詢 5.產品列表 其他.離開："))
    if option == 1:
        fnCreate()
    elif option == 2:
        fnUpdate()
    elif option == 3:
        fnDelete()
    elif option == 4:
        fnGetProductById()
    elif option == 5:
        fnGetProductList()
    else:
        print("離開系統")
        break

print("------------------------------------------------------------")  # 60個

# tuple01.py

tupleFruit = ("apple", "banana", "cherry")  # 建立tupleFruit元組用來存放水果英文名稱
tupleNum = (1, 2, 3, 4, 5)  # 建立tupleNum元組用來存放1~5整數
tupleBool = (True, False)  # 建立tupleBool元組用來存放布林值True|False
tupleProduct = ("P01", "五香豆干", 45)  # 建立tupleProduct元組用來存放產品資訊
print(tupleFruit)  # 顯示 ('apple', 'banana', 'cherry')
print(tupleNum)  # 顯示 (1, 2, 3, 4, 5)
print(tupleBool)  # 顯示 (True, False)
print(tupleProduct)  # 顯示 ('P01', '五香豆干', 45)

print("------------------------------------------------------------")  # 60個

# tuple02.py

tupleScore = (89, 87, 36, 55, 94)
tupleName = ("小明", "小華", "小強", "小保", "小呆")
print("****DTC大學-學生績表****")
print("姓名\t分數")
print("=======================")
for i in range(len(tupleScore)):
    print("%s\t%d" % (tupleName[i], tupleScore[i]))
print("=======================")
print("  最高分：%d" % max(tupleScore))
print("  最低分：%d" % min(tupleScore))
print("平均分數：%.2f" % (sum(tupleScore) / len(tupleScore)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
