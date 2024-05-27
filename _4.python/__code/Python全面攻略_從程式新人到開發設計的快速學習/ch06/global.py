# -*- coding: utf-8 -*-

def order(str, num):
    global no
    print (f"菜單編號：{no}  品名：{str} 數量：{num}")
    no += 1

no = 1

while (True):
    s = input("請輸入品名：")
    n = input("請輸入數量：")
    order(s, n)
    i = input("是否繼續輸入？(y/n)")
    if(i in "nN"):
        break
    