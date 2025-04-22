print("自定義函數, 寫在另一個檔案裏面")

#       位置              檔案名
from module_files import draw_bar

draw_bar.draw(10, "$")
draw_bar.draw(6, "#")
draw_bar.draw(15)

from module_files import my_print  # 把整個 my_print.py 都引進來

print("測試導入自定義模組")
my_print.print_func("Python")


from module_files import calculate  # 匯入 calculate 模組

print(calculate.add(5, 2))  # 7
print(calculate.sub(5, 2))  # 3

"""
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
"""
