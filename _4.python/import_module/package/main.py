"""
# 使用 packageA

# import packageA
from packageA import x
from packageA import *

print(x)
print(moduleA.x)
"""

import packageA

print('使用packageA的參數')
print(packageA.__author__)
print(packageA.__version__)
print(packageA.__date__)
print(packageA.__status__)


print(packageA.CRITICAL)

print(packageA.xa)
print(packageA.xb)
print(packageA.xc)

