# -*- coding: utf-8 -*-
dict1 = {}
for i in range(3):
    data = []
    site = input("請輸入平台名稱：")
    data.append(input("請輸入帳號："))
    data.append(input("請輸入密碼："))
    dict1[site] = data
site = input("請輸入要查詢的平台名稱：")
data = dict1.get(site, False)
if data == False:
    print("無此資料!")
else:
    print(f"{site}的帳號：{data[0]}；密碼：{data[1]}")
