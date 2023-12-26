# ex16_4.py
import re
import os

files = os.listdir("D:\\Python\\ch14")
txtList = []
# 測試1
pattern = '(.*).txt'
print("列印*.txt")
for fn in files:
    #print(fn)
    fnresult = re.search(pattern,fn)      # 傳回搜尋結果
    if fnresult != None:
        txtList.append(fn)
print(txtList)

pyList = []  
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = '(ch14_1(\d).py)'
for fn in files:
    fnresult = re.search(pattern,fn)      # 傳回搜尋結果
    if fnresult != None:
        pyList.append(fn)
print(pyList)

