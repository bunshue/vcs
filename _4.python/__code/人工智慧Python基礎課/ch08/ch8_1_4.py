# coding: utf-8
x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a = y)
print(s)
print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))
