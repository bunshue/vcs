# 程式 6-1.py (Python 3.x version)
# _*_ coding: utf-8 _*_

def add2number(a, b):
    global d
    c = a + b
    d = a + b
    print("在函數中，(c={}, d={})".format(c,d))
    return c

c = 10
d = 99
print("呼叫函數前，(c={}, d={})".format(c,d))
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
print("函數呼叫後，(c={}, d={})".format(c,d))

  
