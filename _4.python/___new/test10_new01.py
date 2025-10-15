"""
準備清除


準備撈出

class bank  class Banks():

def

最前面 為 測試區

最後面 為 準備搬出區


pppp 打印 字串相關
llll 字典 集合 串列 元組 dslt

"""

import requests

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
print("------------------------------------------------------------")  # 60個

set1 = {"a", "b", "c", "d", "e", "f"}
set2 = set1.copy()
print(set1)
print(set2)

print("------------------------------------------------------------")  # 60個


print("---- 字串處理專區 --------------------------------------------------------")  # 60個

query_string = "abcdefghijklmn"
query_number = 12345678901234
replace_parameter = "無f替換變數"
replace_parameter += " WHERE {query_string}"
replace_parameter += " ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)

replace_parameter = "有f替換變數"
replace_parameter += f" WHERE {query_string}"
replace_parameter += f" ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)

table_columns = "(alpaca_name, training, duration, date)"
postgres_insert_query = (
    f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""
)

print(postgres_insert_query)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from urllib import parse

string = "豬頭三"

string_url = parse.quote(string)
print("原字串:\t" + string)
print("轉網址:\t" + string_url)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("if and or")
year = 2024
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "is a leap year?", isLeapYear)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("if and or")
number = 126

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print(number, "divisible by 2 or 3, but not both")

print("------------------------------------------------------------")  # 60個

print("測試 strip()")
input_string = "ABCDEFG       "
print("無strip <<<" + input_string + ">>>")
input_string = input_string.strip()
print("有strip <<<" + input_string + ">>>")

print("------------------------------------------------------------")  # 60個

string = "測試字串是不是有被包含"
ss = "要"
if ss in string:
    print("有被包含")
else:
    print("沒有被包含")

ss = "包含"
if ss in string:
    print("有被包含")
else:
    print("沒有被包含")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

MILLI_SECONDS = 1e3
MICRO_SECONDS = 1e6
PERCENT = 100
LINE = 79
MIN_TEST_RUNTIME = 1e-3

name = "david"
min_time = 11.11
avg_time = 22.22
op_avg = 33.33
min_overhead = 44.44
total_min_time = 55.55
total_avg_time = 66.66
other_min_time = 77.77
warp = 88.88
min_diff = 99.99
other_avg_time = 12.34
avg_diff = 23.45
overhead_times = 34.56
overhead_times = 45.67
eff_time = 56.78
abs_time = 67.89
min_overhead = 78.90

print(
    "%30s:  %5.0fms  %5.0fms  %6.2fus  %7.3fms"
    % (
        name,
        min_time * MILLI_SECONDS,
        avg_time * MILLI_SECONDS,
        op_avg * MICRO_SECONDS,
        min_overhead * MILLI_SECONDS,
    )
)
print("-" * LINE)
print(
    "Totals:                        "
    " %6.0fms %6.0fms"
    % (
        total_min_time * MILLI_SECONDS,
        total_avg_time * MILLI_SECONDS,
    )
)
print()

print(
    "%30s: %5.0fms %5.0fms %7s %5.0fms %5.0fms %7s"
    % (
        name,
        min_time * MILLI_SECONDS,
        other_min_time * MILLI_SECONDS * warp / warp,
        min_diff,
        avg_time * MILLI_SECONDS,
        other_avg_time * MILLI_SECONDS * warp / warp,
        avg_diff,
    )
)
"""
print('%30s:  %6.3fms  %6.3fms' % \
      (name,
       min(overhead_times) * MILLI_SECONDS,
       max(overhead_times) * MILLI_SECONDS))
"""
print(
    "    %5.0fms    %5.0fms %7.3fms"
    % (eff_time * MILLI_SECONDS, abs_time * MILLI_SECONDS, min_overhead * MILLI_SECONDS)
)

i = 123
print(" Round %-25i  effective   absolute  overhead" % (i + 1))

print("%30s:" % name, end=" ")

print("Calib. prep time     = %.6fms" % (total_min_time * MILLI_SECONDS))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import importlib
import platform
from types import ModuleType
from typing import Optional, Tuple, List, cast


def print_table(version_rows: List[Tuple[str, str]]) -> None:
    row_format = "{:12} | {}"
    print(row_format.format("module", "version"))
    print(row_format.format("------", "-------"))
    for module, version in version_rows:
        # Some version strings have multiple lines and need to be squashed
        print(row_format.format(module, version.replace("\n", " ")))


def extract_version(module: ModuleType) -> Optional[str]:
    if module.__name__ == "gdcm":
        return cast(Optional[str], getattr(module, "GDCM_VERSION", None))

    return cast(Optional[str], getattr(module, "__version__", None))


modules = (
    "os",
    "sys",
    "cv2",
    "numpy",
    "PIL",
    "pylibjpeg",
    "openjpeg",
    "libjpeg",
)
"""
for module in modules:
    try:
        m = importlib.import_module(module)
    except ImportError:
        version = "_module not found_"
    else:
        version = extract_version(m) or "**cannot determine version**"

    version_rows.append((module, version))

print('print_table')
print_table(version_rows)
"""

print("------------------------------------------------------------")  # 60個

ENDMARKER = 0
NAME = 1
NUMBER = 2
STRING = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
PERCENT = 24
LBRACE = 25
RBRACE = 26
EQEQUAL = 27
N_TOKENS = 54
NT_OFFSET = 256

tok_name = {
    value: name
    for name, value in globals().items()
    if isinstance(value, int) and not name.startswith("_")
}

print(type(tok_name))
print(tok_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)

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

x = [
    [a, b, c]
    for a in range(1, 20)
    for b in range(a, 20)
    for c in range(b, 20)
    if a**2 + b**2 == c**2
]
print(x)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("chr-ord-ascii ST")
print("------------------------------------------------------------")  # 60個

for x in range(0x2160, 0x216A):
    print(chr(x), end=" ")

print()

print("字元轉數值")
cc = ord("豬")
print(cc)

print("數值轉字元")
nn = 35948 + 5
cc = chr(nn)
print(cc)


# ord()回傳參數字元對應的的編碼位置
print("==Test1==")
print(ord("H"))
print(ord("你"))
print(ord("好"))
# chr()回傳參數編碼位置對應的字元
print("==Test2==")
print(chr(72))
print(chr(20320))
print(chr(22909))


##輸出'A'之後的10個英文字母
print("==Test3==")
for i in range(65, 75):
    print(chr(i), end="")
print()
##輸出'你'之後的10個中文字
for i in range(20320, 20330):
    print(chr(i), end="")
print()
# str()回傳參數為字串
print("==Test4==")
print(str(123) + "456")
# ascii()回傳參數的字串表達形式
##如果字串含有非ASCII字元，所有非ASCII字元會以Unicode跳脫字元的方式呈現
print(ascii("Ab123"))
print(ascii("hello你好".encode("utf-8")))


# ord()是將字元轉成ASCII碼
# chr()是將ASCII碼轉成字元
# ord()和chr()互為反函數
print(chr(ord("A")))
print(ord(chr(65)))


# i的初始值為A字元的ASCII碼(65)，終止值小於Z字元的ASCII碼(90)+1，遞增值為1
for i in range(ord("A"), ord("Z") + 1, 1):
    print(chr(i), end="")


x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出字元x3的Unicode(10進位)碼值
x4 = "魁"
print(hex(ord(x4)))  # 輸出字元'魁'的Unicode(16進位)碼值

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出字元x3的Unicode碼值
x4 = "魁"
print(ord(x4))  # 輸出字元'魁'的Unicode碼值

print("------------------------------------------------------------")  # 60個
print("chr-ord-ascii SP")
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
print("------------------------------------------------------------")  # 60個

print("十進位 轉 十六進位")


# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    return hex


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord("0"))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord("A"))


decimalValue = 170
hexValue = decimalToHex(decimalValue)
print("decimal : %d\thex : %s" % (decimalValue, hexValue))

decimalValue = 65535
hexValue = decimalToHex(decimalValue)
print("decimal : %d\thex : %s" % (decimalValue, hexValue))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 檢查有無包含中文
def is_contains_chinese():
    print("is_contains_chinese")
    global search_word
    for _char in search_word:
        if "\u4e00" <= _char <= "\u9fa5":
            print("True")
            return True
    print("False")
    return False


search_word = "oat"
is_contains_chinese()
search_word = "英國"
is_contains_chinese()

print("------------------------------------------------------------")  # 60個

for y in "12345":
    for x in "JQKA":
        print(x, y, end=" ")

print("------------------------------------------------------------")  # 60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)

print("------------------------------------------------------------")  # 60個

print(2**32)

print("------------------------------------------------------------")  # 60個

"""
word = word.strip()

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))

"""

print("------------------------------------------------------------")  # 60個


def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        if "A" <= ch <= "F" or "0" <= ch <= "9":
            decimalValue = decimalValue * 16 + hexCharToDecimal(ch)
        else:
            return None

    return decimalValue


def hexCharToDecimal(ch):
    if "A" <= ch <= "F":
        return 10 + ord(ch) - ord("A")
    else:
        return ord(ch) - ord("0")


hex = "aa"
decimal = hexToDecimal(hex.upper())

if decimal == None:
    print("Incorrect hex number")
else:
    print("The decimal value for hex number", hex, "is", decimal)

print("------------------------------------------------------------")  # 60個

number = 123456
NUMBER_OF_DIGITS = 10
print(number)
numberList = list(str(number).zfill(NUMBER_OF_DIGITS))
print(numberList)
numberList = list(str(number))
print(numberList)

print("------------------------------------------------------------")  # 60個

print("y = x ^ 2")
x = [x for x in range(21)]
y = [(y * y) for y in x]

print(x)
print(y)

print("------------------------------------------------------------")  # 60個

name = "aaaamock"
message = "%s(%%s)" % name

print(message)

print("------------------------------------------------------------")  # 60個

# 位元運算子綜合應用
x = 12
y = 8
print(x & y)
print(x ^ y)
print(x | y)
print(~x)

print("------------------------------------------------------------")  # 60個

info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)

print("------------------------------------------------------------")  # 60個

loc = ([1, 2, 3, 4], [11, 12, 13, 14])
print(type(loc))
print(loc)
print(loc[::-1])

print("------------------------------------------------------------")  # 60個


"""n2w: 數字轉英文模組, 包含一個num2words函式, 也能獨立執行
獨立執行用法: n2w num
              num: 0~999,999,999,999,999 之間的整數 (可用逗號分隔)
範例: n2w 10,003,103
輸入 10,003,103 後會輸出 ten million three thousand one hundred three
"""

import string
import argparse

# 數字與英文的對應字典
_1to9dict = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
_10to19dict = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen",
}
_20to90dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

# 數字位數與數字英文單位的對應串列(list)
_magnitude_list = [
    (0, ""),
    (3, " thousand "),
    (6, " million "),
    (9, " billion "),
    (12, " trillion "),
    (15, ""),
]


# 數字轉英文的函式
def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == "0":
        return "zero"
    num_string = num_string.replace(",", "")
    num_length = len(num_string)
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than  " "{0} digits".format(
            max_digits
        )
    num_string = "00" + num_string
    word_string = ""

    # 用迴圈從數字最右邊逐次取三個數字來處理，亦即從右邊三個一組進行轉換
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = (
                num_string[-mag - 3],
                num_string[-mag - 2],
                num_string[-mag - 1],
            )
            if not (hundreds == tens == ones == "0"):
                word_string = _handle1to999(hundreds, tens, ones) + name + word_string


# 處理1~999的函式
def _handle1to999(hundreds, tens, ones):
    if hundreds == "0":
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + " hundred " + _handle1to99(tens, ones)


# 處理1~99的函式
def _handle1to99(tens, ones):
    if tens == "0":
        return _1to9dict[ones]
    elif tens == "1":
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + " " + _1to9dict[ones]


num = "12345678"
# 將第一個命令列參數值轉為英文，其餘命令列參數不處理
result = num2words(num)
print("{0} 的英文念法是: {1}".format(num, result))

print("------------------------------------------------------------")  # 60個

for number in range(100):
    print(format(number, "5d"), end="")
    if number % 10 == 9:
        print()

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

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出, 有r的 後面雙引號內的內容保持不變輸出")
print(str2)

print("------------------------------------------------------------")  # 60個
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


filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

print(get_suffix(filename))

print()

help(get_suffix)  # 測試docstring

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

c = 1 + 3j
print("c的資料型態：", type(c))
print("c是否為複數？", isinstance(1 + 3j, complex))

print("------------------------------------------------------------")  # 60個

print("a", "b", "c", sep="|")
print("a", "b", "c", end="\n\n")

print("------------------------------------------------------------")  # 60個
dslt
prices = {
    "AAPL": 191.88,
    "GOOG": 1186.96,
    "IBM": 149.24,
    "ORCL": 48.44,
    "ACN": 166.89,
    "FB": 208.09,
    "SYMC": 21.29,
}
# 用股票價格大於100元的股票構造一個新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

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

dslt
# 最基本簡單的堆疊

s = []
s.append("吃飯")
s.append("睡覺")
s.append("寫程式")

print(type(s))
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())

print("------------------------------------------------------------")  # 60個

dslt
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

print("有f代入數字")

money = 12345
print(f"正確 你得到獎金 ${money} 元")
print("錯誤 你得到獎金 ${money} 元")

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

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" % (z, z))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" % (1.2345))
print("不足數位預設空格：%6.2f\n" % (1.2345))
print("小數點保留2位：%.2f\n" % (1.2345))
print("不足數位補0(以*替代)：%0*.2f\n" % (6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" % (66))
print("不足數位預設空格：%5d\n" % (66))
print("小於位數則輸出全部：%2d\n" % (666))
print("不足數位補0(以*替代)：%0*d\n" % (5, 66))

print("------------------------------------------------------------")  # 60個

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
    print("索引位置：%s\t對應值：%s\t型態：%s\n" % (i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

strName = "台北永和三支"
strCode = "3388128"
intAount = 123456
intMoney = 456789

print("\n郵局：%s" % (strName))
print("郵局代號為%s，轉帳戶頭為%02d" % (strCode, intAount))
print("匯入金額：%c%.2f" % (36, intMoney))

if intMoney < 20000:
    print("%c\n" % ("成"))

print("------------------------------------------------------------")  # 60個

print("=" * 30, "\n")

print("------------------------------------------------------------")  # 60個

number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(number)
lotto1 = {3, 5, 7, 10, 12}  # 第一組幸運彩蛋
print("第一組樂透:", lotto1)
lotto2 = {2, 5, 6, 11, 12}  # 第二組幸運彩蛋
print("第二組樂透:", lotto2)
lucky = lotto1 | lotto2
print("有 %d 個數字出現在其中一次開獎" % len(lucky), lucky)
biglucky = lotto1 & lotto2
print("有 %d 個數字出現在每一次開獎" % len(biglucky), biglucky)
badnum = number - lucky
print("總共有 %d 個不幸運的數字" % len(badnum), badnum)

print("------------------------------------------------------------")  # 60個

phrase = "Happy holiday."
print("原字串：", phrase)
print("將首字大寫 ", phrase.capitalize())
print("每個單字的首字會大寫", phrase.title())
print("全部轉為小寫字元", phrase.lower())
print("判斷字串首字元是否為大寫", phrase.istitle())
print("是否皆為大寫字元", phrase.isupper())
print("是否皆為小寫字元", phrase.islower())

print("------------------------------------------------------------")  # 60個

wd = "Alex is optimistic and clever."
print("字串:", wd)
print("Alex為開頭的字串嗎", wd.startswith("Alex"))
print("clever為開頭的字串嗎", wd.startswith("clever", 0))
print("optimistic從指定位置的開頭的字串嗎", wd.startswith("optimisti", 8))
print("clever.為結尾字串嗎", wd.endswith("clever."))

print("------------------------------------------------------------")  # 60個

pay = (8000, 7200, 8300, 4700, 5500)
print(pay)
print(type(pay))
print("由小而大：", sorted(pay))
print("由大而小：", sorted(pay, reverse=True))

print("資料仍維持原順序：")
print(pay)

print("------------------------------------------------------------")  # 60個

word1 = "zoo"
word2 = "animal"
print("交換前: ")
print("單字1={},單字2={}".format(word1, word2))

word2, word1 = word1, word2
print("交換後: ")
print("單字1={},單字2={}".format(word1, word2))

print("------------------------------------------------------------")  # 60個

product = (("iPhone", "手機", "我預算的首選"), ("iPad", "平板", "視股票獲利"), ("iPod", "播放", "價格最親民"))

for name, c_name, memo in product:
    print("%-10s %-12s %-10s" % (name, c_name, memo))

print("------------------------------------------------------------")  # 60個


def func(a, b, c):
    x = a + b + c
    return x


print(func(1, 2, 3))

print("------------------------------------------------------------")  # 60個


def func(a, b, c):
    x = a + b + c
    print(x)


print(func(1, 2, 3))

print("------------------------------------------------------------")  # 60個


def equation(x, y, z):
    ans = x * y + z * x + y * z
    return ans


print(equation(z=1, y=2, x=3))
print(equation(3, 2, 1))
print(equation(x=3, y=2, z=1))
print(equation(3, y=2, z=1))

print("------------------------------------------------------------")  # 60個


def square_sum(*arg):
    ans = 0
    for n in arg:
        ans += n * n
    return ans


ans1 = square_sum(1)
print("1*1=", ans1)
ans2 = square_sum(1, 2)
print("1*1+2*2=", ans2)
ans3 = square_sum(1, 2, 3)
print("1*1+2*2+3*3=", ans3)
ans4 = square_sum(1, 3, 5, 7)
print("1*1+3*3+5*5+7*7=", ans4)


def progname(**arg):
    return arg


print(progname(d1="python", d2="java", d3="visual basic"))

print("------------------------------------------------------------")  # 60個


def dinner(mainmeal, *sideorder):
    # 列出所點餐點的主餐及點心副餐
    print("所點的主餐為", mainmeal, "所點的副餐點心包括:")
    for snack in sideorder:
        print(snack)


dinner("鐵板豬", "烤玉米")
dinner("泰式火鍋", "德式香腸", "香焦牛奶", "幸運餅")

print("------------------------------------------------------------")  # 60個


def Pow(x, y):
    p = 1
    for i in range(y + 1):
        p *= x
    return p


print("請輸入兩數x及y的值函數：")
x = 3
y = 8
print("次方運算結果：%d" % Pow(x, y))

print("------------------------------------------------------------")  # 60個


def swap_test(x, y):
    print("函數內交換前：x=%d, y=%d" % (x, y))
    x, y = y, x  # 交換過程
    print("函數內交換前：x=%d, y=%d" % (x, y))


a = 10
b = 20  # 設定a,b的初值
print("函數外交換前：a=%d, b=%d" % (a, b))
swap_test(a, b)  # 函數呼叫
print("函數外交換後：a=%d, b=%d" % (a, b))

print("------------------------------------------------------------")  # 60個

animals = "Python"
print(animals.islower())
print("2023".isdigit())

print("------------------------------------------------------------")  # 60個


def clean_string(s):
    """
    刪除字符串中的 '\n', '\r' 和前後的空白

    :param s: str，待處理的字符串
    :return: str，刪除後的字符串
    """
    # 刪除 '\n' 和 '\r'
    s = s.replace("\n", "").replace("\r", "")
    # 刪除前後空白
    s = s.strip()
    return s


animals = "  Python is a \nprogramming language.\n\r   "
cleaned_str = clean_string(animals)
print(cleaned_str)  # "Python is a programming language."

print("------------------------------------------------------------")  # 60個

lst1 = []
lst2 = [1, 2, 3, 4, 5]
lst3 = [1, "Python", 5.5]
print(lst1)
print("lst2: ", lst2)
print(lst3)

print("------------------------------------------------------------")  # 60個

lst7 = [1, ["tom", "mary", "joe"], [3, 4, 5]]
print("lst7:" + str(lst7))

print("------------------------------------------------------------")  # 60個

lst1 = [1, 2, 3, 4, 5, 6]
print(lst1[0])
print(lst1[1])
print(lst1[-1])
print(lst1[-2])
lst1[1] = 10
lst1[2] = "Python"
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 2, 3, 4, 5, 6]
for e in lst1:
    print(e, end=" ")
print()
animals = ["cat", "dog", "bat"]
for index, animal in enumerate(animals):
    print(index, animal)

print("------------------------------------------------------------")  # 60個

lst2 = [[2, 4], ["cat", "dog", "bat"], [1, 3, 5]]
print(lst2[1][0])
lst2[2][1] = 7
for e1 in lst2:
    for e2 in e1:
        print(e2, end=" ")

print("------------------------------------------------------------")  # 60個

lst2 = [[2, 4], ["cat", "dog", "bat"], [1, 3, 5]]
print(lst2[0][1])

print("------------------------------------------------------------")  # 60個

lst1 = [1, 5]
lst1.append(7)
print(lst1)
lst1.extend([9, 11, 13])
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 5, 7, 9, 11, 13]
lst1.insert(1, 3)
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [1, 3, 5, 7, 9, 11, 13]
del lst1[2]
print(lst1)
e1 = lst1.pop()
print(e1, lst1)
e2 = lst1.pop(1)
print(e2, lst1)
lst1.remove(9)
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [4, 2, 8, 9, 1]
print("lst1 = ", lst1)
s = len(lst1)
print("len(lst1) = ", s)
s = max(lst1)
print("max(lst1) = ", s)
s = min(lst1)
print("min(lst1) = ", s)
animals = "Hello World!"
lst2 = list(animals)
print("lst2 = ", lst2)
for i, v in enumerate(lst2, 0):
    print(i, ":", v, end=" ")
print()
s = sum(lst1)
print("sum(lst1) = ", s)
lst3 = sorted(lst1)
print("lst3 = sorted(lst1) = ", lst3)

print("------------------------------------------------------------")  # 60個

lst1 = [4, 2, 8, 9, 1, 8]
print("lst1 = ", lst1)
s = lst1.count(8)
print("lst1.count(8) = ", s)
s = lst1.index(8)
print("lst1.index(8) = ", s)
s = lst1.index(1)
print("lst1.index(1) = ", s)
lst1.sort()
print("lst1.sort() = ", lst1)
lst1.reverse()
print("lst1.reverse() = ", lst1)

print("------------------------------------------------------------")  # 60個


def find_max_and_index(lst1):
    """
    找出串列lst1中的最大值和最大值的索引
    :param lst1: 一個包含數字元素的串列
    :return: 一個包含最大值和最大值索引的元組
    """
    max_val = float("-inf")  # 初始化最大值
    max_idx = -1  # 初始化最大值索引

    # 遍歷串列，尋找最大值和最大值索引
    for i, val in enumerate(lst1):
        if val > max_val:
            max_val = val
            max_idx = i

    return max_val, max_idx


# 測試程式
my_lst = [34, 12, 45, 23, 78, 56, 98, 101, 22]
result = find_max_and_index(my_lst)
print("最大值：", result[0])
print("最大值索引：", result[1])

print("------------------------------------------------------------")  # 60個


def concatenate_strings(lst1):
    """
    從lst1中抽出是字串的項目，並連接成一個字串回傳。

    :param lst1: 一個含有多個項目的串列
    :type lst1: list
    :return: 連接所有字串項目後的字串
    :rtype: str
    """

    str_lst = [item for item in lst1 if isinstance(item, str)]
    return "".join(str_lst)


my_list = ["Hello", 42, "World", True, "Python"]
result = concatenate_strings(my_list)
print(result)  # 輸出：HelloWorldPython

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a=y)
print(s)

print("------------------------------------------------------------")  # 60個

print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = f"Y= {x} X= {y}"
print(s)

print("------------------------------------------------------------")  # 60個

x = 456
print(f"整數: {x:5d}")
x = 123
print(f"整數: {x:05d}")
x = 123.45678
print(f"浮點數: {x:6.3f}")
x = 200
print(f"二進位: {x:b}")
print(f"八進位: {x:o}")
print(f"十六進位: {x:x}")

print("------------------------------------------------------------")  # 60個

t1 = ()
t2 = (1, 2, 3, 4, 5)
t3 = (1, "Joe", 5.5)
print(t1)
print("t2 = ", t2)
print(t3)

print("------------------------------------------------------------")  # 60個

t4 = tuple()
t5 = tuple(["tom", "mary", "joe"])
t6 = tuple("python")
print("t4 = " + str(t4))
print("t5 = " + str(t5))
print("t6 = " + str(t6))

print("------------------------------------------------------------")  # 60個

# tuple
t1 = (1, 2, 3, 4, 5, 6)
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[-2])

print("------------------------------------------------------------")  # 60個

# tuple
t1 = (1, 2, 3, 4, 5, 6)
for e in t1:
    print(e, end=" ")

print("------------------------------------------------------------")  # 60個

# tuple
t1 = (4, 2, 8, 9, 1)
print("t1 = ", t1)
s = len(t1)
print("len(t1) = ", s)
s = max(t1)
print("max(t1) = ", s)
s = min(t1)
print("min(t1) = ", s)
animals = "Hello World!"
t2 = tuple(animals)
print("t2 = ", t2)
for i, v in enumerate(t2, 0):
    print(str(i) + ":" + v, end=" ")
print()
s = sum(t1)
print("sum(t1) = ", s)
t3 = sorted(t1)
print("t3 = sorted(t1) = ", t3)

print("------------------------------------------------------------")  # 60個

# tuple
t1 = (4, 2, 8, 9, 1, 8)
print("t1 = ", t1)
s = t1.count(8)
print("t1.count(8) = ", s)
s = t1.index(8)
print("t1.index(8) = ", s)
s = t1.index(1)
print("t1.index(1) = ", s)

print("------------------------------------------------------------")  # 60個

# 字典
d1 = {}
d2 = {1: "apple", 2: "ball"}
d3 = {"name": "joe", 1: [2, 4, 6]}
print(d1)
print("d2 = ", d2)
print(d3)

print("------------------------------------------------------------")  # 60個

# 字典
d4 = dict()
d5 = dict([(1, "tom"), (2, "mary"), (3, "john")])
print("d4 = " + str(d4))
print("d5 = " + str(d5))

print("------------------------------------------------------------")  # 60個

# 字典
d1 = {"chicken": 2, "dog": 4, "cat": 3}
print(d1["cat"])
print(d1["dog"])
print(d1["chicken"])

print("------------------------------------------------------------")  # 60個

# 字典
d1 = {"chicken": 2, "dog": 4, "cat": 3}
d1["cat"] = 4
print(d1)

print("------------------------------------------------------------")  # 60個

# 字典
d1 = {"chicken": 2, "dog": 4, "cat": 3}
d1["spider"] = 8
print(d1)

print("------------------------------------------------------------")  # 60個

# 字典
d1 = {"chicken": 2, "dog": 4, "cat": 3}
for animal in d1:
    legs = d1[animal]
    print(animal, legs)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 2: 4, "name": "joe", "age": 20, 5: 22}
del d1[2]
print(d1)
del d1["age"]
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 2: 4, "name": "joe", "age": 20, 5: 22}
e1 = d1.pop(5)
print(e1, d1)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 2: 4, "name": "joe", "age": 20, 5: 22}
e2 = d1.popitem()
print(e2, d1)
e2 = d1.popitem()
print(e2, d1)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 2: 4, "name": "joe", "age": 20, 5: 22}
d1.clear()
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 3: 9, 5: 24, 7: 47, 9: 83}
print("d1 = ", d1)
s = len(d1)
d2 = dict([(1, "tom"), (2, "mary"), (3, "joe")])
print("d2 = ", d2)
d3 = sorted(d1)
print("d3 = sorted(d1) = ", d3)

print("------------------------------------------------------------")  # 60個

d1 = {"tom": 2, "bob": 3, "mike": 4}
print("d1 = ", d1)
i = d1.get("tom")
print("d1.get('tom') = ", i)
i = d1.get("jerry", "不存在")
print("d1.get('jerry', '不存在') = ", i)
t1 = d1.keys()
print("d1.keys() = ", t1)
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")
print()
t1 = d1.values()
print("d1.values() = ", t1)
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")

print("------------------------------------------------------------")  # 60個


def sum_dict_values(d):
    """
    將字典d中的所有值加總並返回總和。

    參數:
    d -- 包含數值的字典。

    返回值:
    所有字典值的總和。
    """
    return sum(d.values())


# 定義一個包含數值的字典
my_dict = {"a": 10, "b": 20, "c": 30}

# 使用 sum_dict_values() 函數獲取所有值的總和
total = sum_dict_values(my_dict)

# 列印總和
print(total)

print("------------------------------------------------------------")  # 60個


def find_max_value(d):
    """
    找出字典值的最大值並回傳。

    Args:
        d: 一個字典。

    Returns:
        字典值的最大值。
    """
    max_value = None  # 初始化最大值為空值
    for value in d.values():  # 遍歷字典的值
        if max_value is None or value > max_value:  # 如果目前值大於最大值
            max_value = value  # 將最大值更新為目前值
    return max_value  # 回傳最大值


# 定義一個字典
my_dict = {"apple": 5, "banana": 2, "orange": 8}

# 呼叫 find_max_value() 函數
max_value = find_max_value(my_dict)

# 列印最大值
print("最大值為：", max_value)

print("------------------------------------------------------------")  # 60個


def create_dict(keys, values):
    """
    建立一個字典，使用傳入的keys作為鍵，values作為值。
    :param keys: 一個包含鍵的串列。
    :param values: 一個包含值的串列，鍵與值一一對應。
    :return: 一個字典，使用傳入的鍵值對建立。
    """
    return dict(zip(keys, values))


keys = ["apple", "banana", "orange"]
values = [1, 2, 3]

my_dict = create_dict(keys, values)

print(my_dict)  # 輸出: {'apple': 1, 'banana': 2, 'orange': 3}

print("------------------------------------------------------------")  # 60個

animals, str2 = "Hello ", "World!"
str3 = animals + str2
print(str3)
lst1, lst2 = [2, 4], [6, 8, 10]
lst3 = lst1 + lst2
print(lst3)
t1, t2 = (2, 4), (6, 8, 10)
t3 = t1 + t2
print(t3)

print("------------------------------------------------------------")  # 60個

animals = "Hello"
str2 = animals * 3
print(str2)
lst1 = [1, 2]
lst2 = lst1 * 3
print(lst2)
t1 = (1, 2)
t2 = t1 * 3
print(t2)

print("------------------------------------------------------------")  # 60個

str = "Welcome!"
print("come" in str)
print("come" not in str)
lst1 = [2, 4, 6, 8]
print(8 in lst1)
print(2 not in lst1)
t1 = (2, 4, 6, 8)
print(8 in t1)
print(2 not in t1)
d1 = {"tom": 2, "joe": 3}
print("tom" in d1)
print("tom" not in d1)

print("------------------------------------------------------------")  # 60個

print("green" == "glow")
print("green" != "glow")
print("green" > "glow")
print("green" >= "glow")
print("green" < "glow")
print("green" <= "glow")
d1 = {"tom": 30, "bobe": 3}
d2 = {"bobe": 3, "tom": 30}
print(d1 == d2)
print(d1 != d2)

print("------------------------------------------------------------")  # 60個

animals = "Hello World!"
print("animals = ", animals)
s = animals[1:3]
print("animals[1:3] = ", s)
s = animals[1:5]
print("animals[1:5] = ", s)
s = animals[:7]
print("animals[:7] = ", s)
s = animals[4:]
print("animals[4:] = ", s)
s = animals[1:-1]
print("animals[1:-1] = ", s)
s = animals[6:-2]
print("animals[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

lst1 = list("Hello World!")
print("lst1 = ", lst1)
s = lst1[1:3]
print("lst1[1:3] = ", s)
s = lst1[1:5]
print("lst1[1:5] = ", s)
s = lst1[:7]
print("lst1[:7] = ", s)
s = lst1[4:]
print("lst1[4:] = ", s)
s = lst1[1:-1]
print("lst1[1:-1] = ", s)
s = lst1[6:-2]
print("lst1[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

t1 = tuple("Hello World!")
print("t1 = ", t1)
s = t1[1:3]
print("t1[1:3] = ", s)
s = t1[1:5]
print("t1[1:5] = ", s)
s = t1[:7]
print("t1[:7] = ", s)
s = t1[4:]
print("t1[4:] = ", s)
s = t1[1:-1]
print("t1[1:-1] = ", s)
s = t1[6:-2]
print("t1[6:-2] = ", s)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:4] = [3, 5, 7]
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[2:2] = [1, 9]
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:3] = []
print(lst1)

print("------------------------------------------------------------")  # 60個

lst1 = [x for x in range(10)]
print(lst1)
lst2 = [x + 1 for x in range(10)]
print(lst2)
lst3 = [x for x in range(10) if x % 2 == 1]
print(lst3)
lst4 = [x * 2 for x in range(10) if x % 2 == 1]
print(lst4)

print("------------------------------------------------------------")  # 60個

d1 = {x: x * x for x in range(10)}
print(d1)
d2 = {x: x * x for x in range(10) if x % 2 == 0}
print(d2)

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

search_str = "yellow"
print("單字 %s 第一次出現的索引值%d" % (search_str, word.index(search_str)))

print("------------------------------------------------------------")  # 60個

no = [105, 25, 8, 179, 60, 57]
print("排序前的資料順序：", no)
no.sort()  # 省略reverse參數, 遞增排序
print("遞增排序：", no)
zoo = ["tiger", "elephant", "lion", "rabbit"]
print("排序前的資料順序：")
print(zoo)
zoo.sort(reverse=True)  # 依字母做遞減排序
print("依單字字母遞減排序：")
print(zoo)

print("------------------------------------------------------------")  # 60個

print("集合")
friendA = {"Andy", "Axel", "Michael", "May"}
friendB = {"Peter", "Axel", "Andy", "Julia"}
print(friendA & friendB)
print(friendA | friendB)
print(friendA - friendB)
print(friendA ^ friendB)

print("------------------------------------------------------------")  # 60個

x = 859
y = 935
print("兩數經交換前的值: ")
print("x={},y={}".format(x, y))
y, x = x, y
print("兩數經交換後的值: ")
print("x={},y={}".format(x, y))

print("------------------------------------------------------------")  # 60個

tup = (28, 39, 58, 67, 97, 54)
print("目前元組內的所有元素：")
for item in range(len(tup)):
    print("tup[%2d] %3d" % (item, tup[item]))

print("------------------------------------------------------------")  # 60個

salary = (86000, 72000, 83000, 47000, 55000)
print("原有資料：")
print(salary)
print("--------------------------------")

# 由小而大
print("薪資由小而大排序：", sorted(salary))
print("--------------------------------")

# 遞減排序
print("薪資由大而小排序：", sorted(salary, reverse=True))
print("--------------------------------")

print("資料經排序後仍保留原資料位置：")
print(salary)
print("--------------------------------")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

original = [
    "abase",
    "abate",
    "abdicate",
    "abhor",
    "abate",
    "acrid",
    "appoint",
    "abate",
    "kindle",
]
print("單字收集的原始內容: ")
print(original)
set1 = set(original)
not_duplicatd = list(set1)
print("刪除重複單字的最佳內容: ")
print(not_duplicatd)
print("按照字母的排列順序: ")
not_duplicatd.sort()
print(not_duplicatd)

print("------------------------------------------------------------")  # 60個


def fun1(obj, price):
    obj = "Microwave"
    print("函數內部修改字串及串列資料")
    print("物品名稱:", obj)
    # 新增價格
    price.append(12000)
    print("物品售價:", price)


obj1 = "TV"  # 未呼叫函數前的字串
price1 = [24000, 18000, 35600]  # 未呼叫函數前的串列
print("函數呼叫前預設的字串及串列")
print("物品名稱:", obj1)
print("物品售價:", price1)
fun1(obj1, price1)

print("函數內部被修改過字串及串列:")
print("名字:", obj1)  # 字串內容沒變
print("分數:", price1)  # 串列內容已改變

print("------------------------------------------------------------")  # 60個

str1 = "do your best what you can do"
s1 = str1.count("do", 0)
s2 = str1.count("o", 0, 20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1, s1, s2))

print("------------------------------------------------------------")  # 60個


def func(x, y, z):
    formula = x * x + y * y + z * z
    return formula


print(func(z=5, y=2, x=7))
print(func(7, 2, 5))
print(func(x=7, y=2, z=5))
print(func(7, y=2, z=5))

print("------------------------------------------------------------")  # 60個

phrase = "never put off until tomorrow what you can do today."
print("原字串：", phrase)
print("將首字大寫 ", phrase.capitalize())
print("每個單字的首字會大寫", phrase.title())
print("全部轉為小寫字元", phrase.lower())
print("判斷字串首字元是否為大寫", phrase.istitle())
print("是否皆為大寫字元", phrase.isupper())
print("是否皆為小寫字元", phrase.islower())

print("------------------------------------------------------------")  # 60個


# 不定長度參數之函數
def myfruit(**arg):
    return arg


print(myfruit(d1="apple", d2="mango", d3="grape"))

print("------------------------------------------------------------")  # 60個

"""
#引數：x 為底數       
#y 為指數       
#傳回值：次方運算結果 
def Pow(x,y):
    p=1
    for i in range(y):
        p *= x
    return p
print("請輸入次方運算（ex.2 3）：")
x,y=input().split()
print('x=',x)
print('y=',y)
print("次方運算結果: %d" %Pow(int(x), int(y)))
"""

print("------------------------------------------------------------")  # 60個

wd = "Python is funny and powerful."
print("字串:", wd)
print("Python為開頭的字串嗎", wd.startswith("Python"))  # 回傳True
print("funny為開頭的字串嗎", wd.startswith("funny", 0))  # 回傳False
print("funny從指定位置的開頭的字串嗎", wd.startswith("funny", 10))  # 回傳True
print("powerful.為結尾字串嗎", wd.endswith("powerful."))  # 回傳True

print("------------------------------------------------------------")  # 60個


def fib(n):  # 定義函數fib()
    if n == 0:
        return 0  # 如果n=0 則傳回 0
    elif n == 1 or n == 2:
        return 1
    else:  # 否則傳回 fib(n-1)+fib(n-2)
        return fib(n - 1) + fib(n - 2)


print("輸入所要計算第幾個費式數列:")
n = 10
for i in range(n + 1):  # 計算前n個費氏數列
    print("fib(%d)=%d" % (i, fib(i)))

print("------------------------------------------------------------")  # 60個

N = 50
data = [0] * N

print(type(data))
print(len(data))

for i in range(len(data)):
    data[i] = i

print("------------------------------------------------------------")  # 60個

a, b, c = 3, 5, 7
# 宣告a、b及c三個整數變數
print("a= %d b= %d c= %d" % (a, b, c))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


# 使用一般函數
def square1(x):
    value = x**2
    return value


# 輸出平方值
print(square1(10))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("請輸入大於1的整數做質數測試 = 119")

num = 119

if num == 2:  # 2是質數所以直接輸出
    print("%d是質數" % num)
else:
    for n in range(2, num):  # 用2 .. num-1當除數測試
        if num % n == 0:  # 如果整除則不是質數
            print("%d不是質數" % num)
            break  # 離開迴圈
    else:  # 否則是質數
        print("%d是質數" % num)

print("------------------------------------------------------------")  # 60個

i = 1  # 設定i初始值
while i <= 9:  # 當i大於9跳出外層迴圈
    j = 1  # 設定j初始值
    while j <= 9:  # 當j大於9跳出內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1  # 內層迴圈加1
    print()  # 換行輸出
    i += 1  # 外層迴圈加1

print("------------------------------------------------------------")  # 60個

players = ["Curry", "Jordan", "James", "Durant", "Obama", "Kevin", "Lin"]
n = 5
if n > len(players):
    n = len(players)  # 列出人數不大於串列元素數
index = 0  # 索引index
while index < len(players):  # 是否index在串列長度範圍
    if index == n:  # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1  # 索引index加1

print("------------------------------------------------------------")  # 60個

index = 0
while index <= 10:
    index += 1
    if index % 2 != 0:  # 測試是否奇數
        continue  # 不往下執行
    print(index)  # 輸出偶數


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
while buyers:  # 執行買家分類迴圈分類完成迴圈才會結束
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


def fun(arg):
    pass


print("------------------------------------------------------------")  # 60個


def fun(arg):
    pass


print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x: x))
print("列出內建函數abs的type類型: ", type(abs))

print("------------------------------------------------------------")  # 60個

print(bool(0))
print(bool(""))
print(bool(" "))
print(bool(1))
print(bool("XYZ"))

print("------------------------------------------------------------")  # 60個

num = 123
print(num)
num1 = bin(num)  # 2進位
print(num1)
num2 = oct(num)  # 8進位
print(num2)

num3 = 1234
print(num3)
print(int(num1, 2))  # 將2進位的字串轉換成10進位數值
print(int(num2, 8))  # 將8進位的字串轉換成10進位數值
# print(int(num3,16))#將16進位的字串轉換成10進位數值 fail in sugar

print("------------------------------------------------------------")  # 60個

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

year = 2024
month = 1
day = 20
print("日期：%s-%s-%s" % (year, month, day))

print("------------------------------------------------------------")  # 60個

print("請輸入一個十進位數: ", end="")
Val = 1234
print("Val的八進位數=%o" % Val)  # 以%o格式化字元輸出
print("Val的十六進位數=%x" % Val)  # 以%x格式化字元輸出

print("------------------------------------------------------------")  # 60個

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

num = 168
print("數字 %s 的浮點數：%5.1f" % (num, num))
print("數字 %s 的八進位：%o" % (num, num))
print("數字 %s 的十六進位：%x" % (num, num))
print("數字 %s 的二進位：%s" % (num, bin(num)))

print("------------------------------------------------------------")  # 60個

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" % (801, "朱正富", 32000, 10000, 5000))
print("%3d %3s %6d %6d %6d" % (805, "曾自強", 35000, 8000, 7000))
print("%3d %3s %6d %6d %6d" % (811, "陳威動", 43000, 15000, 6000))

print("------------------------------------------------------------")  # 60個

print("13579")
print("1+2")
print("Hello, how are you?")
print("I'm all right, but it's raining.")
print("I'm all right, but it's raining.")

print("------------------------------------------------------------")  # 60個

print(type(23))  # 輸出結果 <class 'int'>
print(type(3.14))  # 輸出結果 <class 'float'>
print(type("happy birthday"))  # 輸出結果 <class 'str'>
print(type(True))  # 輸出結果 <class 'bool'>

print("------------------------------------------------------------")  # 60個

num1 = 30
print(num1)
num1 = "happy"
print(num1)
a = b = 12
print(a, b)
name, salary, weight = "陳大富", 60000, 85.7
print(name, salary, weight)

print("------------------------------------------------------------")  # 60個

num = 8
num *= 9
print(num)
num += 1
print(num)
num //= 9
print(num)
num %= 5
print(num)
num -= 2
print(num)

print("------------------------------------------------------------")  # 60個

a, b, c = 5, 10, 6
result = a > b and b > c
# 條件式a>b的傳回值與條件式b>c的傳回值做and運算
result = a < b or c != a
# 條件式a<b的傳回值與條件式c!=a的傳回值做or運算
result = not result
# 將result的值做not運算

print("------------------------------------------------------------")  # 60個

a, b, c = 3, 5, 7  # 宣告a、b及c三個整數變
print("a= %d b= %d c= %d" % (a, b, c))
print("====================================")
print("a<b and b<c or c<a = %d" % (a < b and b < c or c < a))
print("not(a==b)and (not a<b) = %d" % (not (a == b) and (not a < b)))
# 包含關係與邏輯運算子的運算式求值

print("------------------------------------------------------------")  # 60個

b = 13
print(b << 2)
print(b >> 1)

print("------------------------------------------------------------")  # 60個

phrase = ["三陽開泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print("{0}--{1}".format(index, x))

print("------------------------------------------------------------")  # 60個

for a in range(1, 6):  # 外層for迴圈控制
    for b in range(1, a + 1):  # 內層for迴圈控制
        if b == 4:
            break
        print(b, end="")  # 印出b的值
    print()

print("------------------------------------------------------------")  # 60個

total = 0
for count in range(1, 100, 2):
    total += count  # 將數值累加
print("數值1~100之間的奇數累計=", total)

print("------------------------------------------------------------")  # 60個

k = 20
sigma = 0
for n in range(int(k) + 1):
    if n % 2 != 0:  # 如果n是奇數
        sigma += float(-1 / (2 * n + 1))
    else:  # 如果n是偶數
        sigma += float(1 / (2 * n + 1))
print("PI = %f" % (sigma * 4))

print("------------------------------------------------------------")  # 60個

# 不一樣
k = 20
sigma = 0
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

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

x, y = 1, 10
while x < y:
    print(x, end=" ")
    x += 1

print("------------------------------------------------------------")  # 60個

str1 = "Happy birthday to my best friend."
s1 = str1.count("to", 0)  # 從str1字串索引0的位置開始搜尋
s2 = str1.count("e", 0, 34)  # 搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1, s1, s2))

print("------------------------------------------------------------")  # 60個

i = 10
for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" % (z, z))

print("------------------------------------------------------------")  # 60個

"""
dictStudent = {}

def isHasKeyAndNotNone():
    findKey = str(input("請輸入欲查詢的key："))
    
    if findKey in dictStudent and dictStudent.get(findKey, None) == None:
        EditData(findKey)
        
    elif findKey in dictStudent and dictStudent.get(findKey, None) != None:
        print("%s的值：%s" %(findKey, dictStudent[findKey]))
        CheckOtherKeyValue()
        
    else:
        dictStudent.setdefault(findKey, None)
        print("%s不存在已自動建立key" %(findKey))

def EditData(findKey):
    strInputValue = str(input("請輸入值："))
    dictStudent[findKey] = strInputValue
    CheckOtherKeyValue()

def CheckOtherKeyValue():
    for key, values in dictStudent.items():
        if values == None:
            print(dictStudent)
            strCheck = str(input("目前還有其他欄位值為None，是否繼續進行編輯(Y/N)："))

            while strCheck == "Y":
                isHasKeyAndNotNone()
            else:
                print(dictStudent)
                break

strFieldName = str(input("請輸入欄位名稱(以逗號分隔)："))
dictStudent = dictStudent.fromkeys(strFieldName.split(","))

isHasKeyAndNotNone()
"""
print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" % (1.2345))
print("不足數位預設空格：%6.2f\n" % (1.2345))
print("小數點保留2位：%.2f\n" % (1.2345))
print("不足數位補0(以*替代)：%0*.2f\n" % (6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" % (66))
print("不足數位預設空格：%5d\n" % (66))
print("小於位數則輸出全部：%2d\n" % (666))
print("不足數位補0(以*替代)：%0*d\n" % (5, 66))

print("------------------------------------------------------------")  # 60個

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
    print("索引位置：%s\t對應值：%s\t型態：%s\n" % (i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

"""
def EditData():
    if len(strEditTitle) > 0:
        print(strEditTitle)
    else:
        print(strTitle)

    print("作者：", strName)
    print("暱稱：", strId)
    print("Gmail：", strEmail)
    print("興趣：", strJoin)

strTitle = ""
strEditTitle = "撰寫Python小網站"

isEditTitle = str(input("是否要更改名稱(Y/N)："))
isSymbol = str(input("是否要更改前後星號(Y/N)："))

if isEditTitle == "Y" and isSymbol == "Y":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strSymbol = str(input("請輸入欲更改前後符號："))

    strEditTitle = strEditTitle.center(36, strSymbol)
    
elif isEditTitle == "Y" and isSymbol == "N":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strEditTitle = strEditTitle.center(36, "*")

elif isEditTitle == "N" and isSymbol == "Y":
    strSymbol = str(input("請輸入欲更改前後符號："))
    strTitle = strTitle.center(36, strSymbol)

strName = str(input("請輸入名字："))
strId = str(input("請輸入暱稱："))
strEmail = str(input("請輸入Gmail："))

while strEmail.endswith("@gmail.com") == False:
    strEmail = str(input("請重新輸入Gmail："))

strSavor = str(input("你的興趣(以逗號分隔)："))
strJoin = "|".join(strSavor.split(","))


print("="*30, "\n")
EditData()

print("------------------------------------------------------------")  # 60個

tupleData = ()
listData = []

print("\n\n")

strFieldName = str(input("請輸入不可修改欄位名稱(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))
strFieldData = str(input("請輸入欄位對應資料(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))

for i in range(len(strFieldName.split(","))):
    listData.append(strFieldName.split(",")[i])
    
for j in range(len(strFieldData.split(","))):
    x = 0

    if len(listData)%2 == 0:
        x = len(listData) - 1
    else:
        x = len(listData) + 1
        
    listData.insert(x, [strFieldData.split(",")[j] for x in range(1)])
    
listToTuple = tuple(listData)
print("\n")
print("list轉換tuple：", listToTuple)

print("------------------------------------------------------------")  # 60個

#設置底薪(BaseSalary)、結案獎金件數(Case)、職位獎金(OfficeBonus)
BaseSalary = 25000
CaseBonus = 1000
OfficeBonus = 5000

#請輸入職位名稱(Engineer)、結案獎金金額(CaseAmount)變數
Engineer = str(input("請輸入職位名稱："))
Case = int(input("請輸入結案案件數(整數)："))


#計算獎金function
def CalculateCase(case, caseBonus):
    return case * caseBonus

def CalculateSalary(baseSalary, officeBonus):
    return baseSalary + officeBonus

CaseAmount = CalculateCase(Case, CaseBonus)
SalaryAmount = CalculateSalary(BaseSalary, OfficeBonus)

print("該工程師薪資：", CaseAmount + SalaryAmount)
"""
print("------------------------------------------------------------")  # 60個

# id的用法

# 動物字典
fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
print(type(fruits))
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)


print("ccccc")

s1 = "lion"
s2 = "mouse"
print(id(s1))
print(id(s2))

s2 = "lions"
print(id(s1))
print(id(s2))

print("------------------------------------------------------------")  # 60個

msg = """
翠蓋龍旗出建章,鶯啼百囀柳初黃,
昆池冰泮三山近,阿閣花深九陌香,
徑轉虹梁通紫極,庭含玉樹隱霓裳,
侍臣緩步隨鑾輅,岡上應看集鳳皇,
小苑平臨太液池,金舖約戶鎖蟠螭,
雲中帝座飛華蓋,城上鈞陳繞翠旗,
紫氣旋面雙鳳閣,青松還有萬年枝,
從來清蹕深嚴地,開盡碧桃人未知
"""

print(f"<鳳>出現的次數 : {msg.count('鳳')}")

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
search_str = "yellow"
print("單字 %s 第一次出現的索引值%d" % (search_str, word.index(search_str)))

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

word = "maintenance"
word.count("n")

len("thunderbolt")

animal = ["cat", "dog", "duck"]
len(animal)

max(100, 10, 50)
min(300, 30, 3000)

print("------------------------------------------------------------")  # 60個


def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ["", "", ""]
    for i, numeral in enumerate(number):
        if numeral == ".":  # Render the decimal point.
            rows[0] += " "
            rows[1] += " "
            rows[2] += "."
            continue  # Skip the space in between digits.
        elif numeral == "-":  # Render the negative sign:
            rows[0] += "    "
            rows[1] += " __ "
            rows[2] += "    "
        elif numeral == "0":  # Render the 0.
            rows[0] += " __ "
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif numeral == "1":  # Render the 1.
            rows[0] += "    "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "2":  # Render the 2.
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += "|__ "
        elif numeral == "3":  # Render the 3.
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += " __|"
        elif numeral == "4":  # Render the 4.
            rows[0] += "    "
            rows[1] += "|__|"
            rows[2] += "   |"
        elif numeral == "5":  # Render the 5.
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += " __|"
        elif numeral == "6":  # Render the 6.
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif numeral == "7":  # Render the 7.
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "8":  # Render the 8.
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif numeral == "9":  # Render the 9.
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"

        # Add a space (for the space in between numerals) if this
        # isn't the last numeral and the decimal point isn't next:
        if i != len(number) - 1 and number[i + 1] != ".":
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "

    return "\n".join(rows)


print("七段顯示器")

for i in range(0, 1000, 167):
    ccc = getSevSegStr(i, 5)
    print(ccc)

print("------------------------------------------------------------")  # 60個


# 函數文件字串 docstring 註明此函數的功能與用法
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")


greeting("Nelson")


# 用help(函數名稱)列出此函數的文件字串

help(greeting)

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

# 一次改變一個數列
celsius = [21, 25, 29]
fahrenheit = [(x * 9 / 5 + 32) for x in celsius]
print(fahrenheit)

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
print("------------------------------------------------------------")  # 60個

print("置換網址資料")
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type_ = "school"

print(url + city + "&radius=" + str(r) + "&type=" + type_)
print(url + "{}&radius={}&type={}".format(city, r, type_))

my_url = url + f"{city}&radius={r}&type={type_}"
print(my_url)

print("------------------------------------------------------------")  # 60個
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
enumerate_drinks = enumerate(drinks)  # 數值初始是0
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
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個

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

names = ["A太", "B介", "C子", "D郎"]
for i, name in enumerate(names):
    if name == "C子":
        print(i, "號的", name, "找到了。")

print("------------------------------------------------------------")  # 60個


def search(findname):
    names = ["A太", "B介", "C子", "D郎"]
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
    units = ["位元組", "KB", "MB", "GB", "TB", "PB", "EB"]
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

print("------------------------------------------------------------")  # 60­э

# 定義迷宮

# 從左上走到右下 沿著 1 xy相反

maze = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

# 定義方向
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, path):
    # 到達終點
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return path + [(x, y)]

    # 標記已經走過的路徑
    maze[x][y] = -1

    # 遍歷四個方向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 如果下一個位置在範圍內，且還沒有走過，就繼續往下搜尋
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1:
            res = dfs(nx, ny, path + [(x, y)])
            if res:
                return res

    return None


# 從起點開始搜索
path = dfs(0, 0, [])
if path:
    print("找到出口，路徑為：", path + [(len(maze) - 1, len(maze[0]) - 1)])
else:
    print("沒有找到出口")


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

print("in, not in 的用法")
print("1" in "123")  # 字串搜尋：判斷 "1" 是否在 "123" 內，成立顯示True
print("13" in "123")  # 字串搜尋：判斷 "13" 是否在 "123" 內，不成立顯示False
print("M" in "ASP.NET MVC")  # 字串搜尋：判斷 "M" 是否在 "ASP.NET MVC" 內，成立顯示True
print(7 not in [1, 2, 3])  # 串列搜尋：判斷 7 是否不在串列內，成立顯示True
print(1 not in [1, 2, 3])  # 串列搜尋：判斷 1 是否不在串列內，不成顯示False

print("------------------------------------------------------------")  # 60個

print("不同進制表示數字")

num = 15  # 以十進制表示15
num0b = 0b1111  # 以二進制表示15
num0o = 0o17  # 以八進制表示15
num0x = 0xF  # 以十六進制表示15
print(num)  # 印出15，print()函式可印出指定的資料
print(num0b)  # 印出15
print(num0o)  # 印出15
print(num0x)  # 印出15

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

print("%07d" % 12345)  # 空格補零		ð 0012345
print("%-7d" % 12345)  # 靠左對齊		ð 12345ΔΔ
print("%#o" % 12345)  # 顯示八進制符號	ð 0x30071
print("%#x" % 12345)  # 顯示十六進制符號	ð 0x3039
print("% d" % 12345)  # 保留一個空格		ð Δ12345

print("------------------------------------------------------------")  # 60個

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

listSport = ["爬山", "游泳", "跑步", "舉重", "飛輪", "跳水", "瑜珈"]
print(listSport[1:5])  # [1:5] 表示第2到第5個串列元素，顯示 ['游泳', '跑步', '舉重', '飛輪']
print(listSport[:4])  # [:4] 表示第1到第4個串列元素，顯示['爬山', '游泳', '跑步', '舉重']
print(listSport[1:6:2])  # [1:6:2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']
print(listSport[6:1:-2])  # [6:1:-2] 表示第7、5、3個串列元素，顯示['瑜珈', '飛輪', '跑步']
print(listSport[1::2])  # [1::2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']

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


def func():
    n = 10
    print("區域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
func()
print("全域變數n 位址=%d, 值=%d" % (id(n), n))

print("------------------------------------------------------------")  # 60個


def func():
    global n
    n = 10
    print("函式內 全域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))
func()
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))

print("------------------------------------------------------------")  # 60個

listScore = [78, 45, 99, 56, 96]
count = len(listScore)
avg = sum(listScore) / count
print("%d 位學生成績：%s" % (count, listScore))
print("最高成績： %d" % max(listScore))
print("最低成績： %d" % min(listScore))
print("加總成績： %d" % sum(listScore))
print("平均成績： %d" % avg)


cname = "米老鼠"
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

print("二維list")
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

# array.array - C 語言格式數值陣列

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

print(" 姓名    國文    英文    總分    平均")
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰儒", 98, 90, 188, 188 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪雨星", 96, 95, 191, 191 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰雨", 92, 88, 180, 180 / 2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪星宇", 93, 97, 190, 190 / 2))

print("------------------------------------------------------------")  # 60個

# 改成動物資料
print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

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
print("------------------------------------------------------------")  # 60個

# 串列, 元素是串列 => 二維串列
sc = [
    [1, "洪錦魁", 80, 95, 88, 0, 0, 0],
    [2, "洪冰儒", 98, 97, 96, 0, 0, 0],
    [3, "洪雨星", 91, 93, 95, 0, 0, 0],
    [4, "洪冰雨", 92, 94, 90, 0, 0, 0],
    [5, "洪星宇", 92, 97, 90, 0, 0, 0],
]
print(type(sc))
print(type(sc[3]))
print(sc[3])

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
print("------------------------------------------------------------")  # 60個

print("列印小數位數")
dd = 123.456789
print(dd)
print(f"列印小數位數 : {dd}")
print(f"列印小數位數 : {dd:4.2f}")
print(f"列印小數位數 : {dd:4.3f}")
print(f"列印小數位數 : {dd:4.4f}")
print(f"列印小數位數 : {dd:1.4f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 元組不能改變內容，要先轉串列，改完再轉回元組

# 元組
tp = (1, 2, 3, 4, 5)
print(tp)

print("舊的元組內容 : ", tp)

# 元組轉串列
lst = list(tp)
print(lst)

# 修改串列的內容
# newlst = sorted(lst)
newlst = sorted(lst, reverse=True)  # 由大到小排序
print(newlst)

# 串列轉元組
newtp = tuple(newlst)
print("新的元組內容 : ", newtp)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 對字典的排序

noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(type(noodles))
print(noodles)
for noodle, price in sorted(noodles.items(), key=lambda item: item[1]):
    print(noodle, ":", price)


noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60, "大滷麵": 90, "麻醬麵": 70}
print(type(noodles))
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item: item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 改成動物資料
soldier0 = {"tag": "red", "score": 3, "speed": "slow"}  # 建立小兵
soldier1 = {"tag": "blue", "score": 5, "speed": "medium"}
soldier2 = {"tag": "green", "score": 10, "speed": "fast"}
armys = [soldier0, soldier1, soldier2]  # 小兵組成串列
for army in armys:  # 列印小兵
    print(army)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    # 字典
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
print("------------------------------------------------------------")  # 60個


def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])


data = [5, 7, 9, 15, 21, 6]
print(f"mysum = {mysum(data)}")

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
print("------------------------------------------------------------")  # 60個

import bext

bext.fg("yellow")
bext.clear()

# Draw the quit message:
bext.goto(0, 0)
print("Ctrl-C to quit.", end="")

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

print("字串的處理")

print("分割字串")
filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

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

print("請輸入一串列的整數，數目之間利用空白分隔：")
ps = "86 75 92 77 84 76 95"

pitems = ps.split()
pscores = [eval(x) for x in pitems]
pabove = 0
paverage = sum(pscores) / len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數：" + str(paverage))
print("大於或等於平均數的數目：" + str(pabove))
print("小於平均數的數目：" + str(len(pscores) - pabove))

print("------------------------------------------------------------")  # 60個

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f" % ("陳大同", 89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f" % ("楊小明", 77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f" % ("陳時雨", 66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f" % ("李婉玲", 76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f" % ("林研時", 89.25, 99.50, 89.25))

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f" % ("陳大同", 89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f" % ("楊小明", 77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f" % ("陳時雨", 66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f" % ("李婉玲", 76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f" % ("林研時", 89.25, 99.50, 89.25))

print("------------------------------------------------------------")  # 60個

list1 = [50, 40, 20, 40, 20, 60, 20, 80, 90]
print(" 原始串列:", list1)
list1.sort()
list1.reverse()
print(" 由大到小:", list1)

print("------------------------------------------------------------")  # 60個

print("%4s %4s %8s" % ("x", "y", "x**y"))
print("%4d %4d %8d" % (1, 1, 1))
print("%4d %4d %8d" % (2, 2, 4))
print("%4d %4d %8d" % (4, 3, 64))
print("%4d %4d %8d" % (8, 4, 4096))

print("------------------------------------------------------------")  # 60個

i = 1
while i <= 9:
    j = 2
    while j <= 9:
        print("%d*%d=%2d" % (j, i, i * j), end=" ")
        j = j + 1
    print()
    i = i + 1

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("要轉換的十進位數字 = 255")
pnum = 255
presult = ""
while pnum != 0:
    pdata = str(pnum % 2)
    presult = "".join([pdata, presult])
    pnum = pnum // 2
print("轉換為二進位數字為:%s" % presult)

print("------------------------------------------------------------")  # 60個

try:
    print(varn)
except NameError:
    print("變數不存在!")
finally:
    print("程式執行結束例外處理區塊")

print("------------------------------------------------------------")  # 60個


def phi(n):
    presult = 0
    ptemp = 1
    for i in range(1, n + 1, 1):
        presult = presult + ptemp / (2 * i - 1)
        ptemp = -1 * ptemp
    presult = 4 * presult
    return presult


print(phi(900))

print("------------------------------------------------------------")  # 60個

try:
    # pnumber = int(input("請輸入一個整數："))
    pnumber = "aaaa"
    print("所輸入的整數%d" % pnumber)
except Exception as ex:
    print("異常例外：", ex)

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

size = 25

for i in range(size):
    for j in range(size):
        if i % 2 == 1 or j % 2 == 1:
            print("■", end="")
        else:
            print("□", end="")
    print()


print("------------------------------------------------------------")  # 60個

n = 10  # 設定進度條總長
for i in range(n + 1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end="")  # 輸出不換行的內容
    time.sleep(0.05)

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

print("------------------------------------------------------------")  # 60個

# 字串函數
animals = "Hello World!"
animals = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)

animals = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animals = "Python程式設計"
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)

print("------------------------------------------------------------")  # 60個

animals = "welcome to python"
print("animals = ", animals)
b = animals.isalnum()
print("animals.isalnum() = ", b)
b = animals.isalpha()
print("animals.isalpha() = ", b)
b = animals.isdigit()
print("animals.isdigit() = ", b)
b = "2023".isdigit()
print('"2023".isdigit() = ', b)
b = animals.isidentifier()
print("animals.isidentifier() = ", b)
b = animals.islower()
print("animals.islower() = ", b)
b = animals.isupper()
print("animals.isupper() = ", b)
b = "   ".isspace()
print('"   ".isspace() = ', b)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

n = 100
icon = "⋮⋰⋯⋱"  # 建立旋轉的符號清單
for i in range(n + 1):
    print(f"\r{icon[i%4]} {i*100/n}%", end="")
    time.sleep(0.1)

print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
b = a * 2 + 1  # 新增變數 b，計算底部有幾個星星
for i in range(1, b, 2):  # 使用 for 迴圈，從 1～b，每隔 2 個一數
    move = round((b - i) / 2) - 1  # 計算星星的位移空白 ( 要將星星都置中 )
    print(f" " * move, end="")  # 印出星星前方的位移空白 ( 不換行 )
    print("*" * i)  # 加上「幾個星星」( 乘以 i )


print("------------------------------------------------------------")  # 60個

a = 15
b = a * 2 + 1
for i in range(1, b, 4):  # 改成 4 個一數，金字塔每一層就會增加 2，高度也會減半
    move = round((b - i) / 2) - 1
    print(f" " * move, end="")
    print("*" * i)


print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
for i in range(1, a + 1):  # 使用 for 迴圈，重複指定的層數
    print(" " * (a - i) + "*" * (2 * i - 1))
    # ' ' * (a-i) 表示星星數越少，前面空白越多
    # '*' * (2*i-1) 串接後方星星的數量


print("------------------------------------------------------------")  # 60個

a = 10  # 要產生的金字塔層數
for i in range(1, a + 1):  # 使用 for 迴圈，重複 1～10 ( a+1 ) 的數字
    print(" " * 3 * (a - i), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    for j in range(1, i + 1):  # 第二層 for 迴圈，重複不同層內的數字
        if j == 1:  # 如果是第一個數字
            print(j, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    for j in range(i - 1, 0, -1):  # 剛剛的 for 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    print("")  # 最後執行換行的 print


print("------------------------------------------------------------")  # 60個

a = 10
for i in range(1, a + 1):
    print(" " * 3 * (a - i), end="")
    for j in range(0, i):  # ragne 改成從 0 開始，因為 2 的 0 次方等於 1
        k = 2**j  # 計算 2 的幾次方
        if k == 1:
            print(k, end="")
        else:
            print(f"{k:>3d}", end="")
    for j in range(i - 2, -1, -1):  # 修改 range，使其最後一位數為 0
        k = 2**j  # 計算 2 的幾次方
        print(f"{k:>3d}", end="")
    print("")

print("------------------------------------------------------------")  # 60個

a = 10  # 要產生的金字塔層數
b = 1  # 提供 while 迴圈停止的依據
while b <= a:  # 如果 b <= a 就讓 while 迴圈繼續
    n = 1  # 設定從 1 開始
    print(" " * 3 * (a - b), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    while n <= b:  # 第二層 while 迴圈，如果 n <= b 就讓 while 迴圈繼續
        if n == 1:  # 如果是第一個數字
            print(n, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{n:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n + 1  # 將 n 增加 1
    while n > 2:  # 剛剛的 while 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{n-2:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n - 1  # 將 n 減少 1
    print("")  # 最後執行換行的 print
    b = b + 1  # 將 b 增加 1

print("------------------------------------------------------------")  # 60個

local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}

print("輸入身分證字號：")
id_number = "A123456789"
check = False  # 新增 check=False 變數，與 while 迴圈搭配
while True:  # 使用 while 迴圈
    id_arr = list(id_number)  # 新增 id_arr 變數，將身分證字號轉換成串列存入
    if len(id_arr) != 10:
        break  # 判斷如果 id_arr 長度不等於 10，就跳出 while 迴圈
    local = str(local_table[id_arr[0]])  # 將對應的二位數字轉換成字串
    check_arr = list(local)  # 將字串轉換成陣列，例如 '10' 會轉換成 ['1','0']
    check_arr[0] = int(check_arr[0])  # 將串列中的第一個項目轉換成數字
    check_arr[1] = int(check_arr[1]) * 9  # 將串列中的第二個項目轉換成數字
    sex = id_arr[1]  # 取得第二碼數字
    if sex != "1" and sex != "2":
        break  # 判斷如果不是 '1' 也不是 '2' 就跳出 while 迴圈
    check_arr.append(int(sex) * 8)  # 將 sex 內容轉換成數字並乘以 8，存入 check_arr 裡
    for i in range(7):  # 使用 for 迴圈，重複七次
        check_arr.append(int(id_arr[i + 2]) * (7 - i))  # 每次重複，按照檢查碼程式，將數字乘以對應的數值
    check_num = 10 - sum(check_arr) % 10  # 計算使用者輸入的檢查碼
    if check_num != int(id_arr[9]):
        break  # 如果檢查碼不相同，跳出 while 迴圈
    check = True  # 如果迴圈都沒有跳出，讓 check 等於 True。
    break  # 結束後跳出迴圈

if check == False:  # while 迴圈結束後，如果 check 等於 Fasle，表示身分證字號錯誤
    print("身分證字號格式錯誤")
else:
    print("身分證字號正確")


print("------------------------------------------------------------")  # 60個


local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}

print("輸入身分證字號：")
id_number = "A123456789"
check = False
while True:
    try:  # 使用 try
        id_arr = list(id_number)
        if len(id_arr) != 10:
            break
        local = str(local_table[id_arr[0]])
        check_arr = list(local)
        check_arr[0] = int(check_arr[0])
        check_arr[1] = int(check_arr[1]) * 9
        sex = id_arr[1]
        if sex != "1" and sex != "2":
            break
        check_arr.append(int(sex) * 8)
        for i in range(7):
            check_arr.append(int(id_arr[i + 2]) * (7 - i))
        check_num = 10 - sum(check_arr) % 10
        if check_num != int(id_arr[9]):
            break
        check = True
        break
    except:  # 使用 except，如果發生例外狀況，跳出迴圈
        break

if check == False:
    print("身分證字號格式錯誤")
else:
    print("身分證字號正確")

print("------------------------------------------------------------")  # 60個

cc = "ABC" * 5
print(cc)

cc = ["A", "B", "C"] * 5
print(cc)

cc = [1, 2, 3] * 5
print(cc)


cc = "A" * 5
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import re

s = " hello world \n"
print("|" + s.strip() + "|")
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")

# Character stripping
t = "-----hello====="
print(t.lstrip("-"))
print(t.strip("-="))

# 对中间不会影响
s = " hello     world \n"
print(s.strip())

print(s.replace(" ", ""))
print(re.sub("\s+", " ", s))

print("------------------------------------------------------------")  # 60個

text = "Hello World"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 填充字符
print(text.rjust(20, "="))
print(text.center(20, "*"))

# format函数
print(format(text, ">20"))
print(format(text, "<20"))
print(format(text, "^20"))
# 同时增加填充字符
print(format(text, "=>20s"))
print(format(text, "*^20s"))

# 格式化多个值
print("{:=>10s} {:*^10s}".format("Hello", "World"))

# 格式化数字
x = 1.2345
print(format(x, "=^10.2f"))

print("------------------------------------------------------------")  # 60個

"""
#plot 暫存
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]
plt.plot(x, y, marker='d',ms=10, mfc='r', mec='b')
"""

print("------------------------------------------------------------")  # 60個

data = b"wxy\x7a"
print(data)  # b'wxyz'，以ASCII字元輸出

print(type(data), type(data[0]))
# <class 'bytes'>, <class 'int'>

print(data[0], hex(data[0]))
# 'w' ASCII碼119，十六進位'0x77'

print(b"\x7a" in data)  # 可以用 in 來判斷
print(data[2:])  # 可以切片

print("------------------------------------------------------------")  # 60個

data = b"wxy\x7a"
print(data)  # b'wxyz'，以ASCII字元輸出

ba = bytearray(data)
print(type(ba), type(ba[0]))
# <class 'bytearray'>, <class 'int'>

ba[3] = 0x70  # 修改資料
print(ba)  # 變成 bytearray(b'wxyp')

print("------------------------------------------------------------")  # 60個
"""
def inn():
    a = input('輸入文字並轉換為 ASCII：')
    print('{} 的 ASCII：{}'.format(a, ord(a)))
    inn()

inn()
"""
print("------------------------------------------------------------")  # 60個

"""
#按 ctrl + c 離開程式

def wait_for_user_interrupt():
    while True:
        time.sleep(1)
        print("無限迴圈, 按 Ctrl + C 離開")

try:
    wait_for_user_interrupt()
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

import shutil

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

print("string.printable 的用法 ")

import string

print(string.printable)
print(len(string.printable))
abc = string.printable[:-5]  # 取消不可列印字元
print(abc)

print("------------------------------------------------------------")  # 60個
"""
pppp
#print
#print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("圓柱的半徑%6.2f長度%6.2f體積為%6.2f"%(pradius,plength,pvolume))
"""

# pppp
title = "南極旅遊講座"
print("/{0:*^20s}/".format(title))

print("------------------------------------------------------------")  # 60個
# pppp
r = 5
PI = 3.14159
area = PI * r**2
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r, area))
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r, area))
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r, area))
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r, area))

print("------------------------------------------------------------")  # 60個
# pppp
r = 5
PI = 3.14159
area = PI * r**2
print(f"/半徑{r:3d}圓面積是{area:10.2f}/")
print(f"/半徑{r:>3d}圓面積是{area:>10.2f}/")
print(f"/半徑{r:<3d}圓面積是{area:<10.2f}/")
print(f"/半徑{r:^3d}圓面積是{area:^10.2f}/")

print("------------------------------------------------------------")  # 60個

import pyautogui

for i in range(10):
    # 全屏截圖
    # myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(f'./pic_all{i}.png')

    # 部分截圖
    x_st, y_st, w, h = 1920 // 2, 1080 // 2, 1920 // 2 - 50, 1080 // 2 - 50
    myScreenshot = pyautogui.screenshot(region=(x_st, y_st, w, h))
    # 偽存檔
    # myScreenshot.save(f'./pic_part{i}.png')

    time.sleep(5)

print("------------------------------------------------------------")  # 60個

print("filter 的用法")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = filter(lambda x: x > 5, a)
c = list(b)
print(c)

"""
python內建函數
lambda匿名函數
map
filter
sorted
"""
print("------------------------------------------------------------")  # 60個

print(time.time(), " 秒")
print(time.time_ns(), " 微秒")

"""
time.ctime 本地時間
time.localtime() 轉換為struct_time格式的本地時間
time.gmtime() 回傳UTC時間

time.mktime(t) 將struct_time格式的時間轉換回秒數
time.asctime() 將struct_time格式的時間轉換為文字顯示
time.strftime() 將時間轉換為特定格式字串
time.strptime() 將特定格式的字串轉換為struct_time格式的時間
"""

print("------------------------------------------------------------")  # 60個

"""
n = 20                   # 設定進度條總長
for i in range(n+1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end='')   # 輸出不換行的內容
    time.sleep(0.5)

print("------------------------------------------------------------")  # 60個

n = 100
icon = '⋮⋰⋯⋱'          # 建立旋轉的符號清單
for i in range(n+1):
    print(f'\r{icon[i%4]} {i*100/n}%', end='')
    time.sleep(0.1)

"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("末N碼")

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("末10碼", string[-10:])
print("末20碼", string[-20:])
print("末26碼", string[-26:])


print("------------------------------------------------------------")  # 60個

# 函式選單模組


def menu(**options):
    def menu_selector():
        option_string = "/".join(options)
        while True:
            choice = input(f"選擇項目 ({option_string}): ")
            if choice in options:
                return options[choice]
                break
            print("選項不存在!")

    return menu_selector


# 主程式
# from menu import menu


def func_a():
    return "執行函式 A"


def func_b():
    return "執行函式 B"


def func_x():
    return "執行函式 X"


my_menu = menu(a=func_a, b=func_b, x=func_x)

func = my_menu()
print(func())

print("------------------------------------------------------------")  # 60個

name = "鼠"
weight = 3
print("動物{0}的體重是{1}公斤".format(name, weight))

print("動物%s的體重是%d公斤" % (name, weight))


"""
name = input('輸入品名：')
num = int(input('輸入數量：'))
price = float(input('輸入單價：'))
print()
print('品名\t\t數量\t單價\t金額')
print('=========================================')
print('%-14s%-9d%-9.1f%-9.1f' %(name,num,price,num*price))



data = []
site = input("請輸入平台名稱：")
data.append(input("請輸入帳號："))
data.append(input("請輸入密碼："))
print(f"{site}的帳號：{data[0]}；密碼：{data[1]}")


radius = int(input("請輸入球半徑(公分) :"))
volume = compute(radius)
print(f"球半徑 = {radius}公分  球體積 = {volume}立方公分")
"""


from random import randint

rand = set()

while len(rand) < 7:
    rand.add(randint(1, 49))
print("本期樂透彩號碼：")
for idx, num in enumerate(rand, 1):
    print(f"({idx})={num}", end="  ")


print("------------------------------------------------------------")  # 60個

print(543.21)  # 顯示浮點數常值 543.21
print(5.4321e2)  # 顯示浮點數常值 543.21
print(5.4321e6)  # 顯示浮點數常值 5432100.0
print(5.4321e-3)  # 顯示浮點數常值 0.0054321

print("------------------------------------------------------------")  # 60個

name = "李金星"  # 宣告字串變數name，初值設為'李金星'
score = 73  # 宣告整數變數score，初值設為73
msg = "{}的成績是{}分".format(name, score)
print(msg)

name = "李金星"  # 宣告字串變數name，初值設為'李金星'
score = 73  # 宣告整數變數score，初值設為73
msg = "{0}的成績是{1}分".format(name, score)
print(msg)

name = "李金星"  # 宣告字串變數name，初值設為'李金星'
score = 73  # 宣告整數變數score，初值設為73
print("{0}的成績是{1}".format(name, score))

print("------------------------------------------------------------")  # 60個

price = 100
qty = 30
print("單價：{0}     數量：{1}".format(price, qty))
print("打八折後,總金額：{0}".format(price * qty * 0.8))

print("------------------------------------------------------------")  # 60個

print("%s風景區在%s境內" % ("日月潭", "南投縣"))
wt = 3
price = 25
print("%s%d斤，共%d元" % ("香蕉", wt, wt * price))

print("------------------------------------------------------------")  # 60個

print("%d" % 1234)  # 顯示整數,未設寬度
print("%8d" % 1234)  # 顯示整數,寬度有剩補空格,靠右對齊
print("%8d" % -1234)  # 顯示整數,寬度有剩補空格,靠右對齊
print("%3d" % -1234)  # 顯示整數,寬度不足設定無效

print("------------------------------------------------------------")  # 60個

print("%f" % 123.456)  # 顯示數值「123.456000」,小數預設6位
print("%f" % -123.456)  # 顯示數值「-123.456000」,小數預設6位
print("%.2f" % 123.456)  # 顯示數值「123.46」,小數2位,第3位四捨五入
print("%8.2f" % -12.3456)  # 顯示「ΔΔ-12.35」,總寬度8位,小數2位
print("%3.1f" % 123.456)  # 顯示「123.5」,寬度不足設定無效,小數位數1位
print("%8.0f" % -123.456)  # 顯示數值「ΔΔΔ-1235」,小數第1位四捨五入
print("%8.0f" % 123.456)  # 顯示數值「ΔΔΔ1235」,小數第1位四捨五入
print("%g" % 12345.6789)  # 顯示數值「12345.7」,總寬度預設7位
print("%g" % 1.23456789)  # 顯示數值「1.23457」,總寬度預設7位
print("%g" % 12.3)  # 顯示數值「12.3」, 寬度低於預設,直接顯示
print("%g" % 123456.789)  # 顯示數值「123457」,最後1位為小數點不顯示
print("%g" % 1234567.89)  # 顯示數值「1.23457e+06」,整數7位以上,
# 改用科學記號顯示,指數位數佔2位(不含+-號)
print("%10.3G" % 1234.5)  # 顯示「ΔΔ1.23E+03」,寬度10位,E及小數3位

print("------------------------------------------------------------")  # 60個

print("%c" % "M")  # 顯示字元「M」
print("%4c" % "M")  # 顯示字元「ΔΔΔM」,靠右對齊,寬度有剩補空格
print("%c" % 65)  # 顯示字元「A」,65的ASCII碼為「A」
print("%s" % "ABCDE")  # 顯示字串「ABCDE」
print("%8s" % "ABCDE")  # 顯示字串「ΔΔΔABCDE」
print("%3s" % "ABCDE")  # 顯示字串「ABCDE」,總寬度不足設定無效
print("%6.2s" % "ABCDE")  # 顯示字串「ΔΔΔΔAB」,寬度設為6,顯示2字元

print("------------------------------------------------------------")  # 60個

print("%+8d" % 12345)  # 顯示「ΔΔ+12345」,靠右對齊,正數值前加「+」號
print("%+8d" % -12345)  # 顯示「ΔΔ-12345」,靠右對齊,負數值前加「-」號
print("%-8d" % 12345)  # 顯示「12345ΔΔΔ」,靠左對齊,正數值前不加號
print("%-8d" % -12345)  # 顯示「-12345ΔΔ」,靠左對齊,負數值前加「-」號
print("%+8.2f" % 12.345)  # 顯示「ΔΔ+12.35」,靠右對齊,正數值加「+」號
print("%-8.2f" % 12.345)  # 顯示「12.35ΔΔΔ」,靠左對齊,正數值不加號
print("%-8.2f" % -12.345)  # 顯示「-12.35ΔΔ」,靠左對齊,負數值加「-」號
print("%-8s" % "ABCDE")  # 顯示字串「ABCDEΔΔΔ」,靠左對齊,寬度有剩補空格
print("%-6.2s" % "ABCDE")  # 顯示字串「ABΔΔΔΔ」,寬度設為6,顯示2個字元

print("------------------------------------------------------------")  # 60個

print("1234567890!\a")  # 出現音效聲,游標位置在'!'字元後面
print("12345\b67890!")  # 顯示字串「123467890!」,刪除字元'5'
print("1234567890!\n")  # 顯示字串「123467890!」,游標跳到下一行行首
print("123\r4567890!")  # 游標跳到行首,刪除'123',顯示字串「4567890!」
print("123\t45\\67")  # 顯示字串「123ΔΔΔΔΔ45\67」
print('123"45"67')  # 顯示字串「123"45"67」
print("123'4'567")  # 顯示字串「123'4'567」
print("ASCII碼41(Hex):\x41")  # 顯示字串「ASCII碼41(Hex):A」

print("------------------------------------------------------------")  # 60個

a = 100
b = 20
print(a, b)  # 輸出a和b的變數值,分別為100,20
print(id(a), id(b))  # 顯示a和b變數所在的記憶體位址
a, b = b, a  # a,b兩變數的記憶體位址交換
print(a, b)  # 輸出a和b的變數值,分別為20,100
print(id(a), id(b))  # 顯示a和b變數所在的記憶體位址

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("印出一個三維陣列")

dates = [
    [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31]],
    [[2, 3, 6, 7], [10, 11, 14, 15], [18, 19, 22, 23], [26, 27, 30, 31]],
    [[4, 5, 6, 7], [12, 13, 14, 15], [20, 21, 22, 23], [28, 29, 30, 31]],
    [[8, 9, 10, 11], [12, 13, 14, 15], [24, 25, 26, 27], [28, 29, 30, 31]],
    [[16, 17, 18, 19], [20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31]],
]

for i in range(5):
    for j in range(4):
        for k in range(4):
            print(format(dates[i][j][k], "4d"), end=" ")
        print()
    print()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("ddf 搬出")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("print 字串處理 搬出")
print("------------------------------------------------------------")  # 60個

data = (("張三", 86, 60), ("李四", 93, 55), ("王五", 72, 66), ("劉六", 89, 84))

print("編號    姓名      學科    術科    總分")
for idx, dt in enumerate(data):
    print(f"{idx + 1}\t{dt[0]}\t{dt[1]}\t{dt[2]}\t{dt[1] + dt[2]}")

print("------------------------------------------------------------")  # 60個

print("格式化字串")

print(12345)

print("八位數 前面補0")
print("{:08d}\n{:08d}\n{:08d}".format(123, 1234, 12345))

print("------------------------------------------------------------")  # 60個

# 替代字串
TABLE_NAME = "people"
SELECT = "select * from %s order by age, name" % TABLE_NAME

print("select * from %s order by age, name" % TABLE_NAME)
print(SELECT)

key_id = 1234
SELECT = "SELECT * FROM memos WHERE key=?", (str(key_id))
print(SELECT)

print("---- 語法專區 --------------------------------------------------------")  # 60個

print("字串處理")

items = "03/11/2006".split("/")
print(items)

print("------------------------------------------------------------")  # 60個

print("處理網址資料")

target = "https://tw.appledaily.com/new/realtime/{}"

for page in range(1, 11):
    url = target.format(page)
    print(url)

print("------------------------------------------------------------")  # 60個

target_url = "https://www.nkust.edu.tw/p/403-1000-12-{}.php"

for page in range(1, 6):
    html = target_url.format(page)
    print(html)

print("------------------------------------------------------------")  # 60個

print("處理網址資料")

url = "https://www.nkust.edu.tw/p/403-1000-12-{}.php?Lang=zh-tw"
for pg in range(1, 11):
    print(url.format(pg))

url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for cate in [1, 4]:
    for pg in range(1, 6):
        print(url.format(cate, pg))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


id_no = 1
ename = "mouse"
cname = "米老鼠"
weight = 8

print("編號 %d 英文名 %s 中文名 %s 體重 %d" % (id_no, ename, cname, weight))
print("編號 {} 英文名 {} 中文名 {} 體重 {}".format(id_no, ename, cname, weight))

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

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

# 體重
company = "藍海科技股份有限公司"
year = 27
print("{}已成立公司 {} 年".format(company, year))

print("------------------------------------------------------------")  # 60個


num = 1234
print("¨數值 = {0:10d},  數值 = {0:10d}".format(num, num))

num = 123.456789

print("¨數值 = {1:6.3f},  數值 = {1:6.3f}".format(num, num))


print("------------------------------------------------------------")  # 60個

chicken = 20
rabbit = 15
print("雞有 {} 隻, 兔有 {} 隻".format(int(chicken), int(rabbit)))
print("雞有 {} 隻, 兔有 {} 隻".format(chicken, rabbit))

d1 = {"chicken": 2, "dog": 4, "cat": 3}
for animal, legs in d1.items():
    print("動物: {0} 有 {1} 隻腳".format(animal, legs))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("python 語法 搬出")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            image = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            image = image.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            #image.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)
"""

print("------------------------------------------------------------")  # 60個

"""
def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            image = Image.open(path)
            image_rgb = image.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            #image_rgb.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')
"""

print("------------------------------------------------------------")  # 60個

"""
#pitems = ps.split()
pfile = input("請輸入讀取檔案名稱：").strip()

pfile = input("請輸入讀取檔案名稱：").strip()
pinfile = open(pfile, "r")
ps = pinfile.read()  
print(str(len(ps)) + " 字元數") 
print(str(len(ps.split())) + " 單字數") 
print(str(len(ps.split('\n'))) + " 行數") 
pinfile.close()
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("字串replace")
s = """紅豆生南國，春來發幾枝。"""
print(s)
s1 = s.replace("南國", "桃園")
print(s1)

print("------------------------------------------------------------")  # 60個

str1 = "happy \nclever \nwisdom"
print(str1.split())  # 以空格與換行符號(\n)來分割
print(str1.split(" ", 2))

print("------------------------------------------------------------")  # 60個

msg = """CIA Mark told CIA Linda that the secret USB had given to CIA Peter"""
print(f"字串開頭是CIA : {msg.startswith('CIA')}")
print(f"字串結尾是CIA : {msg.endswith('CIA')}")
print(f"CIA出現的次數 : {msg.count('CIA')}")

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

# 各種建立資料的寫法
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

# 含頭尾共N個元素的陣列
N = 11
x = np.linspace(0, 10, 11)  # 建立含11個元素的陣列

print("包含頭尾之linespace :", x)


print("------------------------------------------------------------")  # 60個

n = list(range(100))
r = list(range(25))
n = list(range(10)) * 10

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

print("10位 靠右對齊")

text = "abcdefg"
print(text.rjust(10))

number = 1234567
print(repr(int(number)).rjust(10))

print("------------------------------------------------------------")  # 60個

year = 2023
month = 3
day = 11
total = 123
print(f"{year}年{month}月{day}日是{year}年的第{total}天")

print("------------------------------------------------------------")  # 60個

N = 10
lst = list(range(N))
print(lst)
random.shuffle(lst)
print(lst)

lst.sort()
print(lst)

print("------------------------------------------------------------")  # 60個

print("random.choice 多選一")
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]

cc = random.choice(animals)
print(cc)

print("random.sample 多選多")
cc = random.sample(animals, 3)
print(cc)

animals = "鼠牛虎兔龍蛇"
print("random.sample 多選多")
cc = random.sample(animals, 3)
print(cc)

print("------------------------------------------------------------")  # 60個

number = 1234.5678
print("Number :", format(number, ".2f"))

print("------------------------------------------------------------")  # 60個

"""
PAUSE = 0.02

print('無限迴圈進行中..... 按 Ctrl+C離開 ')

try:
    while True:
        print("A", end = " ")
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.

    print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
   
except KeyboardInterrupt:
    print('你按了 Ctrl+C 離開')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""

print("------------------------------------------------------------")  # 60個
"""
for i in range(5, 0, -1):
    print("\r", "倒计时{}秒！".format(i), end="", flush=True)
    time.sleep(1)
"""

print("------------------------------------------------------------")  # 60個
"""
print('目前的全螢幕截圖')

from PIL import ImageGrab

image = ImageGrab.grab()
filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
image.save(filename)

image = ImageGrab.grab().convert('L')  
data = image.load()
print(type(data))
#print(data.size)
if data[260, 300] > 150:
    #isCollision_day(data)
    print("aaaaaaa")
else:
    #isCollision_night(data)
    print("bbbbbbb")
"""
print("------------------------------------------------------------")  # 60個

##預設是取到整數位，根據小數第一位(如果是5要看個位數，奇進偶捨)判別
print("==Test2==")
print(round(3.5))
print(round(3.6))
print(round(4.5))
print(round(4.6))
##指定取到小數第一位，根據小數第二位(如果是5要看小數第一位，奇進偶捨)判別
print("==Test3==")
print(round(1.35, 1))
print(round(1.36, 1))
print(round(1.45, 1))
print(round(1.46, 1))

print("字串的對齊 justify")

print("01234567890123456789")
print("==Test1==")
string1 = str(153)
print(string1)
# center()指定寬度置中對齊
print(string1.center(20))
# ljust()指定寬度靠左對齊
print(string1.ljust(20))
# rjust()指定寬度靠右對齊
print(string1.rjust(20))
print("==Test2==")
# center()指定寬度置中對齊，指定補齊填補字元
print(string1.center(20, "-"))
# ljust()指定寬度靠左對齊，指定補齊填補字元
print(string1.ljust(20, "-"))
# rjust()指定寬度靠右對齊，指定補齊填補字元
print(string1.rjust(20, "-"))
print("==Test3==")
# zfill()指定寬度靠右對齊，以'0'補齊
print(string1.zfill(20))

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

url = "http://jigsaw.w3.org/HTTP/connection.html"
response = requests.get(url)
# 指定html.parser作為解析器
soup = BeautifulSoup(response.text, "html.parser")
# 把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
# 必須借助於Beautiful Shop套件
print(soup.prettify())
# find_all()回傳的格式是串列list
# 而且contens的內容也是串列list
a_tags = soup.find_all("title")
for a_tag in a_tags:
    for b in a_tag.contents:
        print(str(b).strip())
a_tags = soup.find_all("h1")
for a_tag in a_tags:
    cc = ""
    for b in a_tag.contents:
        b = (
            str(b)
            .replace("<i>", "")
            .replace("</i>", "")
            .replace("\n", "")
            .replace("\r", "")
        )
        cc = cc + b
    print(cc.strip())

print("------------------------------------------------------------")  # 60個

student_all = [15463, 22825, 14757, 21441]
student_university = [9093, 12010, 13090, 18176]
student_graduate = [6370, 10815, 1667, 3265]
labels = ["中興大學", "成功大學", "東海大學", "逢甲大學"]

print(student_all)

for i in range(4):
    print(student_university[i] + student_graduate[i])

print("------------------------------------------------------------")  # 60個

file1 = open("handgame.py", "w", encoding="UTF-8")  # 打開檔案，建立handgame.py
file1.write("import random\n")
file1.write("handgesture=['剪刀','石頭','布']\n")
file1.write("def hand():\n")
file1.write("\treturn random.choice(handgesture)")
file1.close()  # 關閉檔案
# 建立games資料夾
#!mkdir games
file1 = open("games/dice.py", "w", encoding="UTF-8")  # 打開檔案，建立games/dice.py
file1.write("from random import choice\n")
file1.write("def dice():\n")
file1.write("\treturn choice(range(1,7))")
file1.close()  # 關閉檔案
file1 = open("games/hand.py", "w", encoding="UTF-8")  # 打開檔案，建立games/hand.py
file1.write("from random import choice\n")
file1.write("handgesture=['剪刀','石頭','布']\n")
file1.write("def hand():\n")
file1.write("\treturn choice(handgesture)")
file1.close()  # 關閉檔案
file1 = open("games/poker.py", "w", encoding="UTF-8")  # 打開檔案，建立games/poker.py
file1.write("from random import choice\n")
file1.write("pokerkind=['♠','♥','♦','♣']\n")
file1.write("pokerpoint=['A','2','3','4','5','6','7','8','9','10','J','Q','K']\n")
file1.write("def poker():\n")
file1.write("\treturn choice(pokerkind)+choice(pokerpoint)")
file1.close()  # 關閉檔案
file1 = open("games/coin.py", "w", encoding="UTF-8")  # 打開檔案，建立games/coin.py
file1.write("from random import choice\n")
file1.write("coinkind=['正面','反面']\n")
file1.write("def coin():\n")
file1.write("\treturn choice(coinkind)")
file1.close()  # 關閉檔案
file1 = open("handgames.py", "w", encoding="UTF-8")  # 打開檔案，建立handgames.py
file1.write("import handgame as hg\n")
file1.write("def handgame():\n")
file1.write("\tcomputer=hg.hand()\n")
file1.write("\thgs=''\n")
file1.write("\tfor i in range(0,len(hg.handgesture)):\n")
file1.write("\t\thgs=hgs+str(i)+hg.handgesture[i]\n")
file1.write("\tyourchoice=int(input('請輸入你的選擇'+hgs+': '))\n")
file1.write("\tyou=hg.handgesture[yourchoice]\n")
file1.write("\tprint('You:',you,'Computer:',computer)\n")
file1.write(
    "\tif (computer=='剪刀' and you=='布') or (computer=='布' and you=='石頭') or (computer=='石頭' and you=='剪刀'): \n"
)
file1.write("\t\tprint('電腦獲勝')\n")
file1.write("\telif computer==you:\n")
file1.write("\t\tprint('平手')\n")
file1.write("\telse:\n")
file1.write("\t\tprint('你獲勝')\n")
file1.write("if __name__=='__main__':\n")
file1.write("\tfor i in range(3):\n")
file1.write("\t\thandgame()\n")
file1.write("else:\n")
file1.write("\tprint('被import使用中')")
file1.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

import subprocess
from os import path
import re

"""
for folder, subfolders, filenames in os.walk("."):
    for filename in filenames:
        fullpath = path.join(folder, filename)
        if fullpath.lower().endswith(".ipynb"):
            print(fullpath)
            #subprocess.call(["ipython", "trust", fullpath, "--profile", "scipybook2"])
"""
print("------------------------------------------------------------")  # 60個

# from IPython.nbformat import read

links = []
for folder, _, filenames in os.walk("."):
    for filename in filenames:
        if re.match(r"\w+-[0-9a-zA-Z]\d\d-.+?\.ipynb$", filename):
            fullpath = path.join(folder, filename)
            print(fullpath)
            """
            book = read(fullpath, 4)
            for cell in book.cells:
                if cell.cell_type == "markdown" and cell.source.startswith("#"):
                    title = cell.source.strip("# ")
                    name = path.splitext(filename)[0]
                    folder = path.basename(folder)
                    link = u"[{title} - {name}]({folder}/{name}.ipynb)".format(
                        title=title, name=name, folder=folder)
                    links.append(link)
                    break
            """

from IPython.display import display_markdown  # 用IPython
from IPython.display import Markdown  # 用IPython

display_markdown(Markdown("\n\n".join(links)))


from os import path
import json

kernel_folder = "tttttttt"

python3_path = "C:\\WinPython-64bit-3.4.3.3\\scripts\\python.bat"

if not path.exists(kernel_folder):
    os.mkdir(kernel_folder)

kernel_fn = path.join(kernel_folder, "kernel.json")

kernel_settings = {
    "argv": [python3_path, "-m", "IPython.kernel", "-f", "{connection_file}"],
    "display_name": "Python3-64bit",
    "language": "python",
}

with open(kernel_fn, "w") as f:
    json.dump(kernel_settings, f, indent=4)

print("------------------------------------------------------------")  # 60個

print("網址編碼解碼")

from urllib.request import quote, unquote

print("網址編碼 utf-8")

url = "https://www.baidu.com/s?wd=中国"

# utf8编码，指定安全字符
ret1 = quote(url, safe=";/?:@&=+$,", encoding="utf-8")
print(ret1)

print("網址編碼 gbk")
# https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD
ret2 = quote(url, encoding="gbk")
print(ret2)
# https%3A//www.baidu.com/s%3Fwd%3D%D6%D0%B9%FA

print("網址解碼 utf-8")
url = "https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD"
ret3 = unquote(url, encoding="utf-8")
print(ret3)
# https://www.baidu.com/s?wd=中国

print("網址編碼 預設")
cc = quote("中文測試")
#'%E4%B8%AD%E6%96%87%E6%B8%AC%E8%A9%A6'
print(cc)

print("網址編碼 utf-8")
cc = quote("中文測試".encode("utf-8"))
#'%E4%B8%AD%E6%96%87%E6%B8%AC%E8%A9%A6'
print(cc)

print("網址編碼 big5")
cc = quote("中文測試".encode("big5"))
#'%E4%B8%AD%E6%96%87%E6%B8%AC%E8%A9%A6'
print(cc)

print("網址編碼 gbk")
cc = quote("中文測試".encode("gbk"))
#'%E4%B8%AD%E6%96%87%E6%B8%AC%E8%A9%A6'
print(cc)

print("網址解碼 utf-8")
url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/%E8%A5%BF%E8%9E%BA%E5%A4%A7%E6%A9%8B_%28cropped%29.jpg"
ret3 = unquote(url, encoding="utf-8")
print(ret3)
# https://www.baidu.com/s?wd=中国

print("網址再解碼 utf-8")
url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/西螺大橋_(cropped).jpg"
ret3 = unquote(url, encoding="utf-8")
print(ret3)
# https://www.baidu.com/s?wd=中国

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("數據處理的方法")
x1 = np.linspace(-1.5, 1.5, 31)
y1 = np.cos(x1) ** 2
print(len(y1))

# 移除 y1 > 0.9 的點
x2 = x1[y1 <= 0.9]
y2 = y1[y1 <= 0.9]

# 遮罩 y1 > 0.7 的點, 遮罩就是不要的
y3 = np.ma.masked_where(y1 > 0.7, y1)
print("y1")
print(len(y1))
print(y1)
print("y3")
print(len(y3))
print(y3)

# 將 y1 > 0.3 的點設為 NaN
y4 = y1.copy()
print("y4")
print(len(y4))
print(y4)
y4[y4 > 0.3] = np.nan
print("y4")
print(len(y4))
print(y4)

plt.scatter(x1, y1, c="r", s=300, label="原始資料")
plt.scatter(
    x2, y2, marker="o", facecolors="none", edgecolors="g", s=150, label="移除>0.9的"
)
plt.scatter(x1, y3, c="b", s=80, label="移除>0.7的")
plt.scatter(x1, y4, c="m", s=30, label="移除>0.3的")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個

print("特殊語法保留")
n = 100000
cc = np.sum(4.0 / np.r_[1:n:4, -3:-n:-4])
print(cc)

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

print("十進位 轉 十六進位")
y = 65535  # 10進位
print(hex(y))  # 十進位 轉 十六進位


"""
#hex()回傳參數的十六進位值
##輸出結果數字前面0x代表十六進位(hexdecimal)
print(hex(10))

x = 0x5D  # 這是16進為整數
print(x)  # 列出10進位的結果

y = 93  # 這是10進為整數
# print(hex(y))  # 列出轉換成16進位的結果  fail in sugar


print("十六進位", hex(number))

y = 93  # 這是10進位整數
print(hex(y))  # 列出轉換成16進位的結果


for i in range(32):
    print(hex(i))
"""

# 字串轉數值,10進位整數
print(int("13", 10))
# 字串轉數值,2進位整數
print(int("1001", 2))
# 字串轉數值,浮點數
print(float("3.14"))

# bin()回傳參數的二進位值
##輸出結果數字前面0b代表二進位(binary)
print(bin(10))
# oct()回傳參數的八進位值
##輸出結果數字前面0o代表八進位(octal)
print(oct(10))

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

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

x = 0b1101  # 這是2進為整數
print(x)  # 列出10進位的結果
y = 13  # 這是10進為整數
print(bin(y))  # 列出轉換成2進位的結果

print("------------------------------------------------------------")  # 60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print("------------------------------------------------------------")  # 60個

print("int(9.6)=", int(9.6))
print("bin(20)=", bin(20))

# print('hex(66)=',hex(66))  fail in sugar
print("oct(135)=", oct(135))
print("float(70)=", float(70))
print("abs(-3.9)=", abs(-3.9))
print("chr(69)=", chr(69))
print("ord('%s')=%d" % ("D", ord("D")))
print("str(543)=", str(543))

print("------------------------------------------------------------")  # 60個

st = 10
sp = 20

for number in range(st, sp):  # Main program loop.
    # Convert to hexadecimal/binary and remove the prefix:
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print("DEC:", number, "   HEX:", hexNumber, "   BIN:", binNumber)

print("------------------------------------------------------------")  # 60個

print("進位轉換")

number = 255
print("型別：", type(number))
print("二進位：", bin(number))
print("八進位", oct(number))

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


# chap8-01
# Cars基礎類別
class Cars:
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        self.__factory = factory  # 廠牌屬性(保護)
        self.__model = model  # 型號屬性(保護)
        self.color = color  # 顏色屬性(可改)
        self.seat = seat  # 座位屬性(可改)
        self.__displacement = displacement  # 排氣量或電功率屬性(保護)

    # 屬性(Attribute)
    # 函式唯讀
    # 傳回製造商出廠資料
    def manufacture(self):
        if self.__model.find("電能") >= 0:
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "HP"
            )
        else:
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "CC"
            )

    # 傳回排氣量或電功率(保護)
    def displacement(self):
        return self.__displacement

    # 傳回燃料稅(因為汽油、柴油、電能車計算方式不同，交由各子類別自行定義函式)
    def fueltax(self):
        pass

    # 傳回牌照稅(因為主要的汽油、柴油都是以排氣量計算，只有電能車不同，另外覆寫即可)
    def licensetax(self):
        if self.__displacement <= 500:
            return 1620
        elif self.__displacement <= 600:
            return 2160
        elif self.__displacement <= 1200:
            return 4320
        elif self.__displacement <= 1800:
            return 7120
        elif self.__displacement <= 2400:
            return 11230
        elif self.__displacement <= 3000:
            return 15210
        elif self.__displacement <= 3600:
            return 28220
        elif self.__displacement <= 4200:
            return 28220
        elif self.__displacement <= 4800:
            return 46170
        else:
            return 46170

    # 傳回全部稅金
    def totaltax(self):
        return self.fueltax() + self.licensetax()

    # 方法(Method)
    # 輸出汽車屬性
    def info(self):
        if self.__model.find("電能") >= 0:
            print(
                self.__factory
                + "-"
                + self.__model
                + "-"
                + self.color
                + "色-"
                + str(self.seat)
                + "人座"
                + str(self.__displacement)
                + "HP"
            )
        else:
            print(
                self.__factory
                + "-"
                + self.__model
                + "-"
                + self.color
                + "色-"
                + str(self.seat)
                + "人座"
                + str(self.__displacement)
                + "CC"
            )


# 汽油車衍生類別
class GasolineCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "汽油" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回燃料稅
    def fueltax(self):
        if self.displacement() <= 500:
            return 2160
        elif self.displacement() <= 600:
            return 2880
        elif self.displacement() <= 1200:
            return 4320
        elif self.displacement() <= 1800:
            return 4800
        elif self.displacement() <= 2400:
            return 6180
        elif self.displacement() <= 3000:
            return 7200
        elif self.displacement() <= 3600:
            return 8640
        elif self.displacement() <= 4200:
            return 9810
        elif self.displacement() <= 4800:
            return 11220
        else:
            return 12180


# 柴油車衍生類別
class DieselCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "柴油" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回燃料稅
    def fueltax(self):
        if self.displacement() <= 1800:
            return 2880
        elif self.displacement() <= 2400:
            return 3708
        elif self.displacement() <= 3000:
            return 4320
        elif self.displacement() <= 3600:
            return 5184
        elif self.displacement() <= 4200:
            return 5886
        elif self.displacement() <= 4800:
            return 6732
        else:
            return 7308


# 電能車衍生類別
class ElectricCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "電能" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回牌照稅
    def licensetax(self):
        return 0

    # 傳回燃料稅
    def fueltax(self):
        return 0


def tax(obj):
    print(obj.manufacture(), ":", obj.totaltax())


# 建構第1輛汽油車物件
print("==Test1==")
a = GasolineCars("CITROEN", "BX16TGS", "灰", 5, 1580)
print(type(a))
print(a.manufacture())
a.info()
print(a.fueltax())
print(a.licensetax())
print(a.totaltax())
# 可以修改屬性
a.color = "綠"
a.seat = 2
print(a.manufacture())
a.info()
# 建構第2輛柴油車物件
print("==Test2==")
b = DieselCars("福特六和", "C346-9W", "白", 5, 1997)
print(type(b))
print(b.manufacture())
b.info()
print(b.fueltax())
print(b.licensetax())
print(b.totaltax())
# 建構第3輛電能車物件
print("==Test3==")
c = ElectricCars("Tesla", "Model 3", "紅", 5, 346)
print(type(c))
print(c.manufacture())
c.info()
print(c.fueltax())
print(c.licensetax())
print(c.totaltax())
print("==Test4==")
tax(a)
tax(b)
tax(c)

print("------------------------------------------------------------")  # 60個


# chap8-02
# 輪胎類別
class Wheels:
    # 建構式
    def __init__(self, width, diameter):
        self.width = width  # 寬度屬性
        self.diameter = diameter  # 直徑屬性

    # 自訂義Wheels物件的比較關係(判斷是否相等)
    # 判斷兩個輪胎是否為相同類型根據輪胎寬度、直徑
    def __eq__(self, other):
        return self.width == other.width and self.diameter == other.diameter

    def eq(self, other):
        return self.width == other.width and self.diameter == other.diameter

    # 屬性(Attribute)
    def dimension(self):
        return "寬" + str(self.width) + "mm" + " 直徑" + str(self.diameter) + "inch"

    # 方法(Method)
    # 輸出輪胎屬性
    def info(self):
        print("寬" + str(self.width) + "mm" + " 直徑" + str(self.diameter) + "inch")


# 機車基礎類別
class Motorcycles:
    # 類別方法變數
    counts = 0

    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        self.__factory = factory  # 廠牌屬性
        self.__model = model  # 型號屬性
        self.color = color  # 顏色屬性
        self.__displacement = displacement  # 排氣量或電功率屬性
        self.wheel = wheel  # 輪胎屬性
        # 改變類別方法變數
        Motorcycles.counts = Motorcycles.counts + 1

    # 解構式
    def __del__(self):
        # 改變類別方法變數
        Motorcycles.counts = Motorcycles.counts - 1

    # 自訂義Motorcycles物件的比較關係(判斷是否相等)
    # 判斷兩台機車是否為相同類型根據廠商、型號、排氣量
    def __eq__(self, other):
        return (
            self.__factory == other.__factory
            and self.__model == other.__model
            and self.__displacement == other.__displacement
        )

    def eq(self, other):
        return (
            self.__factory == other.__factory
            and self.__model == other.__model
            and self.__displacement == other.__displacement
        )

    # 類別方法
    @classmethod
    # 顯示類別方法變數
    def motocycles_counts(cls):
        return cls.counts

    # 屬性(Attribute)
    # 函式唯讀
    # 傳回製造商出廠資料
    def manufacture(self):
        if self.__model.startswith("汽油"):
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "CC"
            )
        else:
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "HP"
            )

    # 傳回排氣量或電功率(保護)
    def displacement(self):
        return self.__displacement

    # 傳回燃料稅(以汽油機車為主，電能車不同，另外覆寫即可)
    def fueltax(self):
        if self.displacement() <= 50:
            return 300
        elif self.displacement() <= 125:
            return 450
        elif self.displacement() <= 250:
            return 600
        elif self.displacement() <= 500:
            return 900
        elif self.displacement() <= 600:
            return 1200
        elif self.displacement() <= 1200:
            return 1800
        else:
            return 2010

    # 傳回牌照稅(因為汽油是以排氣量計算，只有電能車不同，另外覆寫即可)
    def licensetax(self):
        if self.displacement() <= 150:
            return 0
        elif self.displacement() <= 250:
            return 800
        elif self.displacement() <= 500:
            return 1620
        elif self.displacement() <= 600:
            return 2160
        elif self.displacement() <= 1200:
            return 4320
        elif self.displacement() <= 1800:
            return 7120
        else:
            return 11230

    # 傳回全部稅金
    def totaltax(self):
        return self.fueltax() + self.licensetax()

    # 方法(Method)
    # 輸出機車屬性
    def info(self):
        if self.__model.startswith("汽油"):
            print(
                self.__factory
                + "-"
                + self.__model
                + "-"
                + self.color
                + "色-"
                + str(self.displacement())
                + "CC 輪胎"
                + self.wheel.dimension()
            )
        else:
            print(
                self.__factory
                + "-"
                + self.__model
                + "-"
                + self.color
                + "色-"
                + str(self.displacement())
                + "HP 輪胎"
                + self.wheel.dimension()
            )


class GasolineMotorcycles(Motorcycles):
    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        super().__init__(factory, "汽油" + model, color, displacement, wheel)


class ElectricMotorcycles(Motorcycles):
    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        super().__init__(factory, "電能" + model, color, displacement, wheel)

    # 傳回燃料稅(0元)
    def fueltax(self):
        return 0

    # 傳回牌照稅(0元)
    def licensetax(self):
        return 0


# 建立第1台機車
print("==Test1==")
d = GasolineMotorcycles("光陽", "SJ25JF", "白黑銀", 124, Wheels(100, 10))
# print(type(d))
print(d.manufacture())
d.info()
print(d.fueltax())
print(d.licensetax())
print(d.totaltax())
# 建立第2台機車
print("==Test2==")
e = GasolineMotorcycles("功學社", "CT-50", "白紅", 49, Wheels(100, 10))
# print(type(e))
print(e.manufacture())
e.info()
print(e.fueltax())
print(e.licensetax())
print(e.totaltax())
# 建立第3台機車
print("==Test3==")
f = ElectricMotorcycles("睿能", "GHS6B2", "白", 8.58, Wheels(100, 10))
# print(type(f))
print(f.manufacture())
f.info()
print(f.fueltax())
print(f.licensetax())
print(f.totaltax())
# 建立第4台機車
print("==Test4==")
g = GasolineMotorcycles("光陽", "SK60AF", "深藍", 298, Wheels(100, 10))
# print(type(g))
print(g.manufacture())
g.info()
print(g.fueltax())
print(g.licensetax())
print(g.totaltax())
# 建立第5台機車
print("==Test5==")
h = ElectricMotorcycles("睿能", "GHS6B2", "紅", 8.58, Wheels(100, 10))
# print(type(h))
print(h.manufacture())
h.info()
print(h.fueltax())
print(h.licensetax())
print(h.totaltax())
# 判斷f與h這兩台機車是否為相同類型
print("==Test6==")
f.info()
h.info()
print(f == h)
# 判斷d與e這兩台機車的輪台是否為相同類型
d.wheel.info()
e.wheel.info()
print(d.wheel.eq(e.wheel))
print(d.wheel == e.wheel)
print("==Test7==")
# 查看總共新增了幾台機車
print(Motorcycles.counts)
# 刪除d車
del d
print(Motorcycles.counts)
# 刪除e車
del e
print(Motorcycles.counts)
# 刪除f車
del f
print(Motorcycles.counts)
# 刪除g車
del g
print(Motorcycles.counts)
# 刪除h車
del h
print(Motorcycles.counts)

print("------------------------------------------------------------")  # 60個


# chap8-03
# 輪胎類別
class Wheels:
    # 建構式
    def __init__(self, width, diameter):
        self.width = width  # 寬度屬性
        self.diameter = diameter  # 直徑屬性

    # 自訂義Wheels物件的比較關係(判斷是否相等)
    # 判斷兩個輪胎是否為相同類型根據輪胎寬度、直徑
    def __eq__(self, other):
        return self.width == other.width and self.diameter == other.diameter

    def eq(self, other):
        return self.width == other.width and self.diameter == other.diameter

    # 屬性(Attribute)
    def dimension(self):
        return "寬" + str(self.width) + "mm" + " 直徑" + str(self.diameter) + "inch"

    # 方法(Method)
    # 輸出輪胎屬性
    def info(self):
        print("寬" + str(self.width) + "mm" + " 直徑" + str(self.diameter) + "inch")


# 車輛基礎類別
class Vehicles:
    # 建構式
    def __init__(self, factory, model, color, displacement):
        self.__factory = factory  # 廠牌屬性
        self.__model = model  # 型號屬性
        self.color = color  # 顏色屬性
        self.__displacement = displacement  # 排氣量或電功率屬性

    # 自訂義車輛物件的比較關係(判斷是否相等)
    # 判斷兩車輛是否為相同類型根據廠商、型號、排氣量
    def __eq__(self, other):
        return (
            self.__factory == other.__factory
            and self.__model == other.__model
            and self.__displacement == other.__displacement
        )

    def eq(self, other):
        return (
            self.__factory == other.__factory
            and self.__model == other.__model
            and self.__displacement == other.__displacement
        )

    # 屬性(Attribute)
    # 函式唯讀
    # 傳回製造商出廠資料
    def manufacture(self):
        if self.__model.startswith("汽油"):
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "CC"
            )
        else:
            return (
                self.__factory
                + "-"
                + self.__model
                + "-"
                + str(self.__displacement)
                + "HP"
            )

    # 傳回排氣量或電功率(保護)
    def displacement(self):
        return self.__displacement

    # 傳回燃料稅(另外覆寫即可)
    def fueltax(self):
        pass

    # 傳回牌照稅(因為汽油是以排氣量計算，只有電能車不同，另外覆寫即可)
    def licensetax(self):
        if self.displacement() <= 125:
            return 0
        elif self.displacement() <= 250:
            return 800
        elif self.displacement() <= 500:
            return 1620
        elif self.__displacement <= 600:
            return 2160
        elif self.__displacement <= 1200:
            return 4320
        elif self.__displacement <= 1800:
            return 7120
        elif self.__displacement <= 2400:
            return 11230
        elif self.__displacement <= 3000:
            return 15210
        elif self.__displacement <= 3600:
            return 28220
        elif self.__displacement <= 4200:
            return 28220
        elif self.__displacement <= 4800:
            return 46170
        else:
            return 46170

    # 傳回全部稅金
    def totaltax(self):
        return self.fueltax() + self.licensetax()

    # 方法(Method)
    # 輸出車輛屬性
    def info(self):
        if self.__model.startswith("電能"):
            if self.__model.find("機車") >= 0:
                print(
                    self.__factory
                    + "-"
                    + self.__model
                    + "-"
                    + self.color
                    + "色-"
                    + str(self.displacement())
                    + "HP 輪胎"
                    + self.wheel.dimension()
                )
            else:
                print(
                    self.__factory
                    + "-"
                    + self.__model
                    + "-"
                    + self.color
                    + "色-"
                    + str(self.seat)
                    + "人座"
                    + str(self.__displacement)
                    + "HP"
                )
        else:
            if self.__model.find("機車") >= 0:
                print(
                    self.__factory
                    + "-"
                    + self.__model
                    + "-"
                    + self.color
                    + "色-"
                    + str(self.displacement())
                    + "CC 輪胎"
                    + self.wheel.dimension()
                )
            else:
                print(
                    self.__factory
                    + "-"
                    + self.__model
                    + "-"
                    + self.color
                    + "色-"
                    + str(self.seat)
                    + "人座"
                    + str(self.__displacement)
                    + "CC"
                )


# 機車基礎類別
class Motorcycles(Vehicles):
    # 類別方法變數
    counts = 0

    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        super().__init__(factory, model, color, displacement)
        self.wheel = wheel  # 輪胎屬性
        # 改變類別方法變數
        Motorcycles.counts = Motorcycles.counts + 1

    # 解構式
    def __del__(self):
        # 改變類別方法變數
        Motorcycles.counts = Motorcycles.counts - 1

    # 類別方法
    @classmethod
    # 顯示類別方法變數
    def motocycles_counts(cls):
        return cls.counts

    # 屬性(Attribute)
    # 方法(Method)
    def fueltax(self):
        if self.displacement() <= 50:
            return 300
        elif self.displacement() <= 125:
            return 450
        elif self.displacement() <= 250:
            return 600
        elif self.displacement() <= 500:
            return 900
        elif self.displacement() <= 600:
            return 1200
        elif self.displacement() <= 1200:
            return 1800
        else:
            return 2010


class GasolineMotorcycles(Motorcycles):
    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        super().__init__(factory, "汽油機車" + model, color, displacement, wheel)


class ElectricMotorcycles(Motorcycles):
    # 建構式
    def __init__(self, factory, model, color, displacement, wheel):
        super().__init__(factory, "電能機車" + model, color, displacement, wheel)

    # 傳回燃料稅(0元)
    def fueltax(self):
        return 0

    # 傳回牌照稅(0元)
    def licensetax(self):
        return 0


# Cars基礎類別
class Cars(Vehicles):
    # 類別方法變數
    counts = 0

    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, model, color, displacement)
        self.seat = seat  # 座位屬性(可改)
        # 改變類別方法變數
        Cars.counts = Cars.counts + 1

    # 解構式
    def __del__(self):
        # 改變類別方法變數
        Cars.counts = Cars.counts - 1

    # 類別方法
    @classmethod
    # 顯示類別方法變數
    def cars_counts(cls):
        return cls.counts

    # 屬性(Attribute)
    # 方法(Method)


# 汽油車衍生類別
class GasolineCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "汽油汽車" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回燃料稅
    def fueltax(self):
        if self.displacement() <= 500:
            return 2160
        elif self.displacement() <= 600:
            return 2880
        elif self.displacement() <= 1200:
            return 4320
        elif self.displacement() <= 1800:
            return 4800
        elif self.displacement() <= 2400:
            return 6180
        elif self.displacement() <= 3000:
            return 7200
        elif self.displacement() <= 3600:
            return 8640
        elif self.displacement() <= 4200:
            return 9810
        elif self.displacement() <= 4800:
            return 11220
        else:
            return 12180


# 柴油車衍生類別
class DieselCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "柴油汽車" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回燃料稅
    def fueltax(self):
        if self.displacement() <= 1800:
            return 2880
        elif self.displacement() <= 2400:
            return 3708
        elif self.displacement() <= 3000:
            return 4320
        elif self.displacement() <= 3600:
            return 5184
        elif self.displacement() <= 4200:
            return 5886
        elif self.displacement() <= 4800:
            return 6732
        else:
            return 7308


# 電能車衍生類別
class ElectricCars(Cars):
    # 建構式
    def __init__(self, factory, model, color, seat, displacement):
        super().__init__(factory, "電能汽車" + model, color, seat, displacement)

    # 屬性(Attribute)
    # 傳回牌照稅(0元)
    def licensetax(self):
        return 0

    # 傳回燃料稅(0元)
    def fueltax(self):
        return 0


def tax(obj):
    print(obj.manufacture(), ":", obj.totaltax())


# 建構第1輛汽油車物件
print("==Test1==")
a = GasolineCars("CITROEN", "BX16TGS", "灰", 5, 1580)
# print(type(a))
print(a.manufacture())
a.info()
print(a.fueltax())
print(a.licensetax())
print(a.totaltax())
# 可以修改屬性
a.color = "綠"
a.seat = 2
print(a.manufacture())
a.info()
# 建構第2輛柴油車物件
print("==Test2==")
b = DieselCars("福特六和", "C346-9W", "白", 5, 1997)
# print(type(b))
print(b.manufacture())
b.info()
print(b.fueltax())
print(b.licensetax())
print(b.totaltax())
# 建構第3輛電能車物件
print("==Test3==")
c = ElectricCars("Tesla", "Model 3", "紅", 5, 346)
# print(type(c))
print(c.manufacture())
c.info()
print(c.fueltax())
print(c.licensetax())
print(c.totaltax())
print("==Test4==")
# 判斷a與b這兩輛汽車是否為相同類型
a.info()
b.info()
print(a == b)

# 建立第1台機車
print("==Test5==")
d = GasolineMotorcycles("光陽", "SJ25JF", "白黑銀", 124, Wheels(100, 10))
# print(type(d))
print(d.manufacture())
d.info()
print(d.fueltax())
print(d.licensetax())
print(d.totaltax())
# 建立第2台機車
print("==Test6==")
e = GasolineMotorcycles("功學社", "CT-50", "白紅", 49, Wheels(100, 10))
# print(type(e))
print(e.manufacture())
e.info()
print(e.fueltax())
print(e.licensetax())
print(e.totaltax())
# 建立第3台機車
print("==Test7==")
f = ElectricMotorcycles("睿能", "GHS6B2", "白", 8.58, Wheels(100, 10))
# print(type(f))
print(f.manufacture())
f.info()
print(f.fueltax())
print(f.licensetax())
print(f.totaltax())
# 建立第4台機車
print("==Test8==")
g = GasolineMotorcycles("光陽", "SK60AF", "深藍", 298, Wheels(100, 10))
# print(type(g))
print(g.manufacture())
g.info()
print(g.fueltax())
print(g.licensetax())
print(g.totaltax())
# 建立第5台機車
print("==Test9==")
h = ElectricMotorcycles("睿能", "GHS6B2", "紅", 8.58, Wheels(100, 10))
# print(type(h))
print(h.manufacture())
h.info()
print(h.fueltax())
print(h.licensetax())
print(h.totaltax())
print("==Test10==")
# 判斷f與h這兩台機車是否為相同類型
f.info()
h.info()
print(f == h)
print("==Test11==")
# 判斷d與e這兩台機車的輪台是否為相同類型
d.wheel.info()
e.wheel.info()
print(d.wheel.eq(e.wheel))
print(d.wheel == e.wheel)
print("==Test12==")
tax(a)
tax(b)
tax(c)
tax(d)
tax(e)
tax(f)
tax(g)
tax(h)
print("==Test13==")
# 查看總共新增了幾輛汽車
print(Cars.counts)
# 刪除a車
del a
print(Cars.counts)
# 刪除b車
del b
print(Cars.counts)
# 刪除c車
del c
print(Cars.counts)
print("==Test14==")
# 查看總共新增了幾台機車
print(Motorcycles.counts)
# 刪除d車
del d
print(Motorcycles.counts)
# 刪除e車
del e
print(Motorcycles.counts)
# 刪除f車
del f
print(Motorcycles.counts)
# 刪除g車
del g
print(Motorcycles.counts)
# 刪除h車
del h
print(Motorcycles.counts)

print("------------------------------------------------------------")  # 60個

import json

url = "https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json"
res = requests.get(url, verify=False)

print(res)
# 有兩種方法，下面兩行任選一種都可以
# data = json.loads(res.text) #方法1
data = res.json()  # 方法2
print(data)

# 因為有欄位名稱
# 只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
# 轉換'確定病例數'欄位內容為整數(以利後面加總)
df["確定病例數"] = df["確定病例數"].astype(int)

startdate = "2021/07/20"
# startdate=input("請輸日期(yyyy/mm/dd)")
# 只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(["確定病名", "縣市", "鄉鎮", "性別", "年齡層"], inplace=True, axis=1)
# 設定過濾條件(累積)
indexNames = df[df["個案研判日"] > startdate].index
# 刪除所有大於指定日期的個案
df.drop(indexNames, inplace=True)
# 計算累積確診人數
total = df.sum()["確定病例數"]
print("累積確診人數:", total)
# 設定過濾條件(今日)
indexNames = df[df["個案研判日"] != startdate].index
# 刪除所有不是指定日期的個案
df.drop(indexNames, inplace=True)
# 計算境外移入人數
imported = df[df["是否為境外移入"] == "是"].sum()["確定病例數"]
print("今日境外移入人數:", imported)
# 計算本土人數
domestic = df[df["是否為境外移入"] == "否"].sum()["確定病例數"]
print("今日本土人數:", domestic)
total = imported + domestic
print("今日總人數:", total)
# 若要查看有哪些欄位
print((df.keys()))
# 也可以透過df.info()查看
df.info()
# 也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

url = "https://www.dcard.tw/f/stock/p/237123381"
response = requests.get(url)
print(response.text)

url = "https://www.dcard.tw/f/stock/p/237123381"
res = requests.get(url)
print(res.text)

url = "http://jigsaw.w3.org/HTTP/connection.html"
response = requests.get(url)
# print(response.text)

# 在<HEAD></HEAD>區塊中取得包圍網頁標題的指定字串<TITLE></TITLE>所在的位置
# stripe()去除字串頭尾的'\n'(換行)、'\t'(跳格)、' '(空白)
datapos1 = response.text.find("<TITLE>")
datapos2 = response.text.find("</TITLE>")
data = response.text[datapos1 + 7 : datapos2]
data = data.strip()
print("網頁的<TITLE> :", data)
# 在<BODY></BODY>區塊中取得包圍內容標題的指定字串<H1></H1>所在的位置
datapos1 = response.text.find("<H1>")
datapos2 = response.text.find("</H1>")
data = response.text[datapos1 + 4 : datapos2]
# 將設定斜體的HTML語法<I></I>移除
data = data.replace("<I>", "")
data = data.replace("</I>", "")
data = data.strip()
print("<網頁的H1的資料(去掉<I>)> :", data)

datapos1 = response.text.find("<CODE>")
datapos2 = response.text.find("</CODE>")
data = response.text[datapos1 + 7 : datapos2]
data = data.strip()
print("網頁的<CODE> :", data)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/stock/p/237123381"
response = requests.get(url)
# 指定html.parser作為解析器
soup = BeautifulSoup(response.text, "html.parser")
# 把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
# 必須借助於Beautiful Shop套件
print(soup.prettify())

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/stock/p/237123381"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",  # 使用者代理
}

# response = requests.get(url="https://example.com", headers=headers)
response = requests.get(url, headers=headers)
# 指定html.parser作為解析器
soup = BeautifulSoup(response.text, "html.parser")
# 把排版後的html印出來
# print(soup.prettify())
a_tags = soup.find_all("h1")
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/stock/p/237123381"
res = requests.get(url)
# 指定html.parser作為解析器
soup = BeautifulSoup(res.text, "html.parser")
# 把排版後的html印出來
# print(soup.prettify())
a_tags = soup.find_all("h1")
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")
a_tags = soup.find_all("div", limit=1)
a_tag = a_tags[0]
cc = ""
for b in a_tag.contents:
    if str(b).find("gFINpq") >= 0:
        b = str(b).replace("\n", "").replace("\r", "")
        cc = cc + b
print(cc.strip())

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/stock/p/237123381"
res = requests.get(url)
# 指定html.parser作為解析器
soup = BeautifulSoup(res.text, "html.parser")
# 把排版後的html印出來
# print(soup.prettify())
a_tags = soup.find_all("h1")
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print()
a_tags = soup.find_all("div", limit=1)
a_tag = a_tags[0]
cc = ""
for b in a_tag.contents:
    if str(b).find("gFINpq") >= 0:
        b = str(b)
        cc = cc + b
cc = cc.strip()
data = ">>>>>原Po文章\n"
# 尋找前四筆，第一個是原Po文章，後三個則為熱門留言
for j in range(4):
    # 尋找最附近的<div class>有gFINpq
    datapos1 = cc.find("gFINpq")
    # 只保留這個字串以後的文字
    cc = cc[datapos1:]
    while True:
        # 尋找最附近的<span
        datapos1 = cc.find("<span")
        # 只保留<span以後的文字
        cc = cc[datapos1:]
        # 尋找最附近的>
        datapos1 = cc.find(">")
        # 尋找最附近的</span>
        datapos2 = cc.find("</span>")
        # 如果<span></span>中間出現了enUbOQ，表示這個步驟該結束了
        if cc[:datapos2].find("enUbOQ") >= 0:
            break
        # 如果<span></span>有資料，就合併在data字串裡
        if datapos1 + 1 < datapos2:
            # 但是<span></span>的資料，如果還有span就不行了
            if cc[datapos1 + 1 : datapos2].find("span") < 0:
                data = data + cc[datapos1 + 1 : datapos2] + "\n"
        # 只保留</span>之後的文字
        cc = cc[datapos2 + 7 :]
    # 後三個是熱門留言
    if j < 3:
        data = data + "\n*******熱門留言" + str(j + 1) + ":\n"
print(data)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import csv

# from io import StringIO

county = "屏東縣"
url = "https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=keykeykey&sort=ImportDate%20desc&format=csv"
# 方法1:下載檔案後儲存，再開啟檔案讀出
# res = requests.get(url)
# open('data.csv','wb').write(res.content)
# df=pd.read_csv('data.csv')
# 方法2:直接讀取網站的檔案
df = pd.read_csv(url)
# 查看有那些欄位
df.info()
# 只保留SiteName、County、AQI、Status四個欄位
df.drop(
    [
        "SiteId",
        "Longitude",
        "Latitude",
        "PublishTime",
        "SO2_AVG",
        "Pollutant",
        "SO2",
        "CO",
        "NO",
        "CO_8hr",
        "O3",
        "O3_8hr",
        "PM10",
        "PM10_AVG",
        "PM2.5",
        "PM2.5_AVG",
        "NO2",
        "NOx",
        "WindSpeed",
        "WindDirec",
    ],
    inplace=True,
    axis=1,
)
# 設定過濾條件
indexNames = df[df["County"] != county].index
# 刪除所有不是臺北市的偵測站
df.drop(indexNames, inplace=True)
# 重設索引值
df = df.reset_index(drop=True)
# 列出該縣市所有偵測站狀態
print(county, "空氣品質狀態")
for i in range(len(df)):
    print(df.loc[i, "SiteName"], "(", df.loc[i, "Status"], ")")
indexNames = df[df["Status"] == "良好"].index
df.drop(indexNames, inplace=True)
# 重設索引值
df = df.reset_index(drop=True)
# 列出該縣市所有為達良好之偵測站
print()
print(county, "空氣品質未達良好之偵測站")
for i in range(len(df)):
    print(df.loc[i, "SiteName"], "(", df.loc[i, "Status"], ")")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import csv

# from io import StringIO

url = "https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv"
# 方法1:下載檔案後儲存，再開啟檔案讀出
# res = requests.get(url)
# open('data.csv','wb').write(res.content)
# df=pd.read_csv('data.csv')
# 方法2:直接讀取網站的檔案
df = pd.read_csv(url)
# 查看有那些欄位
df.info()
# 只保留確診、死亡、送驗、排除四個欄位
df.drop(["昨日確診", "昨日排除", "昨日送驗"], inplace=True, axis=1)
print(df)
totaldeath = df.loc[0, "死亡"]
print("累積死亡人數", totaldeath)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

try:
    # 嘗試打開一個不存在的檔案
    with open("non_existent_file.txt", "r") as f:
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    # 如果文件不存在, 捕獲異常
    print("The file was not found")
except IOError:
    # 處理 I/O 錯誤, 例如:讀取錯誤
    print("An I/O error occurred")

print("------------------------------------------------------------")  # 60個

filename = "data15_4.txt"
try:
    with open(filename) as f:  # 預設mode=r開啟檔案
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    print(f"找不到 {filename} 檔案")
else:
    print(data)  # 輸出變數data


print("------------------------------------------------------------")  # 60個


set99 = set()
for i in range(2, 9 + 1):
    set99.add(i)

print(type(set99))
print(set99)


print("------------------------------------------------------------")  # 60個

pName = "D:/pcYah"
if os.path.isdir(pName):  # 檢查資料夾路徑是否存在
    print("%s 資料夾路徑存在" % pName)
else:
    print("%s 資料夾路徑不存在" % pName)

fName = "D:/Windows/win.ini"
if os.path.isfile(fName):  # 檢查檔案路徑是否存在
    print("%s 檔案路徑存在" % fName)
else:
    print("%s 檔案路徑不存在" % fName)

"""

isdir  isfile

if os.path.exists(pName):        # 檢查資料夾路徑是否存在
if os.path.exists(fName):        # 檢查檔案路徑是否存在


"""


# try-catch-finally
n1 = 8
n2 = 0
try:
    d = n1 / n2
    print("%d / %d = %d" % (n1, n2, d))
except Exception as e:
    print("錯誤類型 :", end=" ")
    print(e)
finally:
    print("執行 finally: 敘述\n")


print("------------------------------------------------------------")  # 60個


lst = [0 for x in range(4)]
try:
    lst[3] = 33
    print("lst[3] =", lst[3])
    lst[8] = 88
    print("lst[8] =", lst[8])
except ZeroDivisionError:
    print("錯誤類型 : 除數為零")
except IndexError:
    print("錯誤類型 : 串列註標超出範圍")
except MemoryErroe:
    print("錯誤類型 : 超出記憶體空間")
except Exception as e:
    print("錯誤類型 :", e)

fName = "score.txt"
if os.path.isfile(fName):
    f = open(fName, "r")
    print("讀1行")
    str1 = f.readline()
    print(str1)
    print("讀4行")
    str2 = f.readline(4)
    print(str2)
    print("剩下的讀完")
    print(f.read())
    f.close()
else:
    print(None)


print("------------------------------------------------------------")  # 60個

# ord(x) 可以將參數x所代表的Unicode字元，轉換為對應編碼數字
A = ord("A")
B = ord("B")
C = ord("C")

print(A)
print(B)
print(C)

# chr(x) 可以將參數x轉換為所代表的Unicode字元
AA = chr(A)
BB = chr(B)
CC = chr(C)

print(AA)
print(BB)
print(CC)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 量測時間

# from time import clock # 改由 perf_counter()或process_time()替代
from time import perf_counter

timestart = perf_counter()
for i in range(0, 1000):
    for j in range(0, 1000):
        n = i * j
timeend = perf_counter()
print("執行一百萬次整數運算的時間：" + str(timeend - timestart) + " 秒")

timestart = perf_counter()
for i in range(0, 1000):
    for j in range(0, 1000):
        n = float(i) * float(j)
timeend = perf_counter()
print("執行一百萬次浮點數運算的時間：" + str(timeend - timestart) + " 秒")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import time as t

week = ["一", "二", "三", "四", "五", "六", "日"]
dst = ["無日光節約時間", "有日光節約時間"]
time1 = t.localtime()
show = "現在時刻：中華民國 " + str(int(time1.tm_year) - 1911) + " 年 "
show += str(time1.tm_mon) + " 月 " + str(time1.tm_mday) + " 日 "
show += str(time1.tm_hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第 " + str(time1.tm_yday) + " 天，此地" + dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

import time as t

timestart = t.perf_counter()
for i in range(0, 1000):
    for j in range(0, 1000):
        n = i * j
timeend = t.perf_counter()
print("執行一百萬次整數運算的時間：" + str(timeend - timestart) + " 秒")

print("------------------------------------------------------------")  # 60個

date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

print("------------------------------------------------------------")  # 60個

import time as t

time1 = t.localtime()
show = "今天是今年的第 " + str(time1.tm_yday) + " 天，屬於"
if time1.tm_yday < 184:
    show += "上半年。"
else:
    show += "下半年。"
print(show)

print("------------------------------------------------------------")  # 60個

"""
import time as t

timestart = t.perf_counter() ()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.perf_counter() ()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")
"""
print("------------------------------------------------------------")  # 60個

time1 = "10:23:41"
time1 = time1.replace(":", " 點 ", 1)
time1 = time1.replace(":", " 分 ", 1)
time1 += " 秒"
print(time1)

print("------------------------------------------------------------")  # 60個

list1 = random.sample(range(1, 50), 7)
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

import time as t

time1 = t.localtime()
show = "現在時刻："
if time1.tm_hour < 12:
    show += "上午 "
    hour = time1.tm_hour
else:
    show += "下午 "
    hour = time1.tm_hour - 12
show += str(hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒"
print(show)

print("------------------------------------------------------------")  # 60個

dict1 = {"A": "內向穩重", "B": "外向樂觀", "O": "堅強自信", "AB": "聰明自然"}
name = "O"
blood = dict1.get(name)
if blood == None:
    print("沒有「" + name + "」血型！")
else:
    print(name + " 血型的個性為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

person = 7
apple = 52
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

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


def disp_data():  # 顯示串列的自訂程序
    for item in datas:
        print(item, end=" ")
    print()


# 主程式
datas = [3, 5, 2, 1]
print("排序前：", end=" ")
disp_data()  # 顯示排序前串列
n = len(datas) - 1  # 串列長度-1

for i in range(0, n):
    for j in range(0, n - i):
        if datas[j] > datas[j + 1]:  # 由小到大排序
            datas[j], datas[j + 1] = datas[j + 1], datas[j]  # 兩數互換

print("排序後：", end=" ")
disp_data()  # 顯示排序後串列

print("------------------------------------------------------------")  # 60個


def disp_data():  # 顯示串列的自訂程序
    for item in datas:
        print(item, end=" ")
    print()


# 主程式
datas = [3, 5, 2, 1]
print("排序前：", end=" ")
disp_data()  # 顯示排序前串列
n = len(datas) - 1  # 串列長度-1

for i in range(0, n):
    for j in range(0, n - i):
        print("i=%d j=%d" % (i, j))
        if datas[j] > datas[j + 1]:  # 由大到小排序
            print("%d,%d 互換後" % (datas[j], datas[j + 1]), end="：")
            datas[j], datas[j + 1] = datas[j + 1], datas[j]  # 兩數互換
        print(datas)

print("排序後：", end=" ")
disp_data()  # 顯示排序後串列

print("------------------------------------------------------------")  # 60個

dict1 = {"春季": "暖和", "夏季": "炎熱", "秋季": "涼爽", "冬季": "寒冷"}
name = "春季"
feeling = dict1.get(name)
if feeling == None:
    print("沒有「" + name + "」季節！")
else:
    print(name + "的天氣為 " + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"電視": 15000, "冰箱": 23000, "冷氣": 28000}
name = "冰箱"
if name in dict1:
    print(name + "的價格為 " + str(dict1[name]))
else:
    price = input("輸入電器價格：")
    dict1[name] = price
    print("字典內容：" + str(dict1))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座": "活潑善變", "雙魚座": "迷人保守", "白羊座": "天生勇者", "金牛座": "熱情敏感"}
item1 = dict1.items()
for name, nature in item1:
    print("%s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座": "活潑善變", "雙魚座": "迷人保守", "白羊座": "天生勇者", "金牛座": "熱情敏感"}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的性格特癥為 %s" % (listkey[i], listvalue[i]))

print("------------------------------------------------------------")  # 60個

ret = divmod(10000, 350)
print("可維持生活 " + str(ret[0]) + " 天")
print("生活費剩餘 " + str(ret[1]) + " 元")

print("------------------------------------------------------------")  # 60個

listname = ["鍾明達", "鄭廣月", "何美麗"]
list1 = [34210, 23600, 145000, 54300]
list2 = [9000, 23900, 83400, 132000]
list3 = [186500, 127800, 100000, 45000]
list4 = [78900, 125000, 90000, 8000]
print("姓名       第一季  第二季  第三季   第四季")
for i in range(0, 3):
    print(
        listname[i].ljust(5),
        str(list1[i]).rjust(7),
        str(list2[i]).rjust(7),
        str(list3[i]).rjust(7),
        str(list4[i]).rjust(7),
    )

print("------------------------------------------------------------")  # 60個

list1 = random.sample(range(0, 10), 4)
list1.sort()
print("本期四星彩中獎號碼為：", end="")
for i in range(0, 4):
    if i == 3:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=", ")

print("------------------------------------------------------------")  # 60個


def disp_data():  # 顯示串列的自訂程序
    for item in datas:
        print(item, end=" ")
    print()


# 主程式
datas = datas = [2, 3, 5, 7, 1]
print("排序前：", end=" ")
disp_data()  # 顯示排序前串列
n = len(datas) - 1  # 串列長度-1

for i in range(0, n):
    for j in range(0, n - i):
        if datas[j] < datas[j + 1]:  # 由大到小排序
            datas[j], datas[j + 1] = datas[j + 1], datas[j]  # 兩數互換

print("排序後：", end=" ")
disp_data()  # 顯示排序後串列

print("------------------------------------------------------------")  # 60個

monthname = {
    1: "JAN",
    2: "FEB",
    3: "MAR",
    4: "APR",
    5: "MAY",
    6: "JUN",
    7: "JUL",
    8: "AUG",
    9: "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC",
}
m = 3
print("{}月份的英文簡寫為 {}：".format(m, monthname[m]))

print("------------------------------------------------------------")  # 60個

cnum = {0: "零", 1: "壹", 2: "貮", 3: "參", 4: "肆", 5: "伍", 6: "陸", 7: "柒", 8: "捌", 9: "玖"}
num = "1234"
for n in num:
    print(cnum[int(n)], end="")

print("------------------------------------------------------------")  # 60個

dict1 = {"台北市": 6, "新北市": 2, "桃園市": 5, "台中市": 8, "台南市": 3, "高雄市": 9}
name = "新北市"
PM25 = dict1.get(name)
if PM25 == None:
    print("六都中沒有「" + name + "」城市！")
else:
    print(name + " 今天的 PM2.5 值為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"鼠": "親切和藹", "牛": "保守努力", "虎": "熱情大膽", "兔": "溫柔仁慈"}
for name, nature in dict1.items():
    print("生肖屬 %s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

rate = {"USD": 28.02, "JPY": 0.2513, "CNY": 4.24}
TWD = float("123.456")
print(
    "台幣{:.2f}元等於美金{:.2f}元, 日幣{:.2f}元, 人民幣{:.2f}元".format(
        TWD, TWD / rate["USD"], TWD / rate["JPY"], TWD / rate["CNY"]
    )
)

print("------------------------------------------------------------")  # 60個

print("產生N個 從 MIN 到 MAX 不重複的整數(包含頭尾)")
N = 7
MIN = 1
MAX = 50
list1 = random.sample(range(MIN, MAX), N)
print(type(list1))
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)

print("------------------------------------------------------------")  # 60個

N = 10
MIN = 80
MAX = 100
scores = random.sample(range(MIN, MAX), N)
print("原成績：", scores)

print("人數：%d" % len(scores))
print("最高分為：%d" % max(scores))
print("最低分為：%d" % min(scores))
print("總分為：%d" % sum(scores))
print("平均為：%6.2f" % (sum(scores) / N))

scores2 = sorted(scores, reverse=True)  # 由大到小排序
print("成績由大到小排序：", scores2)

scores2 = sorted(scores, reverse=False)  # 由小到大排序
print("成績由小到大排序：", scores2)

print("------------------------------------------------------------")  # 60個

N = 10
MIN = 80
MAX = 100
scores = random.sample(range(MIN, MAX), N)


def disp_scores():  # 顯示串列的自訂程序
    for score in scores:
        print(score, end=" ")
    print()


print("排序前：", end=" ")
disp_scores()  # 顯示排序前串列

n = len(scores) - 1  # 串列長度-1

for i in range(0, n):
    for j in range(0, n - i):
        if scores[j] < scores[j + 1]:  # 由大到小排序
            scores[j], scores[j + 1] = scores[j + 1], scores[j]  # 兩數互換

print("成績由大到小排序：", end="")
disp_scores()  # 顯示排序後串列

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]

print("動物有：", animals)

animal = "豬"
n = animals.count(animal)
if n > 0:  # 串列元素存在
    p = animals.index(animal)
    print("%s 在串列中的第 %d 項" % (animal, p + 1))
    animals.remove(animal)
else:
    print(animal, "不在串列中!, 加入此動物")
    animals.append(animal)

print("動物有：", animals)

print("------------------------------------------------------------")  # 60個

dict1 = {"金牌": 26, "銀牌": 34, "銅牌": 30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))


print("------------------------------------------------------------")  # 60個

names = ["David", "Lily", "Chiou", "Bear", "Shantel", "Cynthia"]

n = len(names) - 1  # 串列長度-1
for i in range(0, n):
    for j in range(0, n - i):
        if names[j] > names[j + 1]:  # 由小到大排序
            names[j], names[j + 1] = names[j + 1], names[j]  # 互換
print("------------------------------------------------------------")  # 60個

print("姓名    成績")
print("%-4s  %3d" % (name1, score1))
print("%-4s  %3d" % (name2, score2))

print("------------------------------------------------------------")  # 60個

# 過度擬合 (overfitting)

# 拉格朗日 (Lagrange) 插值法

x = np.linspace(0, 1, 200)
y = -((x - 1) ** 2) + 1
plt.plot(x, y, "lime")

X = np.linspace(0, 1, 20)
Y = -((X - 1) ** 2) + 1 + 0.08 * np.random.randn(20)
plt.scatter(X, Y, c="b", s=50)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x), "r")

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍

show()

print("------------------------------------------------------------")  # 60個

"""
#【秘技】分列 X, Y 的變成點座標

等一下我們會大量的把資料變換形式, 現在我們先熱身。在畫圖時常常用到把 x, y 座標分列。現在我們要合成點要怎麼做呢? 也就是說
X1 <-- [1,2,3,4]
Y1 <-- [5,6,7,8]
希望變成
[[1,5], [2,6], [3,7], [4,8]]
"""

X1 = np.array([1, 2, 3, 4])
Y1 = np.array([5, 6, 7, 8])

# NumPy 有個神奇的方式會幫我們做!

ccc = np.c_[X1, Y1]
print(ccc)

"""
【重要插播】meshgrid 用法

為了用 contourf (填充型的等高線) 呈現我們成果, 我們要介紹一個初學有點難理解、meshgrid 的概念。

meshgrid 是產生格點的方式, 通常是我們要畫 3D 曲面啦、或是等高線的時候要先為我們在 xy 平面上「佈點」, 然後算出每點的高度 Z。

我們要做的是給定 x 方向座標, y 方向座標, 然後就產生格點, 如圖示。
"""


# 於是我們再度用我們的 X1, Y1 示範。

X1 = np.array([1, 2, 3, 4])

Y1 = np.array([5, 6, 7, 8])

# 因為 matplotlib 很愛 x, y-座標分開, 經 meshgrid 後也是分開的! 所以我們用 Xm 和 Ym 來接。

Xm, Ym = np.meshgrid(X1, Y1)

# 看一下內容...

print(Xm)
print(Ym)

# 等等, 這什麼啊? 原來 meshgrid 存網格的 x 座標是一列一列存的。
# 同理我們可以理解 Ym 的內容為什麼是這樣了...

print("------------------------------------------------------------")  # 60個

# 01 numpy 的 filter

egg = np.array([3, -5, 10, 23, -5, 11])
idx = egg >= 0
print(idx)
# array([ True, False,  True,  True, False,  True])

print(egg[idx])
# array([ 3, 10, 23, 11])

print(egg[egg >= 0])
# array([ 3, 10, 23, 11])

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.scatter(x[y > 0], y[y > 0], c="r")
show()

# 02 Overfitting
Px = np.random.rand(6)
Py = np.random.rand(6)
plt.scatter(Px, Py, c="r", s=50)
show()

x = np.linspace(0, 1, 1000)
y = 0.5 * np.sin(x) + 0.5
plt.scatter(Px, Py, c="r", s=50)
plt.plot(x, y)
show()


def myplot(n=1):
    y = 0.5 * np.sin(n * x) + 0.5
    plt.scatter(Px, Py, c="r", s=50)
    plt.plot(x, y)


myplot(3)

show()

print("------------------------------------------------------------")  # 60個


# lambda: 臨時要使用的函數
currency = 32.1357851  # 1美元 = 32.13台幣    台灣銀行 現金賣出價

price = [100, 500, 1000]  # 美元

ll = list(map(lambda x: currency * x, price))
print("換算成台幣 :", ll)

usb2twd = lambda x: currency * x

print(usb2twd(1000))


# print(f"1 美元合台幣 {c:.2f} 元。")
# print(f"1 美元合台幣 {c:10.2f} 元。")

print("------------------------------------------------------------")  # 60個


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def show(self):
        print(self.SUITS[self.suit] + self.RANKS[self.rank])


card01 = Card(2, 3)
card01.show()

print("------------------------------------------------------------")  # 60個

"""
import matplotlib as mpl
import matplotlib.font_manager as fm

for f in mpl.font_manager.fontManager.ttflist:
    print(f.name)

#[f.name for f in mpl.font_manager.fontManager.ttflist]

print('matplotlib 真的「看到的」字型')
for f in fm.fontManager.ttflist:
    print(f.name)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Create a deck of cards
deck = [x for x in range(0, 52)]

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Shuffle the cards
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)

print("------------------------------------------------------------")  # 60個

from random import randint

# Open file for writing data
outfile = open("tmp_Numbers.txt", "w")
for i in range(10):
    outfile.write(str(randint(0, 9)) + " ")
outfile.close()  # Close the file

# Open file for reading data
infile = open("tmp_Numbers.txt", "r")
s = infile.read()
numbers = [eval(x) for x in s.split()]
for number in numbers:
    print(number, end=" ")
infile.close()  # Close the file

print()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#data analysis

NUMBER_OF_ELEMENTS = 5 # For simplicity, use 5 instead of 100
numbers = [] # Create an empty list
sum = 0

for i in range(NUMBER_OF_ELEMENTS): 
    value = eval(input("Enter a new number: "))
    numbers.append(value)
    sum += value
    
average = sum / NUMBER_OF_ELEMENTS

count = 0 # The number of elements above average
for i in range(NUMBER_OF_ELEMENTS): 
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Number of elements above the average is", count)
"""
print("------------------------------------------------------------")  # 60個

filename = "tmp_Presidents.txt"

# 製作一個檔案
# Open file for output
outfile = open(filename, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close()  # Close the output file

print("------------------------------------------------------------")  # 60個

filename = "tmp_Presidents.txt"

fp = open(filename, "r")
zops = fp.readlines()
fp.close()

i = 1
print("檔案內容")
for zen in zops:
    print("第 {} 行 : {}".format(i, zen), end="")
    i += 1

print()

print("------------------------------------------------------------")  # 60個

filename = "tmp_Presidents.txt"


def main():
    # Open file for input
    infile = open(filename, "r")
    print("(1) Using read(): ")
    print(infile.read())
    infile.close()  # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(2) Using read(number): ")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(repr(s2))
    infile.close()  # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    infile.close()  # Close the input file

    # Open file for input
    infile = open(filename, "r")
    print("\n(4) Using readlines(): ")
    print(infile.readlines())
    infile.close()  # Close the input file


main()  # Call the main function

print("------------------------------------------------------------")  # 60個

print("各種讀取檔案的方法")

filename = "tmp_Presidents.txt"

# Open file for input
infile = open(filename, "r")
print("(1) Using read(): ")
print(infile.read())
infile.close()  # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(2) Using read(number): ")
s1 = infile.read(4)
print(s1)
s2 = infile.read(10)
print(repr(s2))
infile.close()  # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(3) Using readline(): ")
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))
infile.close()  # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(4) Using readlines(): ")
print(infile.readlines())
infile.close()  # Close the input file

print("------------------------------------------------------------")  # 60個

currentTime = time.time()  # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

print(totalSeconds)

print("------------------------------------------------------------")  # 60個

""" 久
import urllib.request
input = urllib.request.urlopen('http://www.yahoo.com/index.html')
print(input.read())
"""

print("------------------------------------------------------------")  # 60個

# Social Security Number

import re

regex = "\d{3}-\d{2}-\d{4}"
# ssn = input("Enter SSN: ")
ssn = "123-45-6789"
match1 = re.match(regex, ssn)

if match1 != None:
    print(ssn, " is a valid SSN")
    print("start position of the matched text is " + str(match1.start()))
    print("start and end position of the matched text is " + str(match1.span()))
else:
    print(ssn, " is not a valid SSN")

print("------------------------------------------------------------")  # 60個

import re

regex = "\d{3}-\d{2}-\d{4}"
# text = input("Enter a text: ")
text = "123-45-6789"

match1 = re.search(regex, text)

if match1 != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + str(match1.start()))
    print("start and end position of the matched text is " + str(match1.span()))
else:
    print(text, " does not contain a SSN")

print("------------------------------------------------------------")  # 60個

s = "1 2 3 4 5"
items = s.split()  # Extract items from the string
lst = [eval(x) for x in items]  # Convert items to numbers

print(lst)

print("------------------------------------------------------------")  # 60個

students = [("John", "Smith", 96), ("Susan", "King", 76), ("Kim", "Yao", 99)]
students.sort(key=lambda e: (e[1]))

print(students)
print(sorted(students, key=lambda t: (t[2]), reverse=True))

print("------------------------------------------------------------")  # 60個

# 河內塔


# The function for finding the solution to move n disks
#   from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    if n == 1:  # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)


print("盤子數 5")
n = 5

# Find the solution recursively
print("The moves are:")
moveDisks(n, "A", "B", "C")

print("------------------------------------------------------------")  # 60個


# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
    hex = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    return hex


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord("0"))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord("A"))


decimalValue = 170

print("The hex number for decimal", decimalValue, "is", decimalToHex(decimalValue))

print("------------------------------------------------------------")  # 60個


print("          九九乘法表")
# Display the number title
print("  |", end="")
for j in range(1, 10):
    print("  ", j, end="")
print()  # Jump to the new line
print("-----------------------------------------")

# Display table body
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        # Display the product and align properly
        print(format(i * j, "4d"), end="")
    print()  # Jump to the new line


print("------------------------------------------------------------")  # 60個


# Compute the distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5


def nearestPoints(points):
    # p1 and p2 are the indices in the points list
    p1, p2 = 0, 1  # Initial two points

    shortestDistance = distance(
        points[p1][0], points[p1][1], points[p2][0], points[p2][1]
    )  # Initialize shortestDistance

    # Compute distance for every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(
                points[i][0], points[i][1], points[j][0], points[j][1]
            )  # Find distance

            if shortestDistance > d:
                p1, p2 = i, j  # Update p1, p2
                shortestDistance = d  # New shortestDistance

    return p1, p2


print("找出多點中最近的兩點")

# Create a list to store points
points = []

point = 2 * [0]
point[0], point[1] = 0, 0
points.append(point)

point = 2 * [0]
point[0], point[1] = 5, 0
points.append(point)

point = 2 * [0]
point[0], point[1] = 5, 5
points.append(point)

point = 2 * [0]
point[0], point[1] = 3, 1
points.append(point)

# p1 and p2 are the indices in the points list
p1, p2 = nearestPoints(points)

# Display result
print(
    "The closest two points are ("
    + str(points[p1][0])
    + ", "
    + str(points[p1][1])
    + ") and ("
    + str(points[p2][0])
    + ", "
    + str(points[p2][1])
    + ")"
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from io import BytesIO
from lxml import etree
import base64


df = pd.DataFrame(
    {
        "id": ["1", "2", "3", "4", "5"],  # 構造數據
        "math": [90, 89, 99, 78, 63],
        "english": [89, 94, 80, 81, 94],
    }
)


x = np.linspace(0, 8, 100)
y = np.sin(x)
plt.plot(x, y)

# df資料存成html
buffer = BytesIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()

imb = base64.b64encode(plot_data)  # 生成網頁內容
ims = imb.decode()
imd = "data:image/png;base64," + ims
data_im = """<h1>Figure</h1>  """ + """<img src="%s">""" % imd
data_des = """<h1>Describe</h1>""" + df.describe().T.to_html()
root = "<title>Dataset</title>"
root = root + data_des + data_im

html = etree.HTML(root)
tree = etree.ElementTree(html)
tree.write("tmp_導出圖表.html")

show()

print("------------------------------------------------------------")  # 60個

root_dir = os.path.abspath(".")
gunfire_path = os.path.join(root_dir, "gunfire.wav")
filename = os.path.join(root_dir, "tone.wav")
print(filename)

"""
# 新建資料夾用於放置影像
if not os.path.isdir('trainer'):
    os.mkdir('trainer')
os.chdir('trainer')
"""

root_dir = os.path.abspath(".")
filename = os.path.join(root_dir, "tone.wav")
print(filename)

print("------------------------------------------------------------")  # 60個

print("建立20組資料")
USERS = [(i, f"account_{i}", f"nickname_{i}") for i in range(20)]

print(type(USERS))
print(len(USERS))
print(USERS)
for _ in USERS:
    print(_)

print("------------------------------------------------------------")  # 60個

print("統計一串英文字串個字母出現的頻率")

from collections import defaultdict

text = "this is a lion-mouse"

frequency = defaultdict(int)
for symbol in text:
    frequency[symbol] += 1
print(frequency)

heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
print(heap)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
from pathlib import Path

# Version
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

VERSION_FILE = BASE_DIR.joinpath('data_store', 'cccc.py')
print(VERSION_FILE)

#執行一個檔案
with open(VERSION_FILE) as fp:
    exec(fp.read())

from pathlib import Path
from setuptools import setup, find_packages

import dicom

BASE_DIR = Path(__file__).parent
with open(BASE_DIR / "pydicom" / "_version.py") as f:
    exec(f.read())

with open(BASE_DIR / 'README.md') as f:
    long_description = f.read()

def data_files_inventory():
    root = BASE_DIR / "pydicom" / "data"
    files = [
        f.relative_to(BASE_DIR / "pydicom")
        for f in root.glob("**/*")
        if f.is_file() and f.suffix != ".pyc"
    ]
    return [os.fspath(f) for f in files]
"""

print("------------------------------------------------------------")  # 60個

from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data"
print(data_path)

print("------------------------------------------------------------")  # 60個

import pydicom.data
from pydicom.data import get_testdata_file

fname = "693_UNCI.dcm"
fpath = get_testdata_file(fname)
print(fpath)

print("done")

print("------------------------------------------------------------")  # 60個

# UTC时间

import datetime

# 创建一个时间戳（以秒为单位）
timestamp = 22
# 带UTC时区时间
dt_with_timezone = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
print("带UTC时区时间:", dt_with_timezone)
# 不带UTC时区时间
dt_without_timezone = datetime.datetime.fromtimestamp(timestamp)
print("不带UTC时区时间", dt_without_timezone)

# 时间戳
print(time.time())
print(time.localtime())  # 获取到当前时间的元组
print(time.mktime(time.localtime()))
# 一周的第几天(周一是0,0-6)、一年的第几天(从1开始，1-366)、夏时令(是夏时令1，不是0，未知-1)。

# 字符串和时间转换

# 字符串和时间转换
# 利用time模块的strftime()函数可以将时间戳转换成系统时间。
time_str = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime())
print(time_str)

# 可以用strptime函数将日期字符串转换为datetime数据类型，
import datetime

print(datetime.datetime.strptime("2022-01-15", "%Y-%m-%d"))

# 可以用Pandas的to_datetime()函数将日期字符串转换为datetime数据类型。
# to_datetime()函数转化后的时间是精准到时分秒精度的

print(pd.to_datetime("2022/01/15"))

# 时间差

# 3. 时间运算--时间差
# 利用datetime将时间类型数据进行转换，然后利用减法运算计算时间的不同之处
# 默认输出结果转换为用（“天”，“秒”）表达
import datetime

delta = datetime.datetime(2022, 1, 16) - datetime.datetime(2021, 1, 1, 9, 15)
print(delta)
print(delta.days)
print(delta.seconds)

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4, 1, 2, 3, 4, 5]).reshape(3, 3)
y = np.arange(9).reshape(3, 3)
print(x)
print(y)
print(x @ y)  # 不知道這是什麼運算

# 使用NumPy進行點積運算 ??

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 1], [10, 25]])
b = np.array([16, 250])
print(np.linalg.solve(a, b))

print("------------------------------------------------------------")  # 60個

print("數字對應 0~9 對應到 9~0")
old = np.array([3, 8, 3, 4, 2, 1, 4, 1, 2, 2])
print(old)

# 數字對應
new = np.choose(old, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]).astype(np.int64)

print(new)


print("------------------------------------------------------------")  # 60個

# 05_08_regularization
# L1、L2 regularization的計算與強度比較

# 權重
W = np.array([-1, 5, 3, -9]).reshape(2, 2)
print(W)

# L1

Lambda = 0.5
L1 = Lambda * np.sum(np.abs(W))
print(L1)

# L2

L2 = Lambda * np.sum(W**2)
print(L2)

# 58.0

print("結論：L2 強度較大")


print("------------------------------------------------------------")  # 60個


# 利用可能なカラーマップを取得
cmaps = plt.colormaps()
cmaps.sort()

# データの生成
xs = np.arange(1, 10)
ys = np.arange(1, 10).reshape(9, 1)
m = xs * ys
df = pd.DataFrame(m)


# テンプレートの読み込み
def load_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# テンプレートを読み込む
header_template = load_template("templates/header_template.txt")
section_template = load_template("templates/section_template.txt")

# README.mdを作成
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(header_template)

    for cmap in cmaps:
        # ヒートマップを生成し、画像として保存
        plt.figure(figsize=(5, 3))
        ax = sns.heatmap(df, cmap=cmap)
        ax.tick_params(axis="both", which="both", length=0)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlabel("")
        ax.set_ylabel("")
        plt.tight_layout(pad=0.1)
        plt.savefig(f"images/{cmap}.png", transparent=True)
        plt.close()

        # READMEにセクションを追加
        section_content = section_template.format(cmap_name=cmap)
        readme.write(section_content)

print("------------------------------------------------------------")  # 60個


print("map 的用法")


def pick(x):
    fruits = ["Apple", "Banana", "Orange", "Tomato", "Pine Apple", "Berry"]
    return fruits[x]


alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)


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


print("List的用法")
list1 = []
list1.append(123)
list1.append(456)
list1.append(234)
list1.append(321)
list1.append(101)
# list1.pop()

print("共輸入 %d 個數" % len(list1))
print("最大：%d" % max(list1))
print("最小：%d" % min(list1))
print("總和：%d" % sum(list1))
print("由大到小排序為：{}".format(sorted(list1, reverse=True)))


"""
money = int(input("請輸入購物金額："))
if(money >= 10000):
    if(money >= 100000):
        print(money * 0.8, end=" 元\n")  #八折
    elif(money >= 50000):
        print(money * 0.85, end=" 元\n")  #八五折
    elif(money >= 30000):
        print(money * 0.9, end=" 元\n")  #九折
    else:
        print(money * 0.95, end=" 元\n")  #九五折
else:
    print(money, end=" 元\n")  #未打折
    
    
    
    
n = int(input("請輸入大樓的樓層數："))
print("本大樓具有的樓層為：")
if(n > 3):
    n += 1
for i in range(1, n+1):
    if(i==4):
        continue
    print(i, end=" ")
print()
"""

print("------------------------------------------------------------")  # 60個

# Classes and Objects


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"


# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Print the attributes of the instance
print("my_dog name:", my_dog.name)
print("my_dog age:", my_dog.age)

# Call the bark method of the instance
bark_result = my_dog.bark()
print("bark_result:", bark_result)

print("------------------------------------------------------------")  # 60個

from threading import Thread


# 繼承Thread類創建自定義的線程類
class DownloadHanlder(Thread):
    def __init__(self, data):
        print(data)
        super().__init__()
        self.data = data

    def run(self):
        print("A")
        time.sleep(1000)


for _ in range(10):
    DownloadHanlder(_).start()

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
