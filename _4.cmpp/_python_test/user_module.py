def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2

print(add(5,2))  # 7
print(sub(5,2))  # 3




import calculate  # 匯入 calculate 模組

print(calculate.add(5,2))  # 7
print(calculate.sub(5,2))  # 3

from calculate import add,sub

print(add(5,2))  # 7
print(sub(5,2))  # 3

from calculate import add

print(add(5,2))  # 7
print(sub(5,2))  # NameError: name 'sub' is not defined


from calculate import *

print(add(5,2))  # 7
print(sub(5,2))  # 3


from calculate import add as a

print(a(5,2))  # 7

import calculate as cal # 匯入 calculate 模組，並取別名為 cal

print(cal.add(5,2))  # 7
print(cal.sub(5,2))  # 3


