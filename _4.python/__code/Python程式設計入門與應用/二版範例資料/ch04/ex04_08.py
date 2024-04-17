# Filename: ex04_08.py
# 集合練習題
import os.path
import sys
keywords = {"reading","comprehension","digital","strategies","ability"}
filename = input("請輸入檔案名稱:").strip()
if not os.path.isfile(filename):
    print("%filename檔案不存在"%(filename))
    sys.exit()
pfile = open(filename,"r")
ptext = pfile.read().split()
pcount = 0
for word in ptext:
    if word in keywords:
        pcount +=1
print("檔案中的關鍵中出現%d次"%(pcount))        