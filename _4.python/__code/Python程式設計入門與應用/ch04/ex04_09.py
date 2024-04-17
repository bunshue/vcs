# Filename: ex04_09.py
# 集合練習題
import os.path
import sys
filename = input("請輸入檔案名稱:").strip()
if not os.path.isfile(filename):
    print("%filename檔案不存在"%(filename))
    sys.exit()
pfile = open(filename,"r")
ptext = pfile.read().split()
pcount = {}
for line in ptext:
    line = line.lower()
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.;:!{}[]'\"":
            line=line.replace(ch," ")
    words = line.split()
    for word in words:
        if word in pcount:
            pcount[word] +=1
        else:
            pcount[word]=1
pairs = list(pcount.items())
items = [[x,y] for (y,x) in pairs]
items.sort()
for i in range(len(items)-1, len(items)-6,-1):
    print(items[i][1]+"\t"+str(items[i][0]))