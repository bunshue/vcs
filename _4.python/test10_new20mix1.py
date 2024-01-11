"""
範例來的混合資料 1


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

x = -10
print("以下輸出abs( )函數的應用")
print(x)  # 輸出x變數
print(abs(x))  # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print(pow(x, y))  # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 48.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 49.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.25
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.151
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.251
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)

print("------------------------------------------------------------")  # 60個

dist = 384400  # 地球到月亮距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days, hours = divmod(total_hours, 24)  # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)

print("------------------------------------------------------------")  # 60個


score = 90
name = "洪錦魁"
count = 1
print("%s你的第 %d 次物理考試成績是 %d" % (name, count, score))

score = 90
name = "洪錦魁"
count = 1
print("{}你的第 {} 次物理考試成績是 {}".format(name, count, score))

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

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)

print("------------------------------------------------------------")  # 60個

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print("------------------------------------------------------------")  # 60個

cars = ["Honda", "Toyota", "Ford", "BMW"]
print("目前串列內容 = ", cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop()  # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ", cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)  # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ", cars)

print("------------------------------------------------------------")  # 60個

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))

print("------------------------------------------------------------")  # 60個

cars = ["toyota", "nissan", "honda"]
search_str = "nissan"
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))

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

aaa = 123

print("%-10d 保留10位向左靠齊")
print("|%-10d|" % aaa)

print("%10d  保留10位向右靠齊")
print("|%10d|" % aaa)


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

# 陣列: list 與 tuple
arr = ["one", "two", "three"]
print(arr[0])

arr[1] = "hello"
print(arr)

del arr[1]

print(arr)

arr.append(23)
print(arr)

arr = ("one", "two", "three")
print(arr[0])
print(arr)

# arr[1] = 'hello'

print("------------------------------------------------------------")  # 60個

# 最基本簡單的堆疊

s = []
s.append("吃飯")
s.append("睡覺")
s.append("寫程式")

print(s)
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())

print("------------------------------------------------------------")  # 60個

# 麻煩的優先佇列

q = []
q.append((2, "寫程式"))
q.append((1, "吃飯"))
q.append((3, "睡覺"))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)

print("------------------------------------------------------------")  # 60個

# 用切片清除或複製 list 元素

lst = [0, 1, 2, 3, 4]
del lst[:]

print(lst)

lst = [1, 2, 3]
new_lst = lst

print(new_lst)
print(new_lst is lst)

lst[:] = [7, 8, 9]

print(lst)
print(new_lst)
print(new_lst is lst)

copied_lst = lst[:]

print(copied_lst)
print(copied_lst is lst)

lst = [0, 1, 2, 3, 4]
s = slice(1, 4)
print(lst[s])

print("------------------------------------------------------------")  # 60個

squares = [value**2 for value in range(1, 11)]
print(squares)

print("------------------------------------------------------------")  # 60個

cal_dict = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}


def calculator(x, operator, y):
    return cal_dict.get(operator, lambda: None)(x, y)


print(calculator(6, "乘", 7))

calculator = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}

default = lambda: None

print(calculator.get("加", default)(1, 2))

print(calculator.get("乘", default)(3, 5))

print("------------------------------------------------------------")  # 60個

# 使用 json.dumps() 美觀列印 dict

import json

config = {
    "lang": "Python",
    "version": [3.6, 3.7, 3.8],
    "date": "2019-10-14",
    "platform": "linux",
    "org": "Python Software Foundation",
    "config_status": 0xC0FFEE,
    "the_answer": 42,
}

print(json.dumps(config, indent=4, sort_keys=False))

print("------------------------------------------------------------")  # 60個

# 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print("")

print([_ for _ in dir(datetime) if "date" in _.lower()])

# help(datetime)

print("------------------------------------------------------------")  # 60個

print("有f代入數字")

money = 12345
print(f"正確 你得到獎金 ${money} 元")
print("錯誤 你得到獎金 ${money} 元")

print("------------------------------------------------------------")  # 60個

"""
print('11')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())#讀一行

print('22')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    data = f.read() #讀全部成一行串列

print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print('33')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())#讀全部成多行串列
"""

print("------------------------------------------------------------")  # 60個

print("用字典建立個人資料")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)

print("------------------------------------------------------------")  # 60個


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

print("------------------------------------------------------------")  # 60個


def printmsg():
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)  # 列印全域變數


msg = "Global Variable"  # 設定全域變數
print("主程式列印: ", msg)  # 列印全域變數
printmsg()  # 呼叫函數

print("------------------------------------------------------------")  # 60個


def printmsg():
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = "Local Variable"  # 設定區域變數
    print("函數列印: ", msg)  # 列印區域變數


msg = "Global Variable"  # 這是全域變數
print("主程式列印: ", msg)  # 列印全域變數
printmsg()  # 呼叫函數

print("------------------------------------------------------------")  # 60個


def printmsg():
    global msg
    msg = "Java"  # 更改全域變數
    print("更改後: ", msg)


msg = "Python"
print("更改前: ", msg)
printmsg()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_17.py

# ch11_17.py
# 定義lambda函數
square = lambda x: x**2

# 輸出平方值
print(square(10))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_18.py


# ch11_18.py
# 使用一般函數
def square(x):
    value = x**2
    return value


# 輸出平方值
print(square(10))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import locale

print(locale.getpreferredencoding())


print("------------------------------------------------------------")  # 60個
"""
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行
with open(fn, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()               # 每次讀一行
"""

print("------------------------------------------------------------")  # 60個

import time  # 導入模組time

print(time.asctime())  # 列出目前系統時間

print("------------------------------------------------------------")  # 60個

import time  # 導入模組time

xtime = time.localtime()
print(xtime)  # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_16.py

# ch13_16.py
import calendar

print("2020年是否潤年", calendar.isleap(2020))
print("2021年是否潤年", calendar.isleap(2021))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_17.py

# ch13_17.py
import calendar

print(calendar.month(2020, 1))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_18.py

# ch13_18.py
import calendar

print(calendar.calendar(2020))

print("------------------------------------------------------------")  # 60個


# ch12_2.py
class Banks:
    # 定義銀行類別
    title = "Taipei Bank"  # 定義屬性

    def motto(self):  # 定義方法
        return "以客為尊"


userbank = Banks()  # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


str1 = 'Python is funny and powerful'
print('原字串', str1)
print('欄寬40，字串置中', str1.center(40))
print('字串置中，* 填補', str1.center(40, '*'))
print('欄寬10，字串靠左', str1.ljust(40, '='))
print('欄寬40，字串靠右', str1.rjust(40, '#'))

mobilephone = '931666888'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Mayor,President'
print('以逗點分割字元', str2.partition(','))

str3 = '禮\n義\n廉\n恥'
print('依\\n分割字串', str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

str1="Happy birthday to my best friend."
s1=str1.count("to",0) #從str1字串索引0的位置開始搜尋
s2=str1.count("e",0,34) #搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1,s1,s2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\ExCarry.py

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" %(z, z))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" %(1.2345))
print("不足數位預設空格：%6.2f\n" %(1.2345))
print("小數點保留2位：%.2f\n" %(1.2345))
print("不足數位補0(以*替代)：%0*.2f\n" %(6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" %(66))
print("不足數位預設空格：%5d\n" %(66))
print("小於位數則輸出全部：%2d\n" %(666))
print("不足數位補0(以*替代)：%0*d\n" %(5, 66))

print("------------------------------------------------------------")  # 60個

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
   print("索引位置：%s\t對應值：%s\t型態：%s\n" %(i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

person = ["John", "Merry", "Mi", "Jason"]
addPerson = "David"

if person.count(addPerson) == 0:
   person.insert(len(person) - 2, addPerson)

print("搜尋剛新增人員索引位置：", person.index(addPerson))

person1 = person.copy()
person.clear()

print("複製原串列：", person1)
print("原串列：", person)

print("------------------------------------------------------------")  # 60個

likeBasketball = set(("class A", "class B", "class C"))
likeDodgeball = set(("class A", "class F", "class k"))

setDifference = likeBasketball.difference(likeDodgeball)
print("\nlikeBasketball差集：", setDifference)
setDifference = likeDodgeball.difference(likeBasketball)
print("likeDodgeball差集：", setDifference)

setIntersection = likeBasketball.intersection(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的交集：", setIntersection)

setUnion = likeBasketball.union(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的聯集：", setUnion)

setSymmetric_difference = likeBasketball.symmetric_difference(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的對稱差：", setSymmetric_difference)

print("------------------------------------------------------------")  # 60個

Index = "Hello Python, This is Program"

print("Index字串：", Index)
print(Index[-3:-25:-2])

print("------------------------------------------------------------")  # 60個

strName = "台北永和三支"
strCode = "3388128"
intAount = 123456
intMoney = 456789
	
print("\n郵局：%s" %(strName))
print("郵局代號為%s，轉帳戶頭為%02d" %(strCode, intAount))
print("匯入金額：%c%.2f" %(36, intMoney))
	
if intMoney < 20000:
    print("%c\n" %("成"))

print("------------------------------------------------------------")  # 60個

print("="*30, "\n")

print("------------------------------------------------------------")  # 60個

number={1,2,3,4,5,6,7,8,9,10,11,12}
print(number)
lotto1={3,5,7,10,12} #第一組幸運彩蛋
print("第一組樂透:",lotto1)
lotto2={2,5,6,11,12} #第二組幸運彩蛋
print("第二組樂透:",lotto2)
lucky=lotto1 | lotto2
print("有 %d 個數字出現在其中一次開獎" %len(lucky), lucky)
biglucky=lotto1 & lotto2
print("有 %d 個數字出現在每一次開獎" %len(biglucky), biglucky)
badnum=number -lucky
print("總共有 %d 個不幸運的數字" %len(badnum), badnum)

print("------------------------------------------------------------")  # 60個

phrase = 'Happy holiday.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

s= "我畢業於宜蘭高中."
print(s)
s1=s.replace("宜蘭高中", "高雄中學")
print(s1)

print("------------------------------------------------------------")  # 60個

fruit = ['apple', 'orange', 'watermelon']
print('反轉前內容：', fruit)
fruit.reverse() 
print('反轉後內容：', fruit)
score = [65,76,54,32,18]
print('反轉前內容：', score)
score.reverse() 
print('反轉後內容：', score)

print("------------------------------------------------------------")  # 60個

score = [98, 46, 37, 66, 69]
print('排序前順序：',score)
score.sort() #省略reverse參數, 遞增排序
print('遞增排序：', score)
letter = ['one', 'time', 'happy', 'child']
print('排序前順序：')
print(letter)
letter.sort(reverse = True) #依字母做遞減排序
print('遞減排序：')
print(letter)

print("------------------------------------------------------------")  # 60個

str1 = "happy \nclever \nwisdom"
print( str1.split() ) #以空格與換行符號(\n)來分割
print( str1.split(' ', 2 ) ) 

print("------------------------------------------------------------")  # 60個

wd = 'Alex is optimistic and clever.'
print('字串:', wd)
print('Alex為開頭的字串嗎', wd.startswith('Alex')) 
print('clever為開頭的字串嗎', wd.startswith('clever', 0))
print('optimistic從指定位置的開頭的字串嗎', wd.startswith('optimisti', 8)) 
print('clever.為結尾字串嗎', wd.endswith('clever.'))  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\tuple_sorted.py

pay = (8000, 7200, 8300, 4700, 5500)
print(pay)
print('由小而大：',sorted(pay))
print('由大而小：', sorted(pay, reverse = True))

print('資料仍維持原順序：')
print(pay)

print("------------------------------------------------------------")  # 60個

word1 = "zoo"
word2 = "animal"
print("交換前: ")
print('單字1={},單字2={}'.format(word1,word2))

word2,word1 = word1,word2
print("交換後: ")
print('單字1={},單字2={}'.format(word1,word2))

print("------------------------------------------------------------")  # 60個

product = (('iPhone','手機','我預算的首選'),
        ('iPad','平板','視股票獲利'),
        ('iPod','播放','價格最親民'))

for(name, c_name,memo) in product:
    print('%-10s %-12s %-10s'%(name,c_name,memo))

print("------------------------------------------------------------")  # 60個

def func(a,b,c):
    x = a +b +c
    return x

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

def func(a,b,c):
    x = a +b +c
    print(x)

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

def equation(x,y,z):
    ans = x*y+z*x+y*z
    return ans

print(equation(z=1,y=2,x=3))
print(equation(3, 2, 1))
print(equation(x=3, y=2 , z=1))
print(equation(3, y=2 , z=1))

print("------------------------------------------------------------")  # 60個

total=lambda a,b:a+b
num1=0
num2=0
num1=123
num2=456
print('數值 1+數值 2 =',total(num1,num2))

print("------------------------------------------------------------")  # 60個

score=[97,76,89,76,90,100,87,65]
print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))

print("------------------------------------------------------------")  # 60個

def square_sum(*arg):
    ans=0
    for n in arg:
        ans += n*n
    return ans

ans1=square_sum(1)
print('1*1=',ans1)
ans2=square_sum(1,2)
print('1*1+2*2=',ans2)
ans3=square_sum(1,2,3)
print('1*1+2*2+3*3=',ans3)
ans4=square_sum(1,3,5,7)
print('1*1+3*3+5*5+7*7=',ans4)

def progname(**arg):
    return arg

print(progname(d1='python', d2='java', d3='visual basic'))

print("------------------------------------------------------------")  # 60個

def dinner(mainmeal, *sideorder):
    #列出所點餐點的主餐及點心副餐
    print('所點的主餐為',mainmeal,'所點的副餐點心包括:')
    for snack in sideorder:
        print(snack)

dinner('鐵板豬','烤玉米')
dinner('泰式火鍋','德式香腸','香焦牛奶','幸運餅')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\pow.py

def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
print('請輸入兩數x及y的值函數：')
x=3
y=8
print('次方運算結果：%d' %Pow(x, y))

print("------------------------------------------------------------")  # 60個

import random

val=0
data=[0]*80
for i in range(80):
    data[i]=random.randint(1,150)

print('資料內容：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]  ' %(i*8+j+1,data[i*8+j]),end='')
    print('')

print("------------------------------------------------------------")  # 60個

def swap_test(x,y):
    print('函數內交換前：x=%d, y=%d' %(x,y))
    x,y=y,x #交換過程
    print('函數內交換前：x=%d, y=%d' %(x,y))     

a=10
b=20 #設定a,b的初值
print('函數外交換前：a=%d, b=%d' %(a,b))
swap_test(a,b) #函數呼叫
print('函數外交換後：a=%d, b=%d' %(a,b))

print("------------------------------------------------------------")  # 60個

print('int(9.6)=',int(9.6))
print('bin(20)=',bin(20))
print('hex(66)=',hex(66))
print('oct(135)=',oct(135))
print('float(70)=',float(70))
print('abs(-3.9)=',abs(-3.9))
print('chr(69)=',chr(69))
print('ord(\'%s\')=%d' %('D',ord('D')))
print('str(543)=',str(543))

print("------------------------------------------------------------")  # 60個

import calendar

y = 2023
m = 12
ys = 5 # int(input("列印n年內為閏年的月曆:"))
notLeap = []

calendar.setfirstweekday(calendar.SUNDAY)

for i in range(ys):
    if calendar.isleap(y+i) == True:
        print("\n")
        calendar.prmonth(y+i, m)
    else:
        notLeap.append(y+i)

print("\n以下非閏年:", notLeap)
print("{}到{}期間有幾個閏年:{}".format(y, y+ys, calendar.leapdays(y, y+ys)))

print("------------------------------------------------------------")  # 60個

"""
import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))
"""

print("------------------------------------------------------------")  # 60個

import random

name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))
print("抽取三個元素：", random.sample(name, 3))
print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

import random

print("任一整數", random.randrange(100))
print("任一整數", random.randrange(52, 100))
print("奇數", random.randrange(1, 100, 2))
print("偶數", random.randrange(0, 100, 2))

print("------------------------------------------------------------")  # 60個

import time

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

import sys
if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])

print("------------------------------------------------------------")  # 60個

import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
word = ['apple','bird','tiger','happy','quick']
random.shuffle(word)  #使用shuffle函數打亂字的順序
print(word)#將打亂後字依序輸出

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("保留區")


