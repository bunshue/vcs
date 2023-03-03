# _*_ coding: utf-8 _*_
# 程式 8-3.py (Python 3 version)

import sys

if len(sys.argv)<2:
    print("使用方法：python 8-2.py 學生班級")
    exit(1)
std_data=dict()
with open(sys.argv[1], encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)
