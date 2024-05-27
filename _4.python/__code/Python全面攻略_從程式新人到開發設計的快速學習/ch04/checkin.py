# -*- coding: utf-8 -*-
tel = []
indata = []
outdata = []
while True:
    s1 = input("請輸入電話號碼：")
    if (s1 in tel):
        idx = tel.index(s1)
        tel.remove(s1)
        lst = indata.pop(idx)
        t1 = input("請輸入離開時間：")
        lst.append(t1)
        lst.append(s1)
        outdata.append(lst)
    else:
        tel.append(s1)
        lst = []
        lst.append(input("請輸入進入時間："))
        lst.append(input("請輸入體温："))
        indata.append(lst)
    ch = input("是否繼續登錄(y/n)？")
    if (ch in "nN"):
        break

if (len(outdata) > 0):
    print(" ---出--入--人--員--記--錄---")
    print("進入時間-體 温-離開時間-電話號碼")
    for item in outdata:
        print(f" {item[0]}  {item[1]}  {item[2]}   {item[3]}")
if (len(indata) > 0):
    print("--館-內-人-員-記-錄---")
    print("進入時間-體 温-電話號碼")
    for i in range (len(indata)):
        print(f" {indata[i][0]}  {indata[i][1]}  {tel[i]}")
        

