import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import os
print(os.name)
print(os.sys.platform)


print('------------------------------------------------------------')	#60個

for envname in 'TMPDIR', 'TEMP', 'TMP':
    dirname = os.getenv(envname)
    print('cccccc', dirname)
    #print(dirname)

print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd

print(np.__version__)

import numpy 
print(numpy.version.version)

#使用 importlib.metadata 模块查找 NumPy 模块的版本
from importlib_metadata import version
print(version('numpy'))

import pkg_resources
print(pkg_resources.get_distribution('numpy').version)


print('查詢已安裝的 Pandas 版本')
print(pd.__version__)

import pandas as pd
print(pd.__version__)

print('------------------------------------------------------------')	#60個

#import this	可以看到 Zen of Python

#lambda : 只有單一運算式的匿名函式
add = lambda x, y : x + y  #冒號前是參數, 冒號後是運算式
cc = add(3, 5)
print('使用 lambda 做加法:', cc)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



