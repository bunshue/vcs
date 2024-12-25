"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

# 從 builtins 模組裡面可以取得所有的內建物件

import builtins

print(dir(builtins))


print("------------------------------------------------------------")  # 60個

#數值型態跟非數值型態的運算，必須明確的轉型



a = 123
b = "abc"
str(a) + b


# 使用 dir() 列出 local scope 裡面有那些變數或模組等
cc = dir()
print(cc)


# 使用 dir(module) 列出模組可以使用的屬性及方法等
cc = dir(sys)
print(cc)

print("------------------------------------------------------------")  # 60個

#格式化輸出

#傳統作法 - 01

Name = 'david'
A = 123
B = 456

print('Name=' + Name + ': A=' + str(A) + '; B=' + str(B))

#傳統作法 - 02

print('Name=%s: A=%d; B=%d' % (Name, A, B))
print('Name=%s: A=%d; B=%f' % (Name, A, B))
print('Name=%s: A=%d; B=%3.5f' % (Name, A, B))

#建議做法

print('Name={0}: A={1}; B={2}'.format(Name, A, B))
print('Name={}: A={}; B={}'.format(Name, A, B))

print("{0}, {1}, {0}".format(123, "abc"))


print("------------------------------------------------------------")  # 60個

"""

什麼是 Encode()？

將字串轉換成特定格式(如UTF-8)的 bytes，以便於儲存或網路傳輸。
什麼是 Decode()？

將特定格式的 bytes，轉換回字串以便於顯示。

"""
a = "中文"
b = a.encode('utf-8')
b

type(b)

b.decode('utf-8')

# 從字元找對應的 codepoint
ord('中')

# 從 codepoint 找回字元
chr(20013)

hex(ord('中'))

print("------------------------------------------------------------")  # 60個

"""
Python 的運算子
算術運算子
比較運算子
指定運算子
邏輯運算子 (Logical Operators)
位元運算子 (Bitwise Operators)
成員運算子 (Membership Operators) (in, not in)
相等運算子 (Identity Operators) (is, is not) 會比較兩變數的記憶體位置是否相等。
"""
print("------------------------------------------------------------")  # 60個

A = range(1,10, 2)

for i, item in enumerate(A):    # enumerate: iterator
    print('{}: {} \n'.format(i, item))


for cc in enumerate(A):    # enumerate: iterator
    print(cc)



print("------------------------------------------------------------")  # 60個

#Python 生成式 (Comprehension)
"""
重點：
    list comprehension
    dict comprehension
    set comprehension
    generator comprehension
"""

# list comprehension
a = [1, 2, 3]
b = [e**2 for e in a]
b

# dict comprehension
word = "letters"
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

# set comprehension
a_set = {number for number in range(1, 6) if number % 3 == 1}
a_set

# generator comprehension
a = [1, 2, 3]
b = (e**2 for e in a)
b

for c in b:
    print(c)

print("------------------------------------------------------------")  # 60個

# 如果知道可能產生的錯誤是甚麼
a = 5
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print("哇！除數是零!")

import sys

try:
    c = a / b
except:
    print(sys.exc_info())


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
