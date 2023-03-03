# _*_ coding: utf-8 _*_
# 程式 8-2 (Python 3 version)

import sys

print("參數長度={}".format(len(sys.argv)))
i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i,arg))
    i += 1
