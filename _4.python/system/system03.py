import sys

print('------------------------------------------------------------')	#60個


print("sys.argv:{}".format(sys.argv))
print("文件名稱{}".format(sys.argv[0]))
length = len(sys.argv)

""" 
if len(sys.argv) < 2:
    sys.exit(0)

for i in range(1,length):
     n1 = sys.argv[i]
     print( "第{}個引數是{}".format(i,n1))
"""

print('------------------------------------------------------------')	#60個

import os
print(os.name)

if os.name == 'nt':
    print('Windows NT 系統')
    import nt
    print(sys.getwindowsversion())
    print(sys.getwindowsversion()[:2])
    if sys.getwindowsversion()[:2] >= (6, 0):
        print('Win10')
    else:
        print('非Win10')
else:
    print('非 Windows NT 系統')

print('------------------------------------------------------------')	#60個


"""
print('Press Ctrl-C to quit.')

while True:
    try:
        time.sleep(1)
        print('A', end = ' ')
    except KeyboardInterrupt:
        print('你按了 ctrl + C, 離開')
        sys.exit()
"""

"""
import time, sys

print("Press Ctrl-C to stop.")

try:
    while True:  # Main program loop.
        print("wait", end=" ")
        time.sleep(1)  # Add a pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""



print('------------------------------------------------------------')	#60個

import os
import sys
m = sys.modules.get('__main__')

print(m)



print('------------------------------------------------------------')	#60個


import os

print(os.name)
print(os.sys.platform)




print('------------------------------------------------------------')	#60個


print('取得本程式名稱')
progname = os.path.basename(sys.argv[0])
print(progname)



print('------------------------------------------------------------')	#60個

try:
    import a_python_module
except ImportError:
    print("匯入模組 a_python_module 失敗")
    print("請安裝模組")
    # sys.exit()

print("------------------------------------------------------------")  # 60個

import sys

if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])
 

print('------------------------------------------------------------')	#60個

import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

print('------------------------------------------------------------')	#60個


import numpy as np
import pandas as pd

print(np.__version__)

import numpy

print(numpy.version.version)

# 使用 importlib.metadata 模块查找 NumPy 模块的版本
from importlib_metadata import version

print(version("numpy"))

import pkg_resources

print(pkg_resources.get_distribution("numpy").version)


print("查詢已安裝的 Pandas 版本")
print(pd.__version__)

import pandas as pd

print(pd.__version__)

print("------------------------------------------------------------")  # 60個

# import this	可以看到 Zen of Python



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


