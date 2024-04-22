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
import math
import random

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

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出 忠實保留雙引號內的資料內容")
print(str2)

print("------------------------------------------------------------")  # 60個

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

x = 12345678
print("/%10.1e/" % x)
print("/%10.2E/" % x)
print("/%-10.2E/" % x)
print("/%+10.2E/" % x)
print("=" * 60)
string = "abcdefg"
print("/%10.3s/" % string)

print("------------------------------------------------------------")  # 60個

print('置換網址資料')
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type_ = "school"
print(url + city + '&radius=' + str(r) + '&type=' + type_)
print(url + "{}&radius={}&type={}".format(city, r, type_))

print("------------------------------------------------------------")  # 60個

print('置換網址資料')
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type_ = "school"
my_url = url + f"{city}&radius={r}&type={type_}"
print(my_url)

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

print("字串的處理")

print("字串的處理 split")

str1 = "Silicon Stone Education"
str2 = "D:\Python\ch6"

sList1 = str1.split()  # 字串轉成串列
sList2 = str2.split("\\")  # 字串轉成串列
print(f"{str1} 串列內容是 {sList1}")  # 列印串列
print(f"{str1} 串列字數是 {len(sList1)}")  # 列印字數
print(f"{str2} 串列內容是 {sList2}")  # 列印串列
print(f"{str2} 串列字數是 {len(sList2)}")  # 列印字數

print("------------------------------------------------------------")  # 60個

print("字串的處理 join")

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

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
lst = list(enumerate_drinks)
print("轉成串列輸出, 初始索引值是 0 = ", lst)
print(type(lst[0]))

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

fruits = ("apple", "banana", "cherry", "date", "cherry")
print(f"fruits 元組長度是 {len(fruits)}")  # 輸出 5

index = fruits.index("cherry")
print(f"cherry 索引位置是 {index}")  # 輸出 2

cherry_count = fruits.count("cherry")
print(f"cherry 出現次數是 {cherry_count}")  # 輸出 2

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

mydict = {"name": "Hung", "age": 25, "city": "New York"}
for key in mydict:
    print(f"{key} : {mydict[key]}")

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

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25}
noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
print("水蜜桃一斤 = ", fruits["水蜜桃"], "元")
print("牛肉麵一碗 = ", noodles["牛肉麵"], "元")

print("------------------------------------------------------------")  # 60個

noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item: item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")


print("------------------------------------------------------------")  # 60個

noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item: item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")


print("------------------------------------------------------------")  # 60個


# 建立內含字串的字典
sports = {"Curry": ["籃球", "美式足球"], "Durant": ["棒球"], "James": ["美式足球", "棒球", "籃球"]}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items():
    print(f"{name} 喜歡的運動是: ")
    # 列印value,這是串列
    for sport in favorite_sport:
        print(f"   {sport}")


print("------------------------------------------------------------")  # 60個

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

fruits = {"Apple": 20, "Orange": 25}
ret_value1 = fruits.get("Orange")
print(f"Value = {ret_value1}")
ret_value2 = fruits.get("Grape")
print(f"Value = {ret_value2}")
ret_value3 = fruits.get("Grape", 10)
print(f"Value = {ret_value3}")


print("------------------------------------------------------------")  # 60個

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

word = "deepmind"
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
print(alphabetCount)

print("------------------------------------------------------------")  # 60個

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

"""
# test locals()
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

# 加總一系列數字


def my_sum(*numbers):
    output = 0
    for n in numbers:
        output += n
    return output


print(my_sum(10, 20, 30, 40, 50))

print("------------------------------------------------------------")  # 60個

# 豬拉丁文


def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


print(pig_latin("python"))

print("------------------------------------------------------------")  # 60個

# 豬拉丁文 --- 句子翻譯機

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

# 擷取和合併多種容器的頭尾元素


def first_last(seq):
    return seq[:1] + seq[-1:]


print(first_last("abcde"))
print(first_last([1, 2, 3, 4, 5]))

print("------------------------------------------------------------")  # 60個

# 萬用加總函式


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

# 依姓名排序聯絡資料

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

# 降雨量資料庫

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

# 有幾個不重複的數字?


def unique_num_len(numbers):
    return len(set(numbers))


numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(unique_num_len(numbers))

print("------------------------------------------------------------")  # 60個

# XML 產生器


def myxml(tag, content="", **kwargs):
    attrs_list = []
    for key, value in kwargs.items():
        attrs_list.append(f' {key}="{value}"')
    attrs = "".join(attrs_list)
    return f"<{tag}{attrs}>{content}</{tag}>"


print(myxml("foo", "bar", a=1, b=2, c=3))

print("------------------------------------------------------------")  # 60個

# 輸出一組數字的絕對值


def abs_numbers(numbers):
    # return [abs(x) for x in numbers]
    return list(map(abs, numbers))


print(abs_numbers([1, -2, 3, -4, 5]))

print("------------------------------------------------------------")  # 60個

# 只加總資料中的數字


def sum_numbers(data):
    return sum([int(d) for d in data.split() if d.isdigit()])


print(sum_numbers("10 abc 20 de44 30 55fg 40"))

print("------------------------------------------------------------")  # 60個

# 用巢狀生成式『壓平』二維 list


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

# 動物類別


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

# 動物展示區類別


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

# 動物園類別


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

# 自訂列舉容器


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

# 循環取值器


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

# 產生器運算式


def num_generator(num):
    return (int(digit) for digit in str(num) if digit.isnumeric())


numbers = num_generator(3.14159)

for num in numbers:
    print(num)

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
    #檢查是否是搜尋的字串
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

import numpy as np
import math

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

print('in, not in 的用法')
print("1" in "123")  # 字串搜尋：判斷 "1" 是否在 "123" 內，成立顯示True
print("13" in "123")  # 字串搜尋：判斷 "13" 是否在 "123" 內，不成立顯示False
print("M" in "ASP.NET MVC")  # 字串搜尋：判斷 "M" 是否在 "ASP.NET MVC" 內，成立顯示True
print(7 not in [1, 2, 3])  # 串列搜尋：判斷 7 是否不在串列內，成立顯示True
print(1 not in [1, 2, 3])  # 串列搜尋：判斷 1 是否不在串列內，不成顯示False

print("------------------------------------------------------------")  # 60個

print('不同進制表示數字')

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

print("{:<5}".format(123))  # 顯示123ΔΔ
print("{:>5}".format(123))  # 顯示ΔΔ123
print("{:^6}".format(123))  # 顯示Δ123ΔΔ
print("{:@<6}".format(123))  # 顯示123@@@

print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('進位轉換')

number = 255
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

x1 = "22"
x2 = "33"
x3 = x1 + x2
x4 = int(x1) + int(x2)
x5 = "11111111"
print("2進位  '11111111' = ", int(x5, 2))
print("8進位  '22'   = ", int(x1, 8))
print("16進位 '22'   = ", int(x1, 16))
print("16進位 'FF'   = ", int("FF", 16))

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

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

# 將 16 進位數轉為 10 進位

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

print("{:#b}".format(12345))  # 顯示0b11000000111001
print("{:#o}".format(12345))  # 顯示0o30071
print("{:#x}".format(12345))  # 顯示0x3039

print("------------------------------------------------------------")  # 60個

#改成動物資料
print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print("------------------------------------------------------------")  # 60個

#改成動物資料
listScore = []  # 建立listScore為空串列

listScore.append(int(input("")))

print("成績列表：", listScore)  # 顯示listScore所有元素
listScore.sort()  # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)  # 印出listScore由小到大排序的結果
listScore.reverse()  # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)  # 印出listScore由大到小排序的結果

#改成動物資料
soldier0 = {"tag": "red", "score": 3, "speed": "slow"}  # 建立小兵
soldier1 = {"tag": "blue", "score": 5, "speed": "medium"}
soldier2 = {"tag": "green", "score": 10, "speed": "fast"}
armys = [soldier0, soldier1, soldier2]  # 小兵組成串列
for army in armys:  # 列印小兵
    print(army)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

listScore = [78, 45, 99, 56, 96]
count = len(listScore)
avg = sum(listScore) / count
print("%d 位學生成績：%s" % (count, listScore))
print("最高成績： %d" % max(listScore))
print("最低成績： %d" % min(listScore))
print("加總成績： %d" % sum(listScore))
print("平均成績： %d" % avg)


cname = '米老鼠'
message = f"中文名{cname}"
print(message)

print("------------------------------------------------------------")  # 60個

listScore = []
listScore.append(55)
listScore.append(88)
listScore.append(33)
listScore.append(77)

print("成績列表：", listScore)
listScore.sort()
print("遞增排序：", listScore)
listScore.reverse()
print("遞減排序：", listScore)

print('二維list')
product = [
    ["E01", "碁峰可樂", 100],
    ["E02", "阿才肉乾", 690],
    ["E03", "龍哥豆漿", 25],
    ["E04", "五香牛肉", 300],
]

index = 2
print("編號：%s" % product[index][0])
print("品名：%s" % product[index][1])
print("單價：%d" % product[index][2])

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

# 方法1
animals = set("鼠牛虎兔龍")
print("兔 是屬於animals集合?", "兔" in animals)
print("豬 是屬於animals集合?", "豬" in animals)
# 方法2
animals = {"鼠", "牛", "虎", "兔", "龍"}
boolean = "兔" in animals
print("兔 in animals :", boolean)
boolean = "豬" in animals
print("豬 in animals :", boolean)

print("------------------------------------------------------------")  # 60個

animals1 = ["鼠", "牛", "虎", "兔", "龍"]
animals2 = ["牛", "豬", "虎"]
print("目前animals2串列 : ", animals2)
for animal in animals2[:]:
    if animal in animals1:
        animals2.remove(animal)
        print(f"刪除 {animal}")
print("最後animals2串列 : ", animals2)

print("------------------------------------------------------------")  # 60個

# 供應商 A 和 B 的產品列表
supplier_a_products = {"apple", "banana", "cherry", "date", "elderberry"}
supplier_b_products = {"banana", "cherry", "fig", "grape"}

# 找到共同產品
common_products = supplier_a_products.intersection(supplier_b_products)
print(f"共同產品 : {common_products}")

# 找到只由供應商 A 提供的獨特產品
unique_to_a = supplier_a_products - supplier_b_products
print(f"供應商 A 的獨特產品 : {unique_to_a}")

# 找到只由供應商 B 提供的獨特產品
unique_to_b = supplier_b_products - supplier_a_products
print(f"供應商 B 的獨特產品 : {unique_to_b}")

# 所有提供的產品
all_products = supplier_a_products.union(supplier_b_products)
print(f"所有產品 : {all_products}")

print("------------------------------------------------------------")  # 60個


def kitchen(unserved, served):
    """將未服務的餐點轉為已經服務"""
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop()
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()


def show_unserved_meal(unserved):
    """顯示尚未服務的餐點"""
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)


def show_served_meal(served):
    """顯示已經服務的餐點"""
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)


unserved = ["大麥克", "可樂", "麥克雞塊"]  # 所點餐點
served = []  # 已服務餐點
# 列出餐廳處理前的點餐內容
show_unserved_meal(unserved)  # 列出未服務餐點
show_served_meal(served)  # 列出已服務餐點
# 餐廳服務過程
kitchen(unserved, served)  # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_unserved_meal(unserved)  # 列出未服務餐點
show_served_meal(served)  # 列出已服務餐點

print("------------------------------------------------------------")  # 60個


def kitchen(unserved, served):
    """將未服務的餐點轉為已經服務"""
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop()
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()


def show_unserved_meal(unserved):
    """顯示尚未服務的餐點"""
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)


def show_served_meal(served):
    """顯示已經服務的餐點"""
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)


order_list = ["大麥克", "可樂", "麥克雞塊"]  # 所點餐點
served_list = []  # 已服務餐點
# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)  # 列出未服務餐點
show_served_meal(served_list)  # 列出已服務餐點
# 餐廳服務過程
kitchen(order_list, served_list)  # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)  # 列出未服務餐點
show_served_meal(served_list)  # 列出已服務餐點

print("------------------------------------------------------------")  # 60個


def kitchen(unserved, served):
    """將未服務的餐點轉為已經服務"""
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop()
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()


def show_order_meal(unserved):
    """顯示所點的餐點"""
    print("=== 下列是所點的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)


def show_served_meal(served):
    """顯示已經服務的餐點"""
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)


order_list = ["大麥克", "可樂", "麥克雞塊"]  # 所點餐點
served_list = []  # 已服務餐點
# 列出餐廳處理前的點餐內容
show_order_meal(order_list)  # 列出所點的餐點
show_served_meal(served_list)  # 列出已服務餐點
# 餐廳服務過程
kitchen(order_list[:], served_list)  # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_order_meal(order_list)  # 列出所點的餐點
show_served_meal(served_list)  # 列出已服務餐點

print("------------------------------------------------------------")  # 60個


def build_dict(name, age, **players):
    """建立NBA球員的字典資料"""
    info = {}  # 建立空字典
    info["Name"] = name
    info["Age"] = age
    for key, value in players.items():
        info[key] = value
    return info  # 回傳所建的字典


player_dict = build_dict("James", "32", City="Cleveland", State="Ohio")

print(player_dict)  # 列印所建字典

print("------------------------------------------------------------")  # 60個


def dist(x1, y1, x2, y2):  # 計算2點之距離函數
    def mySqrt(z):  # 計算開根號值
        return z**0.5

    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mySqrt(dx + dy)


print(dist(0, 0, 1, 1))

print("------------------------------------------------------------")  # 60個


def outer():
    def inner(n):
        print("inner running")
        return sum(range(n))

    return inner


f = outer()  # outer()傳回inner位址
print(f)  # 列印inner記憶體
print(f(5))  # 實際執行的是inner()

y = outer()
print(y)
print(y(10))

print("------------------------------------------------------------")  # 60個


def create_multiplier(multiplier):
    def multiplier_function(number):
        return number * multiplier

    return multiplier_function


# 建立一個將數字乘以2的函數
double_function = create_multiplier(2)

result = double_function(5)  # 返回值是 10
print(result)  # 輸出: 10

# 建立一個將數字乘以3的函數
triple_function = create_multiplier(3)

result = triple_function(5)  # 返回值是 15
print(result)  # 輸出: 15

print("------------------------------------------------------------")  # 60個


def outer():
    b = 10  # inner所使用的變數值

    def inner(x):
        return 5 * x + b  # 引用第3列的b

    return inner


b = 2
f = outer()
print(f(b))

print("------------------------------------------------------------")  # 60個


def outer(a, b):
    # a 和 b 將是inner()的環境變數
    def inner(x):
        return a * x + b

    return inner


f1 = outer(1, 2)
f2 = outer(3, 4)
print(f1(1), f2(3))

print("------------------------------------------------------------")  # 60個


def lazy_evaluation(expression):
    def evaluate():
        print(f"評估 : {expression}")
        return eval(expression)

    return evaluate


lazy_sum = lazy_evaluation("1 + 2 + 3 + 4")  # 這裡不會立即計算總和

result = lazy_sum()  # 這裡將計算並返回總和
print(result)

print("------------------------------------------------------------")  # 60個


def counter(start=0):
    count = [start]

    def increment():
        count[0] += 1
        return count[0]

    return increment


count_from_5 = counter(5)
print(count_from_5())  # 輸出: 6
print(count_from_5())  # 輸出: 7

print("------------------------------------------------------------")  # 60個


def event_handler(event):
    def register_handler(handler_function):
        print(f"Handling {event} with {handler_function.__name__}")
        handler_function(event)

    return register_handler


def on_click(event):
    print(f"Clicked: {event}")


def on_hover(event):
    print(f"Hovered: {event}")


# 創建事件處理器
click_handler = event_handler("Click Event")
hover_handler = event_handler("Hover Event")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)

print("------------------------------------------------------------")  # 60個



def printlocal():
    lang = "Java"
    print(f"語言 : {lang}")
    print(f"區域變數 : {locals()}")


msg = "Python"
printlocal()
print(f"語言 : {msg}")
print(f"全域變數 : {globals()}")

print("------------------------------------------------------------")  # 60個

from functools import reduce


def strToInt(s):
    def func(x, y):
        return 10 * x + y

    def charToNum(s):
        print("s = ", type(s), s)
        mydict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        n = mydict[s]
        print("n = ", type(n), n)
        return n

    return reduce(func, map(charToNum, s))


string = "5487"
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

things = {
    "iWatch手錶": (15000, 0.1),  # 定義商品
    "Asus  筆電": (35000, 0.7),
    "iPhone手機": (38000, 0.3),
    "Acer  筆電": (40000, 0.8),
    "Go Pro攝影": (12000, 0.1),
}

# 商品依價值排序
th = sorted(things.items(), key=lambda item: item[1][1])
print("所有商品依價值排序如下")
print("商品", "        商品價格 ", " 商品重量")
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")

print("------------------------------------------------------------")  # 60個

from functools import reduce


def strToInt(s):
    def func(x, y):
        return 10 * x + y

    def charToNum(s):
        print("s = ", type(s), s)
        n = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }[s]
        print("n = ", type(n), n)
        return n

    return reduce(func, map(charToNum, s))


string = "5487"
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

from functools import reduce


def strToInt(s):
    def func(x, y):
        return 10 * x + y

    def charToNum(s):
        return {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }[s]

    return reduce(func, map(charToNum, s))


string = "5487"
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

from functools import reduce


def strToInt(s):
    def charToNum(s):
        return {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }[s]

    return reduce(lambda x, y: 10 * x + y, map(charToNum, s))


string = "5487"
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

str_len = lambda x: len(x)
strs = ["abc", "ab", "abcde"]
strs.sort(key=str_len)
print(strs)

print("------------------------------------------------------------")  # 60個

strs = ["abc", "ab", "abcde"]
strs.sort(key=lambda x: len(x))
print(strs)

print("------------------------------------------------------------")  # 60個

sc = [["John", 80], ["Tom", 90], ["Kevin", 77]]
sc.sort(key=lambda x: x[1])
print(sc)

print("------------------------------------------------------------")  # 60個

sc = [["John", 80], ["Tom", 90], ["Kevin", 77]]
newsc = sorted(sc, key=lambda x: x[1])
print(newsc)

print("------------------------------------------------------------")  # 60個

sc = {"John": 80, "Tom": 90, "Kevin": 77}
newsc1 = sorted(sc.items(), key=lambda x: x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key=lambda x: x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)

print("------------------------------------------------------------")  # 60個


def fun(arg):
    pass


print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x: x))
print("列出內建函數abs的type類型: ", type(abs))

print("------------------------------------------------------------")  # 60個


def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step


print(type(myRange))
for x in myRange(0, 5):
    print(x)

print("------------------------------------------------------------")  # 60個

# 創建一個簡單的串列
my_list = [1, 3, 5]

# 建立串列的迭代器
my_iterator = iter(my_list)

# 使用 next() 函數遍歷迭代器並列印元素
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print("------------------------------------------------------------")  # 60個


def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x


myiter = iter_data()  # 建立迭代器
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("------------------------------------------------------------")  # 60個


def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x


myiter = iter_data()  # 建立迭代器
for data in myiter:
    print(data)

print("------------------------------------------------------------")  # 60個


def list_square(n):
    mylist = []
    for data in range(1, n + 1):
        mylist.append(data**2)
    return mylist


print(list_square(5))

print("------------------------------------------------------------")  # 60個


def iter_square(n):
    for data in range(1, n + 1):
        yield data**2


myiter = iter_square(5)  # 建立迭代器
for data in myiter:
    print(data)

print("------------------------------------------------------------")  # 60個

list_square = [n**2 for n in range(1, 6)]
print(list_square)

print("------------------------------------------------------------")  # 60個

list_square = (n**2 for n in range(1, 6))
for data in list_square:
    print(data)

print("------------------------------------------------------------")  # 60個


def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step


print(type(myRange))
for x in myRange(0, 5):
    print(x)

print("------------------------------------------------------------")  # 60個


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# 呼叫生成器函數，建立迭代器
fib = fibonacci(10)

# for 迴圈遍歷迭代器，輸出前 10 個 Fib 數
for num in fib:
    print(num, end="  ")

print("------------------------------------------------------------")  # 60個


def upper(func):  # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print("函數名稱 : ", func.__name__)
        print("函數參數 : ", args)
        return newresult

    return newFunc


def greeting(string):  # 問候函數
    return string


mygreeting = upper(greeting)  # 手動裝飾器
print(mygreeting("Hello! iPhone"))

print("------------------------------------------------------------")  # 60個


def upper(func):  # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print("函數名稱 : ", func.__name__)
        print("函數參數 : ", args)
        return newresult

    return newFunc


@upper  # 設定裝飾器
def greeting(string):  # 問候函數
    return string


print(greeting("Hello! iPhone"))

print("------------------------------------------------------------")  # 60個


def errcheck(func):  # 裝飾器
    def newFunc(*args):
        if args[1] != 0:
            result = func(*args)
        else:
            result = "除數不可為0"
        print("函數名稱 : ", func.__name__)
        print("函數參數 : ", args)
        print("執行結果 : ", result)
        return result

    return newFunc


@errcheck  # 設定裝飾器
def mydiv(x, y):  # 函數
    return x / y


print(mydiv(6, 2))
print(mydiv(6, 0))

print("------------------------------------------------------------")  # 60個


def upper(func):  # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult

    return newFunc


def bold(func):  # 加粗體字串裝飾器
    def wrapper(args):
        return "bold" + func(args) + "bold"

    return wrapper


@bold  # 設定加粗體字串裝飾器
@upper  # 設定大寫裝飾器
def greeting(string):  # 問候函數
    return string


print(greeting("Hello! iPhone"))

print("------------------------------------------------------------")  # 60個


def upper(func):  # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult

    return newFunc


def bold(func):
    def wrapper(args):
        return "bold" + func(args) + "bold"

    return wrapper


@upper  # 設定大寫裝飾器
@bold  # 設定加粗體字串大寫裝飾器
def greeting(string):  # 問候函數
    return string


print(greeting("Hello! iPhone"))

print("------------------------------------------------------------")  # 60個


def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")


print("------------------------------------------------------------")  # 60個


def modifySong(songStr):  # 將歌曲的標點符號用空字元取代
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, "")
    return songStr  # 傳回取代結果


def wordCount(songCount):
    global mydict
    songList = songCount.split()  # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd: songList.count(wd) for wd in set(songList)}


data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}  # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)  # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)  # 列印字典

print("------------------------------------------------------------")  # 60個


def create_multiplier(multiplier):
    def multiplier_function(number):
        return number * multiplier

    return multiplier_function


# 建立一個將數字乘以2的函數
double_function = create_multiplier(2)

# 使用返回的函數
result = double_function(5)  # 返回值是 10
print(result)  # 輸出: 10

# 建立一個將數字乘以3的函數
triple_function = create_multiplier(3)

# 使用返回的函數
result = triple_function(5)  # 返回值是 15
print(result)  # 輸出: 15

print("------------------------------------------------------------")  # 60個


def event_handler(event):
    def register_handler(handler_function):
        print(f"處理(Handling) {event} with {handler_function.__name__}")
        handler_function(event)

    return register_handler


def on_click(event):  # 按一下
    print(f"按一下 : {event}")


def on_hover(event):  # 懸停留
    print(f"懸停留 : {event}")


# 創建事件處理器
click_handler = event_handler("按一下事件")
hover_handler = event_handler("懸停留事件")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)

print("------------------------------------------------------------")  # 60個


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # 獲取函數開始執行的時間
        result = func(*args, **kwargs)  # 調用原始函數
        end_time = time.perf_counter()  # 獲取函數結束執行的時間
        duration = end_time - start_time  # 計算函數執行時間
        print(f"{func.__name__} 執行需 : {duration:.7f} 秒")
        return result

    return wrapper


@timing_decorator
def slow_function(duration):
    time.sleep(duration)  # 使函數暫停指定的秒數


# 調用裝飾器函數
slow_function(3)  # 輸出 slow_function 執行需 : 3.000xxxx 秒

print("------------------------------------------------------------")  # 60個


def interest(interest_type, subject):
    """顯示興趣和主題"""
    print("我的興趣是 " + interest_type)
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print()


interest("旅遊", "敦煌")
interest("程式設計", "Python")

print("------------------------------------------------------------")  # 60個


def interest(interest_type, subject):
    """顯示興趣和主題"""
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type} 中, 最喜歡的是 {subject}")
    print()


interest(interest_type="旅遊", subject="敦煌")  # 位置正確
interest(subject="敦煌", interest_type="旅遊")  # 位置更動

print("------------------------------------------------------------")  # 60個


def interest(interest_type, subject="敦煌"):
    """顯示興趣和主題"""
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type}  中, 最喜歡的是 {subject}")
    print()


interest("旅遊")  # 傳遞一個參數
interest(interest_type="旅遊")  # 傳遞一個參數
interest("旅遊", "張家界")  # 傳遞二個參數
interest(interest_type="旅遊", subject="張家界")  # 傳遞二個參數
interest(subject="張家界", interest_type="旅遊")  # 傳遞二個參數
interest("閱讀", "旅遊類")  # 傳遞二個參數,不同的主題

print("------------------------------------------------------------")  # 60個


def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")


ret_value = greeting("Nelson")
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def getMax(x, y):
    """文件字串實例
    建議x, y是整數
    這個函數將傳回較大值"""
    if int(x) > int(y):
        return x
    else:
        return y


print(getMax(2, 3))  # 列印較大值
print(getMax.__doc__)  # 列印文件字串docstring

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except Exception:
        print(f"Exception找不到 {fn} 檔案")
    else:
        wordList = data.split()  # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")  # 文章字數


files = ["data1.txt", "data2.txt", "data3.txt"]  # 檔案串列
for file in files:
    wordsNum(file)

print("------------------------------------------------------------")  # 60個


def division(x, y):
    try:  # try - except指令
        return x / y
    except ZeroDivisionError:  # 除數為0使用
        print("除數為0發生")
    except TypeError:  # 資料型別錯誤
        print("使用字元做除法運算異常")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


def division(x, y):
    try:  # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError):  # 2個異常
        print("除數為0發生 或 使用字元做除法運算異常")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


def division(x, y):
    try:  # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError) as e:  # 2個異常
        print(e)


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


def division(x, y):
    try:  # try - except指令
        return x / y
    except:  # 捕捉所有異常
        print("異常發生")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    pwdlen = len(pwd)  # 密碼長度
    if pwdlen < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if pwdlen > 8:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")


for pwd in ("aaabbbccc", "aaa", "aaabbb"):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import traceback  # 導入taceback


def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    pwdlen = len(pwd)  # 密碼長度
    if pwdlen < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if pwdlen > 8:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")


for pwd in ("aaabbbccc", "aaa", "aaabbb"):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open("tmp_errch15_16.txt", "a")  # 開啟錯誤檔案
        errlog.write(traceback.format_exc())  # 寫入錯誤檔案
        errlog.close()  # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_16.txt完成")
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import traceback


def division(x, y):
    try:  # try - except指令
        return x / y
    except:  # 捕捉所有異常
        errlog = open("tmp_errch15_17.txt", "a")  # 開啟錯誤檔案
        errlog.write(traceback.format_exc())  # 寫入錯誤檔案
        errlog.close()  # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_17.txt完成")
        print("異常發生")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個

try:
    # 嘗試打開一個不存在的檔案
    with open("non_existent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    # 如果文件不存在, 捕獲異常
    print("The file was not found")
except IOError:
    # 處理 I/O 錯誤, 例如:讀取錯誤
    print("An I/O error occurred")

print("------------------------------------------------------------")  # 60個

import requests

try:
    # 嘗試發出網絡請求
    response = requests.get("http://example.com")
    # 如果請求返回了錯誤響應, 會引發 HTTPError
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    # 處理 HTTP 錯誤
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    # 處理連接錯誤
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    # 處理請求超時錯誤
    print(f"Timeout Error: {e}")

print("------------------------------------------------------------")  # 60個

fn = "data15_4.txt"  # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    print(data)  # 輸出變數data


print("------------------------------------------------------------")  # 60個

fn = "data15_5.txt"  # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)  # 輸出變數data

print("------------------------------------------------------------")  # 60個

fn = "data15_6.txt"  # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    wordList = data.split()  # 將文章轉成串列
    print(f"{fn} 文章的字數是 {len(wordList)}")  # 列印文章字數

print("------------------------------------------------------------")  # 60個


def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
    else:
        wordList = data.split()  # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")  # 文章字數


file = "data15_6.txt"  # 設定欲開啟的檔案
wordsNum(file)

print("------------------------------------------------------------")  # 60個


def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
    else:
        wordList = data.split()  # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")  # 文章字數


files = ["data1.txt", "data2.txt", "data3.txt"]  # 檔案串列
for file in files:
    wordsNum(file)

print("------------------------------------------------------------")  # 60個


def division(x, y):
    try:  # try - except指令
        return x / y
    except Exception:  # 通用錯誤使用
        print("通用錯誤發生")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:  # 如果長度不是12
        return False  # 傳回非手機號碼格式

    for i in range(0, 4):  # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格式

    if string[4] != "-":  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(5, 8):  # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格

    if string[8] != "-":  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(9, 12):  # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格
    return True  # 通過以上測試


print("I love Ming-Chi: 是台灣手機號碼", taiwanPhoneNum("I love Ming-Chi"))
print("0932-999-199:    是台灣手機號碼", taiwanPhoneNum("0932-999-199"))


print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個

""" error
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息
"""
print("------------------------------------------------------------")  # 60個

import string


def encrypt(text, encryDict):  # 加密文件
    cipher = []
    for i in text:  # 執行每個字元加密
        v = encryDict[i]  # 加密
        cipher.append(v)  # 加密結果
    return "".join(cipher)  # 將串列轉成字串


abc = string.printable[:-5]  # 取消不可列印字元
subText = abc[-3:] + abc[:-3]  # 加密字串
encry_dict = dict(zip(subText, abc))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

msg = "If the implementation is easy to explain, it may be a good idea."
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個


def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()  # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))  # 列印文章字數


"""
files = []
for i in range(5):
    filename = input("請輸入檔案名稱 : ")
    files.append(filename)
    
for file in files:
    wordsNum(file)
"""

print("------------------------------------------------------------")  # 60個


def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()  # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))  # 列印文章字數
        return len(wordList)


def lenWord(filename):
    """檢查檔案長度必須是10到35個字元"""
    wdlen = wordsNum(filename)  # 檔案長度
    if wdlen < 10:  # 檔案長度不足
        raise Exception("檔案長度不足")
    if wdlen > 35:  # 檔案長度太長
        raise Exception("檔案長度太長")
    print("檔案長度正確")


for file in (
    "data/d1.txt",
    "data/d2.txt",
    "data/d3.txt",
    "data/d4.txt",
    "data/d5.txt",
):  # 測試系列檔案
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import re

msg = """txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         hung@gmail.com
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         service@deepwidsom.com
         mymail@yahoo.com
         de1988@kkk
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )"""
eMail = re.findall(pattern, msg, re.VERBOSE)  # 傳回搜尋結果
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個

import bs4
import requests

"""
url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件

dataTag = objSoup.select('.contents_box02')         # 尋找class是contents_box02
        
# 找尋開出順序與大小順序的球
balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("開出順序 : ", end='')
for i in range(6):                                  # 前6球是開出順序
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                       # 第7球以後是大小順序
    print(balls[i].text, end='   ')

# 找出第二區的紅球                   
redball = dataTag[2].find_all('div', {'class':'ball_red'})
print("\n特別號   :", redball[0].text)

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://www.wikipedia.org/'
browser.get(url)                    # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id('searchInput')
txtBox.send_keys('Artificial Intelligence')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單

print("------------------------------------------------------------")  # 60個

from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC308f91e9dc748a01538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f62118e4d33ca8ac'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 填上老師的號碼
            body = "感謝老師,我們學會了Python" )   # 發送的訊息

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ['cshung@deepwisdom.com.tw', 'jiinkwei@me.com']   # 設定收件人

with open('ex26_2.txt', 'rb') as filename:         # 讀取檔案內容
    mailContent = filename.read()
msg = MIMEText(mailContent, 'base64', 'utf-8')
msg['Content-Type'] = 'application/octet-stream'
msg['Content-Disposition'] = 'attachment; filename="ex26_2.txt"'
msg['Subject'] = '傳送Python學習心得附加檔案'
msg['From'] = '學生'
msg['To'] = 'cshung@deepwisdom.com.tw'
msg['Cc'] = 'jiinkwei@me.com'

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個
"""


print("------------------------------------------------------------")  # 60個

code1 = "洪"
print("洪")
print(hex(ord(code1)))  # 輸出字元'洪'的Unicode(16進位)碼值
code2 = "錦"
print("錦")
print(hex(ord(code2)))  # 輸出字元'錦'的Unicode(16進位)碼值
code3 = "魁"
print("魁")
print(hex(ord(code3)))  # 輸出字元'魁'的Unicode(16進位)碼值


print("------------------------------------------------------------")  # 60個

print(" 姓名    國文    英文    總分    平均")
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰儒", 98, 90, 188, 188 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪雨星", 96, 95, 191, 191 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰雨", 92, 88, 180, 180 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪星宇", 93, 97, 190, 190 / 2))

print("------------------------------------------------------------")  # 60個

wd = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print("下列是Python之禪內文")
print(wd)
print("以分行符號將Python 之禪的行資料變成串列元素")
songlist = wd.split("\n")
print(songlist)

print("------------------------------------------------------------")  # 60個

abc = "abcdefghijklmnopqrstuvwxyz"
front5 = abc[:5]
end21 = abc[5:]
subText = end21 + front5
print("abc     = ", abc)
print("subText = ", subText)

print("------------------------------------------------------------")  # 60個

cities = ["Taipei", "Beijing", "Tokyo", "Chicago", "Nanjing"]
print(cities)
cities.append("London")
print(cities)
cities.insert(3, "Xian")
print(cities)
cities.remove("Tokyo")
print(cities)

print("------------------------------------------------------------")  # 60個

sc = [
    ["洪錦魁", 80, 95, 88, 0, 0],
    ["洪冰儒", 98, 97, 96, 0, 0],
    ["洪雨星", 91, 93, 95, 0, 0],
    ["洪冰雨", 92, 94, 90, 0, 0],
    ["洪星宇", 92, 97, 90, 0, 0],
]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[2][4] = sum(sc[2][1:4])
sc[3][4] = sum(sc[3][1:4])
sc[4][4] = sum(sc[4][1:4])
sc[0][5] = round((sc[0][4] / 3), 1)
sc[1][5] = round((sc[1][4] / 3), 1)
sc[2][5] = round((sc[2][4] / 3), 1)
sc[3][5] = round((sc[3][4] / 3), 1)
sc[4][5] = round((sc[4][4] / 3), 1)
print(sc[0])
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])

print("------------------------------------------------------------")  # 60個

# 網址
site = "https://www.grenade.tw/blog/how-to-use-the-python-financial-analysis-visualization-module-mplfinance/"
if site.startswith("http://") or site.startswith("https://"):
    print("網址格式正確")
else:
    print("網址格式錯誤")

print("------------------------------------------------------------")  # 60個

n = 10
for i in range(1, n):
    for j in range(1, n - i + 1):
        print(j, end="")
    print()

print("------------------------------------------------------------")  # 60個

title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1, 10):
    print(f"{i:4d}", end="")
print()  # 跳列輸出
for i in range(40):
    print("=", end="")  # 列印分隔符號
print()  # 跳列輸出
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        print(f"{i*j:4d}", end="")  # 列印乘法值
    print()  # 跳列輸出

print("------------------------------------------------------------")  # 60個

names = ["洪錦魁", "洪冰儒", "東霞", "大成"]
lastname = []
for name in names:
    if name.startswith("洪"):  # 是否姓氏洪開頭
        lastname.append(name)  # 加入串列
print(lastname)

print("------------------------------------------------------------")  # 60個

sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 90, 0, 0, 0],
]
# 計算總分與平均
print("原始成績單")
for i in range(len(sc)):
    print(sc[i])
    sc[i][5] = sum(sc[i][2:5])  # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)  # 填入平均
sc.sort(key=lambda x: x[5], reverse=True)  # 依據總分高往低排序
# 以下填入名次
for i in range(len(sc)):  # 填入名次
    sc[i][7] = i + 1
# 以下修正相同成績應該有相同名次
for i in range((len(sc) - 1)):
    if sc[i][5] == sc[i + 1][5]:  # 如果成績相同
        sc[i + 1][7] = sc[i][7]  # 名次應該相同
# 以下依座號排序
sc.sort(key=lambda x: x[0])  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

weight = 50
increase = 1.2
n = 5
for i in range(int(n)):
    weight += increase
    print(f"第 {i+1} 年體重 : {weight:4.1f}")

print("------------------------------------------------------------")  # 60個

fahrenheit = [32, 77, 104]
celsius = [(x - 32) * 5 / 9 for x in fahrenheit]
print(celsius)

print("------------------------------------------------------------")  # 60個

n1 = [1, 2, 3, 4, 5]
n2 = [1, 2, 3, 4, 5]
result = [[x, y] for x in n1 for y in n2]
print(result)

print("------------------------------------------------------------")  # 60個

bookclub = ["John", "Peter", "Curry", "Mike", "Kevin"]
print("讀書會成員")
for people in bookclub:
    print(people)
bookclub[0] = "Johnnason"
for people in bookclub:
    print(people)

print("------------------------------------------------------------")  # 60個

tp = (1, 2, 3, 4, 5, 2, 3, 1, 4)
lst = list(tp)
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
newtp = tuple(newlst)
print("新的元組內容 : ", newtp)

print("------------------------------------------------------------")  # 60個

weatherH = (30, 28, 29, 31, 33, 35, 32)
weatherL = (20, 21, 19, 22, 23, 24, 20)
print(f"過去一周的最高溫度 {max(weatherH)}")
print(f"過去一周的最低溫度 {min(weatherH)}")

print("過去一周的平均溫度")
for i in range(len(weatherH)):
    print(f"{((weatherH[i]+weatherL[i])/2):3.1f}  ", end="")

print("------------------------------------------------------------")  # 60個

abc = "abcdefghijklmnopqrstuvwxyz"
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(subText, abc))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

msgTest = "python"  # 測試字串
cipher = []
for i in msgTest:  # 執行每個字元加密
    v = encry_dict[i]  # 加密
    cipher.append(v)  # 加密結果
ciphertext = "".join(cipher)  # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

season = {"Spring": "春季", "Summer": "夏季", "Fall": "秋季", "Winter": "冬季"}

wd = "Spring"
if wd in season:
    print(wd, " 中文字義是 : ", season[wd])
else:
    print("查無此單字")

print("------------------------------------------------------------")  # 60個

month = {
    "一月": "January",
    "二月": "February",
    "三月": "March",
    "四月": "April",
    "五月": "May",
    "六月": "June",
    "七月": "July",
    "八月": "August",
    "九月": "September",
    "十月": "October",
    "十一月": "November",
    "十二月": "December",
}

key = "三月"
if key in month:
    print(month[key])
else:
    print("輸入錯誤")

print("------------------------------------------------------------")  # 60個

noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(noodles)
for noodle, price in sorted(noodles.items(), key=lambda item: item[1]):
    print(noodle, ":", price)

print("------------------------------------------------------------")  # 60個

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
# 更改編號47到49的小兵
for soldier in armys[47:50]:
    if soldier["tag"] == "red":
        soldier["tag"] = "green"
        soldier["score"] = 10
        soldier["speed"] = "fast"
# 列印編號47到49的小兵
print("列印編號47到49小兵資料")
for soldier in armys[47:50]:
    print(soldier)

print("------------------------------------------------------------")  # 60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()  # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch, "")

# 將歌曲字串轉成串列
songList = songLower.split()

# 將歌曲串列處理成字典
dict = {wd: songList.count(wd) for wd in songList}

maxCount = max(dict.values())  # 出現最多次數
for key, count in dict.items():
    if count == maxCount:
        print(f"字串 {key} 出現最多次共出現 {count} 次")

print("------------------------------------------------------------")  # 60個

A = []
for i in range(1, 100, 2):
    A.append(i)

num = 2
B = []
primeNum = 0
while num < 100:
    if num == 2:  # 2是質數所以直接輸出
        B.append(num)
        primeNum += 1
    else:
        for n in range(2, num):  # 用2 .. num-1當除數測試
            if num % n == 0:  # 如果整除則不是質數
                break  # 離開迴圈
        else:  # 否則是質數
            primeNum += 1
            B.append(num)
    num += 1

aSet = set(A)  # 將串列A轉成集合aSet
bSet = set(B)  # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)
AsdB = aSet ^ bSet
print("AB對稱差集 : ", AsdB)

print("------------------------------------------------------------")  # 60個


def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])


data = [5, 7, 9, 15, 21, 6]
print(f"mysum = {mysum(data)}")

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

evenlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列: ", evenlist)

print("------------------------------------------------------------")  # 60個


def upper(func):  # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult

    return newFunc


def bold(func):  # 加粗體字串裝飾器
    def wrapper(args):
        return "bold" + func(args) + "bold"

    return wrapper


def italic(func):  # 加斜體字串裝飾器
    def wrapper(args):
        return "italic" + func(args) + "italic"

    return wrapper


@italic
@bold  # 設定加粗體字串裝飾器
@upper  # 設定大寫裝飾器
def greeting(string):  # 問候函數
    return string


print(greeting("Hello! iPhone"))

print("------------------------------------------------------------")  # 60個


def factorial(n):
    """計算n的階乘, n 必須是正整數"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 輸入城市的個數
N = 10
times = 10000000000000  # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24  # 一天秒數
year_secs = 365 * day_secs  # 一年秒數
combinations = factorial(N)  # 組合方式
years = combinations / (times * year_secs)
print(f"城市個數 {N}, 路徑組合數 = {combinations}")
print(f"需要 {years} 年才可以獲得結果")

print("------------------------------------------------------------")  # 60個

def pi(n):
    p = 0
    for i in range(1, n + 1, 1):
        p += 4 * ((-1) ** (i + 1) / (2 * i - 1))
    return p


print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))

print("------------------------------------------------------------")  # 60個


class Myschool:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def msg(self):
        print("Hi!" + self.name.title() + "你的成績是" + str(self.score) + "分")


A = Myschool("kevin", 80)
A.msg()

print("------------------------------------------------------------")  # 60個


class Animals:
    """Animals類別, 這是基底類別"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name  # 紀錄動物名稱
        self.age = animal_age  # 紀錄動物年齡

    def run(self):  # 輸出動物 is running
        print(self.name.title(), " is running")


class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別"""

    def __init__(self, dog_name, dog_age):
        super().__init__("My pet " + dog_name.title(), dog_age)


class Birds(Animals):
    """Birds類別, 這是Animal的衍生類別"""

    def __init__(self, bird_name, bird_age):
        super().__init__("My pet " + bird_name.title(), bird_age)

    def run(self):
        print(self.name.title(), "is flying")


mycat = Animals("lucy", 5)  # 建立Animals物件以及測試
print(mycat.name.title(), " is ", mycat.age, " years old.")
mycat.run()

mydog = Dogs("lily", 6)  # 建立Dogs物件以及測試
print(mydog.name.title(), " is ", mydog.age, " years old.")
mydog.run()

mybird = Birds("Cici", 8)  # 建立Birds物件以及測試
print(mybird.name.title(), " is ", mybird.age, " years old.")
mybird.run()

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Aunt(Grandfather):
    """定義阿姨類別"""

    def action2(self):  # 定義action2()
        print("Aunt")


class Ivan(Father, Uncle, Aunt):
    """定義Ivan類別"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Aunt(Grandfather):
    """定義阿姨類別"""

    def action2(self):  # 定義action2()
        print("Aunt")


class Ivan(Father, Uncle, Aunt):
    """定義Ivan類別"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Aunt(Grandfather):
    """定義阿姨類別"""

    def action2(self):  # 定義action2()
        print("Aunt")


class Ivan(Uncle, Aunt, Father):
    """定義Ivan類別"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Aunt(Grandfather):
    """定義阿姨類別"""

    def action2(self):  # 定義action2()
        print("Aunt")


class Ivan(Aunt, Father, Uncle):
    """定義Ivan類別"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

""" 很多
secretcode = '112299'                                   # 設定密碼
codeNotFound = True                                     # 尚未找到密碼為True
for i1 in range(0, 10):                                 # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(0, 10):                         # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(0, 10):                 # 第三位數
                    if codeNotFound:
                        for i4 in range(0, 10):
                            if codeNotFound:
                                for i5 in range(0, 10):
                                    if codeNotFound:
                                        for i6 in range(0, 10):
                                            code = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6) # 組成密碼
                                            if code == secretcode:              # 比對密碼
                                                print('Bingo!', code)
                                                codeNotFound = False            # 註明已經比對成功
                                                break
                                            else:
                                                print(code)                     # 列印無效碼
"""
print("------------------------------------------------------------")  # 60個


"""
def inn():
    a = input('輸入文字並轉換為 ASCII：')
    print('{} 的 ASCII：{}'.format(a, ord(a)))
    inn()

inn()
"""

print("------------------------------------------------------------")  # 60個

# 九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}x{}={} ".format(i, j, i * j), end="")
    print("")

print("------------------------------------------------------------")  # 60個

"""
while(True):
    a = input('請輸入簡單的數學式：')
    answer = '你輸入的不是數字呦～'
    if('+' in a):
        p = a.split('+')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) + int(p[1])
    elif('-' in a):
        p = a.split('-')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) - int(p[1])
    elif('/' in a):
        p = a.split('/')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) / int(p[1])
    elif('*' in a):
        p = a.split('*')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) * int(p[1])
    print(answer)
"""

print("------------------------------------------------------------")  # 60個

# a = input('請輸入倒數的秒數：')
a = "3"

if a.isdigit():
    a = int(a)
    while a > 0:
        print(a)
        a = a - 1
        time.sleep(1)
    print("時間到！")
else:
    print("你輸入的不是數字呦～")

print("------------------------------------------------------------")  # 60個

# 參考：http://violin-tao.blogspot.com/2017/05/python3_26.html

import multiprocessing as p

loc = p.Lock()  # 定義 Lock


def a1():
    global loc
    loc.acquire()  # 鎖住 Lock
    a = 0
    while a <= 20:
        a = a + 1
        print("a" + str(a))
        time.sleep(0.01)
        if a == 10:
            loc.release()  # 釋放 Lock


def a2():
    global loc
    a = 0
    while a <= 20:
        a = a + 1
        print("b" + str(a))
        time.sleep(0.01)
        if a == 5:
            loc.acquire()  # 鎖住 Lock


p1 = p.Process(target=a1)
p2 = p.Process(target=a2)
p1.start()
p2.start()

print("------------------------------------------------------------")  # 60個

import asyncio

c = True


async def a():
    global c
    a = 0
    while c == True:
        a = a + 1
        print(f"a{a}")
        await asyncio.sleep(0.1)


async def b():
    global c
    a = 0
    while a <= 5:
        a = a + 1
        print(f"b{a}")
        await asyncio.sleep(0.1)
    c = False
    return a


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(a()),
    asyncio.ensure_future(b()),
]
c = loop.run_until_complete(asyncio.gather(*tasks))
print(f"end:{c[1]}")

print("------------------------------------------------------------")  # 60個


class human:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = "???"

    def talk(self, msg):
        print(f"{self.name}: {msg}")


class Taiwan(human):
    def __init__(self, name, age=None):
        super().__init__(name)  # 繼承 human 的 name
        if age:
            self.age = age
        else:
            self.age = "???"


a = human("oxxo")
b = human("tom")
c = human()  # 沒有輸入就採用預設值
print(a.name)  # oxxo
print(b.name)  # tom

a.talk("hello")  # oxxo: hello
b.talk("ya")  # tom: ya
c.talk("okok!!!!!")  # ???: okok!!!!!

c = Taiwan("qq", 18)
print(c.name, c.age)  # qq 18

print("------------------------------------------------------------")  # 60個

import requests
import json

print("讀取網頁的json資料")

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式
#print(j)#全部
print("第0筆")
print(j[0])
print("第1筆")
print(j[1])

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
jj = json.dumps(j[0], ensure_ascii=False)
print(jj)

with open("tmp_json_data1.txt", "a+") as f:
    f.write(jj)

print("------------------------------------------------------------")  # 60個

import csv
import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
# 此處不使用，因為發現出來變成純文字格式，非 json
jj = json.dumps(j[0], ensure_ascii=False)

with open("tmp_json_data2.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for i in j:
        writer.writerow([i["tag"], i["title"], i["site"], i["date"]])
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
    print("寫入完成！")

print("------------------------------------------------------------")  # 60個

# 參考 https://zh.wikipedia.org/wiki/%E9%80%97%E5%8F%B7%E5%88%86%E9%9A%94%E5%80%BC
import csv
from collections import OrderedDict

with open("data/a16.csv") as csvFile:
    # r = csv.reader(csvFile)      # 無法和 DictReader 同時使用，不知道為什麼
    # for i in r:
    #   print(i)

    rows = csv.DictReader(csvFile)  # 轉成 OrderedDict
    o = []
    for row in rows:
        print(row)
        d = dict(OrderedDict(row))  # 轉成 Dict
        print(d)
        o.append(d)

    for i in o:
        print(f'姓名：{i["name"]}，年紀：{i["age"]} 歲。')

print("------------------------------------------------------------")  # 60個

""" fail
from lxml import html
import requests

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
page = requests.get(url)
tree = html.fromstring(page.text)

print('美金：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()')[0]))
print('日圓：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()')[0]))
"""

print("------------------------------------------------------------")  # 60個

from lxml import html
import requests
import json

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
page = requests.get(url)
j = json.loads(page.text)

print(j)


print("------------------------------------------------------------")  # 60個

import requests

rep = requests.get("https://www.oxxostudio.tw/img/articles/201803/css-animation-01.gif")

with open("tmp_test.gif", "wb") as f:
    f.write(rep.content)

print("------------------------------------------------------------")  # 60個

""" 跳過 webdriver

from selenium import webdriver
import requests

# pip3 install selenium
# 下載 chromedriver ( 注意要對應自己 chrome 版本 )
# https://chromedriver.chromium.org/downloads

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver')  # 設定 chromedriver 路徑
driver.get('http://oxxo.studio')  # 前往這個網址
print(driver.title)
time.sleep(1)
driver.execute_script(
    'window.scrollTo(0, document.body.scrollHeight);')  # 捲動到最下方
time.sleep(1)
for i in range(1, 7):
    img = driver.find_element_by_xpath(
        '//*[@id="content-grid"]/ul/li[' + str(i) + ']/a[1]/div/img')
    rep = requests.get(img.get_attribute('src'))
    with open('demo/test'+str(i)+'.jpg', 'wb') as f:
        f.write(rep.content)
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 不會開啟瀏覽器

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver', chrome_options=options)  # 設定 chromedriver 路徑
driver.get('https://www.dinbendon.net/do/login')  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input')
user.send_keys('XXX')

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input')
pwd.send_keys('XXX')

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]')
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input')

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r'\d+',checktext)[0])   # 使用正則表達式提取數字
b = int(re.findall(r'\d+',checktext)[1])
result = a+b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]')
btn.click()

time.sleep(1)

# 抓取第一筆便當名稱，加入例外處理
try:
    menu = driver.find_element_by_xpath(
        '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]')

    print(menu.text)
except:
    print('找不到便當名稱')

driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import requests

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver')  # 設定 chromedriver 路徑
driver.get('https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl')  # 前往這個網址

search = driver.find_element_by_xpath(
    '//*[@id="sbtc"]/div/div[2]/input')
search.send_keys('林志玲')


btn = driver.find_element_by_xpath(
    '//*[@id="sbtc"]/button')
btn.click()

for i in range(1, 6):

    time.sleep(0.5)
    div = driver.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div['+str(i)+']')
    div.click()

    time.sleep(0.5)
    img = driver.find_element_by_xpath(
        '//*[@id="irc-ss"]/div['+str(i)+']/div[1]/div[4]/div[1]/a/div/img')
    src = img.get_attribute('src')
    print(src)
    if(str(src) != 'None'):
      if('.jpg' in src):
          filename = src.split('/')[-1]
          rep = requests.get(src)
          with open('demo/'+str(filename), 'wb') as f:
              f.write(rep.content)
              closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
              closeBtn.click()
      else:
          closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
          closeBtn.click()
"""
print("------------------------------------------------------------")  # 60個

import re

# 取出一段文字中的阿拉伯數字
a = "123 + 456"
b = re.findall(r"\d+", a.replace(" ", ""))
print(b)

# 取出一段文字中的「非」阿拉伯數字
c = "hello 123 !!!"
d = re.findall(r"\D+", c.replace(" ", ""))
print(d)

# 取出每個非空白字元
msg1 = "hello world!!"
msg1r = re.findall(r"\S", msg1)
print(msg1r)


# 替換指定區間文字
msg2 = "hello {name}, {age}"
msg2r = re.findall(r"\{.+?\}", msg2)
print(msg2r)
text = {"name": "oxxo", "age": "18"}
for i in range(0, len(msg2r)):
    o = re.sub(r"\{|\}", "", msg2r[i])
    msg2 = re.sub(msg2r[i], text[o], msg2)

print(msg2)

aa = "abc"
aa = aa + "def"
print(aa)

print("------------------------------------------------------------")  # 60個

a = 4
b = 2.2

print("a=" + str(a))
print("a=%d" % a)
print("a=" + str(a) + " b=" + str(b))
print("a=%d b=%f" % (a, b))
print("a=%d b=%.1f" % (a, b))

print("------------------------------------------------------------")  # 60個

try:  # python 3.x
    name = "豬八戒"
    print(" 你好! " + name)
except:  # python 2.x
    name = raw_input("名字:").decode("utf-8")
    nameutf8 = unicode(name).encode("utf-8")
    print(" 你好! " + nameutf8)

print("------------------------------------------------------------")  # 60個

list1 = [1, 2, 3, 4]
list1 = [x * 2 for x in list1 if x % 2 == 0]
print(list1)

list1 = [1, 2, 3, 4]
list1 = [x for x in list1 if x >= 3]
print(list1)

list1 = [59, 60, 70, 80]
list1 = [x**2 for x in list1 if x < 60]
print(list1)

list1 = [20, 30, 50, 80]
list1 = [x for x in list1 if (x >= 30 and x <= 50)]
print(list1)  # 30,50

print("------------------------------------------------------------")  # 60個

# 可以拿來作統計常態分佈用

scores = [90, 59, 78, 71, 39, 0, 19, 85, 77, 84, 91, 98, 38, 66, 65, 88, 63, 85, 18, 0]
freq = [0] * 5
for score in scores:
    if score < 20:
        freq[0] += 1
    elif score < 40:
        freq[1] += 1
    elif score < 60:
        freq[2] += 1
    elif score < 80:
        freq[3] += 1
    else:
        freq[4] += 1
print("人數分佈頻率:", freq)


print("------------------------------------------------------------")  # 60個


def wait_for_user_interrupt():
    while True:
        time.sleep(1)
        print("無限迴圈, 按 Ctrl + C 離開")


try:
    wait_for_user_interrupt()
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

import bext

bext.fg("yellow")
bext.clear()

# Draw the quit message:
bext.goto(0, 0)
print("Ctrl-C to quit.", end="")

print("------------------------------------------------------------")  # 60個


SAND = chr(9617)
WALL = chr(9608)

print(WALL, end="")
print(" ", end="")  # Clear the old position.
print(SAND, end="")
print(" ", end="")  # Clear the old position.

print(WALL, end="")
print(" ", end="")  # Clear the old position.
print(SAND, end="")
print(" ", end="")  # Clear the old position.

print(WALL, end="")
print(" ", end="")  # Clear the old position.
print(SAND, end="")
print(" ", end="")  # Clear the old position.

print(WALL, end="")
print(" ", end="")  # Clear the old position.
print(SAND, end="")
print(" ", end="")  # Clear the old position.


print("enumerate的用法")
allSand = list("ABCD")

for i, sand in enumerate(allSand):
    print(i, sand)

print("------------------------------------------------------------")  # 60個

print("enumerate() 一個串列")

animals = ["鼠", "牛", "虎", "兔"]

print("用 for")
for _ in enumerate(animals):
    print(_)

print("用 list")
print(list(enumerate(animals)))

print("用 unpacking 取出內容")

for index, ani in enumerate(animals):
    print(index, ani)

print("------------------------------------------------------------")  # 60個

print("字元相關的兩個內建函式")

print("字元轉數值")
cc = ord("豬")
print(cc)

print("數值轉字元")
nn = 35948 + 5
cc = chr(nn)
print(cc)

print("------------------------------------------------------------")  # 60個

# lambda匿名函數

# List 含有 Tuple
student = [
    ("Eugene", 1989, "Taipei"),
    ("Davie", 1993, "Kaohsiung"),
    ("Michelle", 1999, "Yilan"),
    ("Peter", 1988, "Hsinchu"),
    ("Connie", 1997, "Pingtung"),
]

# 定義sort()方法參數key
na = lambda item: item[0]
student.sort(key=na)
print("依名字排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

# 直接在sort()方法帶入lamdba()函式
student.sort(key=lambda item: item[2], reverse=True)
print("依出生地遞減排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

print("------------------------------------------------------------")  # 60個

size = 25

for i in range(size):
    for j in range(size):
        if i % 2 == 1 or j % 2 == 1:
            print("■", end="")
        else:
            print("□", end="")
    print()


print("------------------------------------------------------------")  # 60個

list1 = [1, 2, 3, 4, 5, 6, 7]
# 找最小、最大元素
print(min(list1), max(list1))
# 串列長度、串列加總
print(len(list1), sum(list1))

s0 = slice(0, 2)  # 切片物件：定義切片範圍
s1 = slice(1, -1, 2)
print(list1[s0], list1[s1])  # list1直接帶入切片範圍
# 結果：([1, 2], [2, 4, 6])

print("------------------------------------------------------------")  # 60個

fset = frozenset(["a", "b", "c"])
print(fset)  # frozenset({'a', 'b', 'c'})

# fset.remove('a')      # 不能修改，AttributeError
# frozenset根本沒有remove()可用！

print("------------------------------------------------------------")  # 60個

print("用zip組合資料成字典")
keys = ("cname", "ename", "weight")
values = ("鼠", "mouse", 3)
dic1 = dict(zip(keys, values))
print(dic1)


print("------------------------------------------------------------")  # 60個

names = ["Amy", "Bob", "Cathy"]
scores = [70, 92, 85]
list1 = list(enumerate(zip(names, scores)))
# [(0, ('Amy', 70)), (1, ('Bob', 92)), (2, ('Cathy', 85))]
for item in list1:
    print(item[0], item[1][0], item[1][1])

print(list(zip(("a", "b", "c"), (30, 41, 52))))
# [('a', 30), ('b', 41), ('c', 52)]

print(list(enumerate(["a", "b", "c"])))
# [(0, 'a'), (1, 'b'), (2, 'c')]

print("------------------------------------------------------------")  # 60個

print("從list中過濾資料")
list1 = [30, 45, 1024, 2500, 699, 126]

# 過濾出小於1000元的消費
list2 = [num for num in list1 if num < 1000]

sum1 = sum(list1)  # 用sum做消費加總
avg1 = sum1 / len(list1)  # 用len取消費筆數
sum2 = sum(list2)  # 用sum做消費加總
avg2 = sum2 / len(list2)  # 用len取消費筆數

print(sum1)
print(avg1)
print(sum2)
print(avg2)

print("------------------------------------------------------------")  # 60個

n = 10  # 設定進度條總長
for i in range(n + 1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end="")  # 輸出不換行的內容
    time.sleep(0.05)


print("------------------------------------------------------------")  # 60個

print("字串的處理")

print("分割字串")
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

ss = filename.split("/")
print(filename)
print(len(ss))
for _ in ss:
    print(_)

print("------------------------------------------------------------")  # 60個

print("測試不定引數的函式")


# 定義函式
def funtionTest(*number):
    print("你傳入了", len(number), "個引數")
    outcome = 1
    for item in number:
        outcome *= item
    return outcome


# 呼叫函式
print("呼叫函式並傳入 1 個引數 :", funtionTest(7))
print("呼叫函式並傳入 2 個引數 :", funtionTest(12, 3))
print("呼叫函式並傳入 4 個引數 :", funtionTest(3, 5, 9, 14))

print("------------------------------------------------------------")  # 60個

print("print語法")

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

"""
驗證輸入用戶名和QQ號是否有效并給出對應的提示信息

要求：
用戶名必須由字母、數字或下劃線構成且長度在6~20個字符之間
QQ號是5~12的數字且首位不能為0
"""

import re

# username = input('請輸入用戶名: ')
username = "lion_mouse"
m1 = re.match(r"^[0-9a-zA-Z_]{6,20}$", username)
if not m1:
    print("請輸入有效的用戶名.")

# qq = input('請輸入QQ號: ')
qq = "12345678"
m2 = re.match(r"^[1-9]\d{4,11}$", qq)
if not m2:
    print("請輸入有效的QQ號.")
if m1 and m2:
    print("你輸入的信息是有效的!")


print("------------------------------------------------------------")  # 60個

import string

# 北美獨立宣言
text = (
    "Resolved: That these United Colonies are, and of right ought to be, "
    + "free and independent States, that they are absolved from all allegiance "
    + "to the British Crown, and that all political connection between them and "
    + "the State of Great Britain is, and ought to be, totally dissolved."
)
# 先一律轉小寫
str2 = text.lower()

charSet = set(string.ascii_lowercase)
freqDict = {}
for ch in str2:
    # 判斷如果不在ASCII小寫字母集，則略過
    if not ch in charSet:
        continue
    freqDict[ch] = freqDict.get(ch, 0) + 1

print(freqDict)

print("------------------------------------------------------------")  # 60個

print("字串的處理")

# 北美獨立宣言
text = (
    "Resolved: That these United Colonies are, and of right ought to be, "
    + "free and independent States, that they are absolved from all allegiance "
    + "to the British Crown, and that all political connection between them and "
    + "the State of Great Britain is, and ought to be, totally dissolved."
)

print(text)

print("依以下符號split字串")

seplist = [":", ",", "."]
for i in range(len(seplist) - 1):
    text = text.replace(seplist[i], seplist[-1])

slist = text.split(seplist[-1])
print(slist)

with open("tmp_resolution.txt", "wt") as outf:
    for s in slist:
        outf.write("-------------------------\n")
        outf.write(s.strip() + "\n")

print("------------------------------------------------------------")  # 60個

"""
import os

# 我們指定本機的/tmp暫存資料夾來試試
path = '/tmp/'
stat = {}
for item in os.walk(path):
    # item[0]是路徑名稱，item[2]是檔案清單
    for fname in item[2]:
        # 取出檔名完整路徑
        ffname = os.path.join(item[0], fname)
        # 取出檔案大小
        size = os.path.getsize(ffname)
        # 取出檔案副檔名，統一轉小寫並去除開頭的'.'字元
        ext = os.path.splitext(ffname)[-1].lower().replace('.', '')
        # 如果副檔名是空的，跳過
        if ext.strip()=='':
            continue
        # 進行累計
        stat[ext] = stat.get(ext, 0)+size

for k, v in stat.items():
    print(k, v)
"""
print("------------------------------------------------------------")  # 60個

# 九九乘法表就應該是2..9而不是1..9哦！
set99 = set()
outf = open("tmp_99.txt", "wt")
for i in range(2, 9 + 1):
    for j in range(1, 9 + 1):
        prod = i * j
        # 判斷乘積數字是否出現過
        if prod not in set99:
            outf.write(str(prod) + " ")
            # 沒出現過，加入set99
            set99.add(prod)
    outf.write("\n")
outf.close()

print("------------------------------------------------------------")  # 60個

print("字串的處理")

text = "welcome to python"

print("endswith 是否以xxx為結尾")
cc = text.endswith("thon")
print(cc)

print("startswith 是否以xxx為開頭")
cc = text.startswith("hello")
print(cc)

print("count 計數出現的次數")
cc = text.count("o")
print(cc)

print("find 找到字串的位置")
cc = text.find("come")
print(cc)

print("find 找到字串的位置")
cc = text.find("become")
print(cc)

print("find 找到字串的位置")
cc = text.find("o")
print(cc)

print("find 找到字串的位置")
cc = text.find("e")
print(cc)

print("rfind 找到字串的位置")
cc = text.rfind("o")
print(cc)

print("rfind 找到字串的位置")
cc = text.rfind("e")
print(cc)

print("------------------------------------------------------------")  # 60個

text = "welcome to python"

print("text = " + text)

str2 = "Welcome to Python"
print("str2 = " + str2)

str3 = "This is a test."
print("str3 = " + str3)

print("轉成capitalize")
cc = text.capitalize()
print(cc)

print("轉成小寫")
cc = str2.lower()
print(cc)

print("轉成大寫")
cc = text.upper()
print(cc)

print("轉成title")
cc = text.title()
print(cc)

print("轉成swapcase")
cc = str2.swapcase()
print(cc)

print("replace")
cc = str3.replace("is", "was")
print(cc)

print("------------------------------------------------------------")  # 60個

text = "This is a book."
print("split")
cc = text.split()
print(cc)

str2 = "Tom,Bob,Mary,Joe"
print("split ,")
cc = str2.split(",")
print(cc)

str3 = "23\n12\n45\n56"
print("splitlines")
cc = str3.splitlines()
print(cc)

str4 = "23\n12\n45\n56"
print("split xx")
cc = str4.split("\n")
print(cc)

print("------------------------------------------------------------")  # 60個

text = "-"
list1 = ["This", "is", "a", "book."]
print(text.join(list1))

print("------------------------------------------------------------")  # 60個

print("使用 round 四捨五入到小數點三位")
cc = 1234.56789
print("原數字 :", cc)
cc = round(cc, 3)
print("處理後 :", cc)

print("------------------------------------------------------------")  # 60個

b1 = 1
b2 = 3
print(f"{b1} / {b2} = {round(b1/b2,3)}")  # 使用 round 四捨五入到小數點三位
print(f"{b2} / {b1} = {round(b2/b1,3)}")

print("------------------------------------------------------------")  # 60個

v4 = int("11", 16)  # 17, base 16
print(v4)
v8 = float("2.7E-2")  # 0.027
print(v8)

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print('請輸入一串列的整數，數目之間利用空白分隔：')
ps = "86 75 92 77 84 76 95"

pitems = ps.split()
pscores = [ eval(x) for x in pitems ]
pabove = 0
paverage = sum(pscores)/len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數："+str(paverage))
print("大於或等於平均數的數目："+str(pabove))
print("小於平均數的數目："+str(len(pscores)-pabove))

print("------------------------------------------------------------")  # 60個

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f"%("陳大同",89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("楊小明",77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f"%("陳時雨",66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f"%("李婉玲",76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("林研時",89.25, 99.50, 89.25))

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f"%("陳大同",89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("楊小明",77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f"%("陳時雨",66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f"%("李婉玲",76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("林研時",89.25, 99.50, 89.25))

print("------------------------------------------------------------")  # 60個

list1 = [50,40,20,40,20,60,20,80,90]
print(" 原始串列:",list1)
list1.sort()
list1.reverse()
print(" 由大到小:",list1)

print("------------------------------------------------------------")  # 60個

print("%4s %4s %8s"%("x","y","x**y"))
print("%4d %4d %8d"%(1,1,1))
print("%4d %4d %8d"%(2,2,4))
print("%4d %4d %8d"%(4,3,64))
print("%4d %4d %8d"%(8,4,4096))

print("------------------------------------------------------------")  # 60個

i=1
while (i<=9):
    j=2
    while (j<=9):        
        print("%d*%d=%2d"%(j,i,i*j), end=" ")
        j=j+1
    print()
    i=i+1

print("------------------------------------------------------------")  # 60個

def calarea(height, width=6):
    result = height*width
    return result
getarea = calarea(10)
print(getarea)

print("------------------------------------------------------------")  # 60個

def calarea(height, width=6):
    result = height*width
    return result
getarea = calarea(10, 7)
print(getarea)

print("------------------------------------------------------------")  # 60個

def scope():
    var1 = 1
    print(var1, var2)
var1 = 3
var2 = 4
print(var1, var2)
scope()
print(var1, var2) 

print("------------------------------------------------------------")  # 60個

def scope():
    global var1
    var1 = 1
    print(var1, var2)
var1 = 3
var2 = 4
print(var1, var2)
scope()
print(var1, var2)  

print("------------------------------------------------------------")  # 60個

import calendar
print(calendar.month(2018,2))

print("------------------------------------------------------------")  # 60個

# 模組與套件

import calendar
print(calendar.__file__)

print("------------------------------------------------------------")  # 60個

print('要轉換的十進位數字 = 255')
pnum = 255
presult=""
while(pnum!=0):
    pdata=str(pnum%2)
    presult="".join([pdata,presult])
    pnum=pnum//2
print("轉換為二進位數字為:%s"%presult)

print("------------------------------------------------------------")  # 60個

try:   
    print(varn)
except NameError:
    print("變數不存在!")
finally:
    print("程式執行結束例外處理區塊")

print("------------------------------------------------------------")  # 60個

""" fail
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=52B8s2zrdeE")
stream = yt.streams.filter(file_extension='mp4', res='360p').first()
stream.download("c:\\dddddddddd")
"""

print("------------------------------------------------------------")  # 60個


def phi(n):
    presult = 0
    ptemp = 1
    for i in range(1, n + 1, 1):
        presult = presult+ptemp/(2 * i - 1) 
        ptemp = -1*ptemp
    presult = 4*presult
    return presult

print(phi(900))

print("------------------------------------------------------------")  # 60個

from random import randint
import os.path

#pfile = input("請輸入檔名：").strip()

pfile = 'tmp_cccccc.txt'
if os.path.isfile(pfile):
    print("此檔案已經存在，程式終止")
else:
    poutfile = open(pfile, "w")
        
    for i in range(30):
        print(randint(0, 999), file = poutfile, end = " ")
       
    poutfile.close()
        
    pinfile = open(pfile, "r")
    ps = pinfile.read()
    
    pnumber = [eval(items) for items in ps.split()]
    pnumber.sort()
        
    for i in range(len(pnumber)):
        print(pnumber[i], end = " ")
            
    pinfile.close()

print("------------------------------------------------------------")  # 60個

try:
    #pnumber = int(input("請輸入一個整數："))
    pnumber = 'aaaa'
    print("所輸入的整數%d"%pnumber)
except Exception as ex:
    print("異常例外：", ex) 

print("------------------------------------------------------------")  # 60個


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

