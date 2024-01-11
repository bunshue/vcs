"""
範例來的混合資料 2


"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
for animal in animals:
    print(animal)

print("------------------------------------------------------------")  # 60個

animals = "Python程式設計"
print(animals[0])
print(animals[1])
print(animals[-1])
print(animals[-2])

print("------------------------------------------------------------")  # 60個

animals = "Python"
print(animals.islower())
print("2023".isdigit())

print("------------------------------------------------------------")  # 60個

# 字串函數
animals = 'Hello World!'
print("animals = ", animals)
s = len(animals)
print("len(animals) = ", str(s))
s = max(animals)
print("max(animals) = ", s)
s = min(animals)
print("min(animals) = ", s)
str2 = 'Python程式設計'
print("str2 = ", str2)
s = len(str2)
print("len(str2) = ", str(s))
s = max(str2)
print("max(str2) = ", s)
s = min(str2)
print("min(str2) = ", s)

sys.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-1-3c.py

animals = 'welcome to python'
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-1-3d.py

animals = 'welcome to python'
print("animals = ", animals)
b = animals.endswith('thon')
print("animals.endswith('thon') = ", b)
b = animals.startswith('hello')
print("animals.startswith('hello') = ", b)
b = animals.count('o')
print("animals.count('o') = ", b)
b = animals.find('come')
print("animals.find('come') = ", b)
b = animals.find('become')
print("animals.find('become') = ", b)
b = animals.find('o')
print("animals.find('o') = ", b)
b = animals.find('e')
print("animals.find('e') = ", b)
b = animals.rfind('o')
print("animals.rfind('o') = ", b)
b = animals.rfind('e')
print("animals.rfind('e') = ", b)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-1-3e.py

animals = 'welcome to python'
print("animals = ", animals)
str2 = 'Welcome to Python'
print("str2 = ", str2)
str3 = 'This is a test.'
print("str3 = ", str3)
s = animals.capitalize()
print("animals.capitalize() = ", s)
s = str2.lower()
print("str2.lower() = ", s)
s = animals.upper()
print("animals.upper() = ", s)
s = animals.title()
print("animals.title() = ", s)
s = str2.swapcase()
print("str2.swapcase() = ", s)
s = str3.replace('is', 'was')
print("str3.replace('is', 'was') = ", s)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-1-4_gpt.py

animals = """Python is a programming language that lets you work quickly
and integrate systems more effectively."""

# 將 animals 以空白字元切割成串列 lst1
lst1 = animals.split()

# 顯示 lst1 內容
print(lst1)

# 將 lst1 合併成 CSV 字串 str2
str2 = ",".join(lst1)

# 顯示 str2 內容
print(str2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-1-4a_gpt.py

def clean_string(s):
    """
    刪除字符串中的 '\n', '\r' 和前後的空白

    :param s: str，待處理的字符串
    :return: str，刪除後的字符串
    """
    # 刪除 '\n' 和 '\r'
    s = s.replace('\n', '').replace('\r', '')
    # 刪除前後空白
    s = s.strip()
    return s

animals = "  Python is a \nprogramming language.\n\r   "
cleaned_str = clean_string(animals)
print(cleaned_str)  # "Python is a programming language."


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-1.py

lst1 = []
lst2 = [1, 2, 3, 4, 5]
lst3 = [1, 'Python', 5.5]
print(lst1)
print("lst2: ", lst2)
print(lst3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-1a.py

lst4 = list()
lst5 = list(["tom", "mary", "joe"])
lst6 = list("python")
print("lst4:" + str(lst4))
print("lst5:" + str(lst5))
print("lst6:" + str(lst6))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-1b.py

lst7 = [1, ["tom", "mary", "joe"], [3, 4, 5]]
print("lst7:" + str(lst7))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-2.py

lst1 = [1, 2, 3, 4, 5, 6]
print(lst1[0])
print(lst1[1])
print(lst1[-1])
print(lst1[-2])
lst1[1] = 10
lst1[2] = "Python"
print(lst1)

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-2a.py

lst1 = [1, 2, 3, 4, 5, 6]
for e in lst1:
    print(e, end=" ")
print()
animals = ['cat', 'dog', 'bat']
for index, animal in enumerate(animals):
    print(index, animal)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-2b.py

lst2 = [[2, 4], ['cat', 'dog', 'bat'], [1, 3, 5]]
print(lst2[1][0])
lst2[2][1] = 7
for e1 in lst2:
    for e2 in e1:
        print(e2, end=" ")

print("------------------------------------------------------------")  # 60個

lst2 = [[2, 4], ['cat', 'dog', 'bat'], [1, 3, 5]]
print(lst2[0][1])

print("------------------------------------------------------------")  # 60個

lst1 = [1, 5]
lst1.append(7)
print(lst1)
lst1.extend([9, 11, 13])
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-3a.py

lst1 = [1, 5, 7, 9, 11, 13]
lst1.insert(1, 3)
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-3b.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-4.py

lst1 = [4, 2, 8, 9, 1]
print("lst1 = ", lst1)
s = len(lst1)
print("len(lst1) = ", s)
s = max(lst1)
print("max(lst1) = ", s)
s = min(lst1)
print("min(lst1) = ", s)
animals = 'Hello World!'
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-4a.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-5_gpt.py

def find_max_and_index(lst1):
    """
    找出串列lst1中的最大值和最大值的索引
    :param lst1: 一個包含數字元素的串列
    :return: 一個包含最大值和最大值索引的元組
    """
    max_val = float('-inf')  # 初始化最大值
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-2-5a_gpt.py

def concatenate_strings(lst1):
    """
    從lst1中抽出是字串的項目，並連接成一個字串回傳。

    :param lst1: 一個含有多個項目的串列
    :type lst1: list
    :return: 連接所有字串項目後的字串
    :rtype: str
    """

    str_lst = [item for item in lst1 if isinstance(item, str)]
    return ''.join(str_lst)

my_list = ['Hello', 42, 'World', True, 'Python']
result = concatenate_strings(my_list)
print(result)  # 輸出：HelloWorldPython


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-3-1.py

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a = y)
print(s)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-3-1a.py

print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-3-2.py

x, y = 10, 20
s = f"Y= {x} X= {y}"
print(s)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-3-2a.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-4.py

animals = "This is a pen."
lst1 = animals.split()
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-4a.py

str2 = "Tom,Bob,Mary,Joe,John"
lst2 = str2.split(",")
print(lst2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch09\ch9-4b.py

str3 = "23\n52\n44\n78"
lst3 = str3.splitlines()
print(lst3)

print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-1.py

t1 = ()
t2 = (1, 2, 3, 4, 5)
t3 = (1, 'Joe', 5.5)
print(t1)
print("t2 = ", t2)
print(t3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-1a.py

t4 = tuple()
t5 = tuple(["tom", "mary", "joe"])
t6 = tuple("python")
print("t4 = " + str(t4))
print("t5 = " + str(t5))
print("t6 = " + str(t6))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-2.py

t1 = (1, 2, 3, 4, 5, 6)
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[-2])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-2a.py

t1 = (1, 2, 3, 4, 5, 6)
for e in t1:
    print(e, end=" ")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-3.py

t1 = (4, 2, 8, 9, 1)
print("t1 = ", t1)
s = len(t1)
print("len(t1) = ", s)
s = max(t1)
print("max(t1) = ", s)
s = min(t1)
print("min(t1) = ", s)
animals = 'Hello World!'
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-1-3a.py

t1 = (4, 2, 8, 9, 1, 8)
print("t1 = ", t1)
s = t1.count(8)
print("t1.count(8) = ", s)
s = t1.index(8)
print("t1.index(8) = ", s)
s = t1.index(1)
print("t1.index(1) = ", s)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-1.py

d1 = {}
d2 = {1: 'apple', 2: 'ball'}
d3 = {
       "name": "joe",
       1: [2, 4, 6]
     }
print(d1)
print("d2 = ", d2)
print(d3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-1a.py

d4 = dict()
d5 = dict([(1, "tom"), (2, "mary"), (3, "john")])
print("d4 = " + str(d4))
print("d5 = " + str(d5))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-2.py

d1 = {"chicken": 2, "dog": 4, "cat":3}
print(d1["cat"])
print(d1["dog"])
print(d1["chicken"])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-2a.py

d1 = {"chicken": 2, "dog": 4, "cat":3}
d1["cat"] = 4
print(d1)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-2b.py

d1 = {"chicken": 2, "dog": 4, "cat":3}
d1["spider"] = 8
print(d1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-2c.py

d1 = {"chicken": 2, "dog": 4, "cat":3}
for animal in d1:
    legs = d1[animal]
    print(animal, legs)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-2d.py

d1 = {"chicken": 2, "dog": 4, "cat":3}
for animal, legs in d1.items():
    print("動物: {0} 有 {1} 隻腳".format(animal, legs))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-3.py

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
del d1[2]
print(d1)
del d1["age"]
print(d1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-3a.py

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
e1 = d1.pop(5)
print(e1, d1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-3b.py

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
e2 = d1.popitem()
print(e2, d1)
e2 = d1.popitem()
print(e2, d1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-3c.py

d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
d1.clear()
print(d1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-4.py

d1 = {1:1, 3:9, 5:24, 7:47, 9:83}
print("d1 = ", d1)
s = len(d1)
d2 = dict([(1,"tom"), (2,"mary"), (3, "joe")])
print("d2 = ", d2)
d3 = sorted(d1)
print("d3 = sorted(d1) = ", d3)
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-4a.py

d1 = {"tom":2, "bob":3, "mike":4}
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-5_gpt.py

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
my_dict = {'a': 10, 'b': 20, 'c': 30}

# 使用 sum_dict_values() 函數獲取所有值的總和
total = sum_dict_values(my_dict)

# 列印總和
print(total)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-5a_gpt.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-5b_gpt.py

def create_dict(keys, values):
    """
    建立一個字典，使用傳入的keys作為鍵，values作為值。
    :param keys: 一個包含鍵的串列。
    :param values: 一個包含值的串列，鍵與值一一對應。
    :return: 一個字典，使用傳入的鍵值對建立。
    """
    return dict(zip(keys, values))

keys = ['apple', 'banana', 'orange']
values = [1, 2, 3]

my_dict = create_dict(keys, values)

print(my_dict)  # 輸出: {'apple': 1, 'banana': 2, 'orange': 3}


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-2-5c_gpt.py

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = zip(a, b)
print(list(c)) # 输出 [(1, 'a'), (2, 'b'), (3, 'c')]


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-1.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-2.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-3.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-4.py

print("green" == "glow")
print("green" != "glow")
print("green" > "glow")
print("green" >= "glow")
print("green" < "glow")
print("green" <= "glow")
d1 = {"tom":30, "bobe":3}
d2 = {"bobe":3, "tom":30}
print(d1 == d2)
print(d1 != d2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5.py

animals = 'Hello World!'
print("animals = ",animals)
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5a.py

lst1 = list('Hello World!')
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5b.py

t1 = tuple('Hello World!')
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

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5c.py

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:4] = [3, 5, 7]
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5d.py

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[2:2] = [1, 9]
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-3-5e.py

lst1 = [2, 4, 6, 8]
print(lst1)
lst1[1:3] = []
print(lst1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-4-1.py

lst1 = [x for x in range(10)]
print(lst1)
lst2 = [x+1 for x in range(10)]
print(lst2)
lst3 = [x for x in range(10) if x % 2 == 1]
print(lst3)
lst4 = [x*2 for x in range(10) if x %2 == 1]
print(lst4)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch10\ch10-4-2.py

d1 = {x: x*x for x in range(10)}
print(d1)
d2 = {x: x*x for x in range(10) if x % 2 == 0}
print(d2)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

r = abs(-10)
print("abs(-10) = ", r)
r = abs(5)
print("abs(5) = ", r)
r = pow(8, 2)
print("pow(8, 2) = ", r)
r = pow(2, 3)
print("pow(2, 3) = ", r)
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = ", r)
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = ", r)
r = round(5.32)
print("round(5.32) = ", r)
r = round(5.52)
print("round(5.52) = ", r)
r = round(3.14568757, 3)
print("round(3.14568757, 3) = ", r)
r = round(3.14568757, 1)
print("round(3.14568757, 1) = ", r)

bmi = 1.23456789

print("您的BMI值為：", round(bmi, 2))

# 輸出BMI值，並四捨五入到小數點後兩位
print("您的BMI值為：", round(bmi, 2))

print("------------------------------------------------------------")  # 60個

"""
path = os.getcwd() + "\\temp"
os.chdir(path)
print(path)
print(os.listdir(path))

print("------------------------------------------------------------")  # 60個
 
path = os.getcwd()
new_path = os.getcwd() + "\\temp"
print("目前工作路徑: ", path)
print(new_path)
os.chdir(new_path)
print("chdir(): ", new_path)
os.mkdir('newDir')
print("mkdir(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(new_path))
os.remove("aa.txt")
print("remove(): ", os.listdir(new_path))
"""

print("------------------------------------------------------------")  # 60個

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)

print("------------------------------------------------------------")  # 60個

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)

print("------------------------------------------------------------")  # 60個

import os.path as path
 
p = "D:\PythonChatGPT\ch11"
f = "ch11-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)

print("------------------------------------------------------------")  # 60個

import math
 
# 顯示數學常數
print("math.e = ", math.e)
print("math.pi = ", math.pi)

print("------------------------------------------------------------")  # 60個

import math
 
# 數學函數
no = -19.536
print("測試值no = ", no)
print("math.fabs(no) =  ", math.fabs(no))
print("math.ceil(no) = ", math.ceil(no))
print("math.floor(no) = ", math.floor(no))
# 指數和對數函數
x, y = 13.536, 3.57
print("測試值x / y = ", x, "/", y)
print("math.exp(x) = ", math.exp(x))
print("math.log(x) = ", math.log(x))
print("math.pow(x,y) = ", math.pow(x,y))
print("math.sqrt(x) = ", math.sqrt(x))
# 三角函數
deg = 60.0
rad = math.radians(deg)
print("測試值deg / rad = ", deg, "/", rad)
print("math.sin(rad) = ", math.sin(rad))
print("math.cos(rad) = ", math.cos(rad))
print("math.tan(rad) = ", math.tan(rad)) 

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("保留區")




