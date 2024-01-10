import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個


def show():
    person1 = {"name": "Amy", "phone": "049-1234567", "age": 20}
    person2 = {"name": "Jack", "phone": "02-4455666", "age": 25}
    person3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
    persons = [person1, person2, person3]
    print(type(person1))
    print(type(person2))
    print(type(person3))
    print(type(persons))
    print(person1)
    print(person2)
    print(person3)
    print(persons)


show()

print("------------------------------------------------------------")  # 60個

POSTGRES = {
    "user": "admin",
    "password": "123456",
    "db": "NTUHQA",
    "host": "localhost",
    "port": "5432",
}

string = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s" % POSTGRES

print(string)

print("------------------------------------------------------------")  # 60個

animals = ["cat", "dog", "bat"]
for index, animal in enumerate(animals):
    print(index, animal)

animals = ["cat", "dog", "bat"]
for animal in animals:
    print(animal)

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal, legs in d.items():
    print("動物: %s 有 %d 隻腳" % (animal, legs))

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal in d:
    legs = d[animal]
    print(animal, legs)


d = {"cat": "white", "dog": "black"}  # 建立字典
print(d["cat"])  # 使用Key取得項目: 顯示 "white"
print("cat" in d)  # 是否有Key: 顯示 "True"
d["pig"] = "pink"  # 新增項目
print(d["pig"])  # 顯示 "pink"
print(d.get("monkey", "N/A"))  # 取出項目+預設值: 顯示 "N/A"
print(d.get("pig", "N/A"))  # 取出項目+預設值: 顯示 "pink"
del d["pig"]  # 使用Key刪除項目
print(d.get("pig", "N/A"))  # "pig"不存在: 顯示 "N/A"


from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)


print("------------------------------------------------------------")  # 60個


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

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
print(x3)  # 輸出字元x3的Unicode碼值
x4 = "魁"
print(ord(x4))  # 輸出字元'魁'的Unicode碼值

print("------------------------------------------------------------")  # 60個

x = 0x5D  # 這是16進為整數
print(x)  # 列出10進位的結果
y = 93  # 這是10進為整數
print(hex(y))  # 列出轉換成16進位的結果

print("------------------------------------------------------------")  # 60個

x = 0b1101  # 這是2進為整數
print(x)  # 列出10進位的結果
y = 13  # 這是10進為整數
print(bin(y))  # 列出轉換成2進位的結果

print("------------------------------------------------------------")  # 60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

james = [23, 19, 22, 31, 18]  # 定義james串列
print("列印james第1-3場得分", james[0:3])
print("列印james第2-4場得分", james[1:4])
print("列印james第1,3,5場得分", james[0:6:2])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day09\clock.py

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

'''
if __name__ == '__main__':
    main()
'''

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个矩形'


if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('周长:', shape.perimeter())
        print('面积:', shape.area())

print("------------------------------------------------------------")  # 60個




import numpy as np

a = np.random.randint(0, 5, 10)
print(a)
print(np.unique(a))  # unique統計陣列中所有不同的值

print(np.bincount(a))  # bincount統計整數陣列中每個元素出現的次數


print("------------------------------------------------------------")  # 60個

import datetime

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

now = datetime.datetime.now()
date = now.date
month = now.month
year = now.year

m, y = (month, year) if month >= 3 else (month + 12, year - 1)
c, y = y // 100, y % 100
w = (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10) % 7
month_words = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
print(f'{month_words[month - 1]} {year}'.center(20))
print('Su Mo Tu We Th Fr Sa')
print(' ' * 3 * w, end='')
days = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
][is_leap(year)][month - 1]   
for day in range(1, days + 1):
    print(str(day).rjust(2), end=' ')
    w += 1
    if w == 7:
        print()
        w = 0
print()

print("------------------------------------------------------------")  # 60個

f = [x for x in range(1, 10)]

print(f)

print(sys.getsizeof(f))  # 查看對象佔用內存的字節數

print("------------------------------------------------------------")  # 60個

print("設計一個函數產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。\n")

import random


def generate_code(code_len=4):
    """
    生成指定長度的驗證碼

    :param code_len: 驗證碼的長度(默認4個字符)

    :return: 由大小寫英文字母和數字構成的隨機驗證碼
    """
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code(10))

print("------------------------------------------------------------")  # 60個

print("設計一個函數返回給定文件名的後綴名。\n")


def get_suffix(filename, has_dot=False):
    """
    獲取文件名的後綴名

    :param filename: 文件名
    :param has_dot: 返回的後綴名是否需要帶點
    :return: 文件的後綴名
    """
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print(get_suffix(filename))

print("------------------------------------------------------------")  # 60個

print("計算指定的年月日是這一年的第幾天\n")


def is_leap_year(year):
    """
    判斷指定的年份是不是閏年

    :param year: 年份
    :return: 閏年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    計算傳入的日期是這一年的第幾天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第幾天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))

print("------------------------------------------------------------")  # 60個

import numpy as np

print("二維陣列 6 X 4")
a = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(a[3, 1:4])

print("前2列 之 第2欄之後")
print(a[:2, 2:])

print("第2列 之 全部")
print(a[2, :])

print("全部列 之 第3欄, 轉成row")
print(a[:, 3])

print("全部列 之 偶數欄")
print(a[:, ::2])

print("偶數列 之 036欄")
print(a[::2, ::3])

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", a.sum())
print("直行加:", a.sum(axis=0))
print("橫列加:", a.sum(axis=1))

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", a.min(axis=0))
print("每個直行的最小值對應的索引:", a.argmin(axis=0))
print("每個直行的標準差:", a.std(axis=0))

print("全部平均:", a.mean())
print("直行平均:", a.mean(axis=0))
print("橫列平均:", a.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
a = np.arange(10)
print(a)

print("前4項")
print(a[:4])

print("第3項 至 第7項(不含尾)")
print(a[3:7])

print("第5項 至 最後")
print(a[5:])

print("第3至第9項 跳一個")
print(a[3:9:2])

print("第2項開始至最後, 跳一個")
print(a[2::2])

print("從頭至最後, 跳二個")
print(a[::3])

print("------------------------------------------------------------")  # 60個

print("np亂數建立一維陣列 1 ~ 7(不含尾), 300個")
a = np.random.randint(1, 7, 300)
print(a)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
a = np.random.randint(1, 7, (6, 4))
print(a)

for _ in range(10):
    a = np.random.uniform()
    print(a)


print("------------------------------------------------------------")  # 60個

x = np.random.normal(1,4,(3,5))
x = np.random.normal(1,4,(3,5))
y = np.argmax(x,axis=1)
print(x)
print(x.shape)
print(y)
print(y.shape)
                                                                                                                  
print('查詢函數用法')
help(np.max)

print("------------------------------------------------------------")  # 60個

print("使用 numpy函數 對 list做處理")

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))


print("------------------------------------------------------------")  # 60個

print("用numpy建立資料")
a = np.arange(5)
print(a)
a = np.arange(2,5,1)
print(a)
a = np.linspace(2,5,4)
print(a)
a = np.logspace(0,2,5)
print(a)

a = np.empty(5) # 生成5個元素，值爲隨機數的數組（速度快）
print(a)
a = np.zeros(5) # 生成5個值全爲0的數組
print(a)
a = np.ones(5) # 生成5個值全爲1的數組
print(a)
a = np.full(5, 6) # 生成5個值全爲6的數組
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6], dtype=np.int64)
print(a.dtype) 
a = a.astype(np.float32)
print(a.dtype) 
print(a.dtype.type)


print("------------------------------------------------------------")  # 60個

N = 10
y = np.random.randn(N)

print(y)


print("分段函數")

x=np.arange(10)
print(x)

print(np.where(x<5, x, 9-x))


a=np.arange(10)
print(np.select([x<3,x>6], [-1,1], 0))


a=np.arange(10)
print(np.piecewise(x, [x<3,x>6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------------------------------------")  # 60個

print("統計函數")
a=np.arange(10,0,-1)
print(a)
print(a.mean())
print(a.var())
print(a.std())
print(np.average(a, weights=np.arange(0,10,1)))
print(np.median(a))
print(np.percentile(a, 75))


print(a.min())
print(a.max())
print(a.ptp())
print(a.argmin())
print(a.argmax())
print(a.argsort())
a.sort()
print(a)

a=np.random.randint(0,5,10)
print(a) 
print(np.unique(a)) 
print(np.bincount(a)) 
print(np.histogram(a,bins=5))

print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(type(a))

a = np.mat(np.random.random((2,2)))
print(a)
print(np.eye(2))
print(np.diag([2,3]))

a = np.mat([[1.,2.],[3.,4.]])
print(np.dot(a,a))    # 矩陣乘積
print(np.multiply(a,a))    # 矩陣點乘
print(a.T)   # 矩陣轉置
print(a.I)   # 矩陣求逆
print(np.trace(a))    # 求矩陣的跡
print(np.linalg.eig(a))   # 特徵分解

a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print("------------------------------------------------------------")  # 60個

# id的用法

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)


print("------------------------------------------------------------")  # 60個

import random  # 導入模組random

fruits = ["蘋果", "香蕉", "西瓜", "水蜜桃", "百香果"]

count = []
for _ in range(10):
    cc = random.choice(fruits)
    print(cc)

print("------------------------------------------------------------")  # 60個

"""
双色球随机选号程序
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input("机选几注: "))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)


print("------------------------------------------------------------")  # 60個

# 函数的定义和使用 - 求最大公约数和最小公倍数

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(15, 27))
print(lcm(15, 27))

print("------------------------------------------------------------")  # 60個

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(strtime)
mydate = time.strptime("2018-1-1", "%Y-%m-%d")
print(mydate)

# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system("ls -l")
# os.chdir('/Users/Hao')
os.system("ls -l")
# os.mkdir('test')

print("------------------------------------------------------------")  # 60個

# 用range创建数值列表
list1 = list(range(1, 11))  # 不含尾
print(list1)

print("------------------------------------------------------------")  # 60個

c = 1 + 3j
print("c的資料型態：", type(c))
print("c是否為複數？", isinstance(1 + 3j, complex))

print("------------------------------------------------------------")  # 60個

sigma = 0
k = int(input("請輸入k值："))  # 輸入k值
for n in range(0, k, 1):
    if n & 1:  # 如果n是奇數
        sigma += float(-1 / (2 * n + 1))
    else:  # 如果n是偶數
        sigma += float(1 / (2 * n + 1))
print("PI = %f" % (sigma * 4))

print("------------------------------------------------------------")  # 60個

# 九九乘法表的雙重迴圈
for i in range(1, 10):
    for j in range(1, 10):
        print("{0}*{1}={2:2d}  ".format(i, j, i * j), sep="\t", end="")
        if j >= 7:
            break  # 設定跳出的條件
    print("\n-------------------------------------------------------\n")


print("------------------------------------------------------------")  # 60個
info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)


print("------------------------------------------------------------")  # 60個

word = [
    "holiday",
    "happy",
    "birth",
    "yesterday",
    "holiday",
    "car",
    "yellow",
    "happy",
    "mobile",
    "cup",
    "happy",
    "holiday",
    "holiday",
    "desk",
    "birth",
]
print("holiday 出現的次數", word.count("holiday"))


print("------------------------------------------------------------")  # 60個

str1 = "do your best what you can do"
s1 = str1.count("do", 0)
s2 = str1.count("o", 0, 20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1, s1, s2))


print("------------------------------------------------------------")  # 60個

str1 = "設定中文字型及負號正確顯示"
print("原字串內容: ", str1)
print("轉換成串列: ", list(str1))
print("轉換成值組: ", tuple(str1))
print("字串長度: ", len(str1))

list1 = list(str1)
print("原串列內容: ", list1)
print("串列中最大值: ", max(list1))
print("串列中最小值: ", min(list1))

relist = reversed(list1)  # 反轉串列
for i in relist:  # 將反轉後的串列內容依序印出
    print(i, end=" ")
print()  # 換行
print("串列元素由小到大排序: ", sorted(list1))


print("------------------------------------------------------------")  # 60個


result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8

print("------------------------------------------------------------")  # 60個


def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


formula = lambda x, y: 3 * x + 2 * y  # 表示lambda有二個參數
print(formula(5, 10))  ##傳入兩個數值讓lambda()函數做運算，輸出數值35


print("------------------------------------------------------------")  # 60個

str1 = "淡泊以明志，寧靜以致遠"
print("原字串", str1)
print("欄寬20，字串置中", str1.center(20))
print("字串置中，# 填補", str1.center(20, "#"))
print("欄寬20，字串靠左", str1.ljust(20, "@"))
print("欄寬20，字串靠右", str1.rjust(20, "!"))

mobilephone = "931828736"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Time create hero.,I love my family."
print("以逗點分割字元", str2.partition(","))

str3 = "忠孝\n仁愛\n信義\n和平"
print("依\\n分割字串", str3.splitlines(False))


print("------------------------------------------------------------")  # 60個
math.sqrt(sum(pow(x - (sum(data) / len(data)), 2) for x in data) / len(data))

mean = sum(data) / len(data)
variance = sum(pow(x - mean, 2) for x in data) / len(data)
std = math.sqrt(variance)


print("------------------------------------------------------------")  # 60個

print("a", "b", "c", sep="|")

print("a", "b", "c", end="\n\n")



print("------------------------------------------------------------")  # 60個




prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票價格大於100元的股票構造一個新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

print("------------------------------------------------------------")  # 60個


"""
迭代工具 - 排列 / 組合 / 笛卡爾積
"""
import itertools

itertools.permutations('ABCD')
itertools.combinations('ABCDE', 3)
itertools.product('ABCD', '123')


"""
找出序列中出現次數最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

