print("------------------------------------------------------------")  # 60個

import sys
import csv
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個


import csv

f = open("data/tScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csvReader = csv.reader(f, delimiter="\t")  # 建立reader物件使用 '\t' 當分隔符號
listData = list(csvReader)  # 使用list()函數將data轉成串列再指定給Reader
for row in listData:  # 使用巢狀迴圈將ListData串列逐欄印出
    for col in row:
        print(col, "   ", end="")
    print()
f.close()

print("------------------------------------------------------------")  # 60個

import csv

f = open("data/StudentScore.csv")
data = csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in data:  # 逐一印出字典的內容
    print(row)
f.close()

print("------------------------------------------------------------")  # 60個

import csv

f = open("data/StudentScore.csv")
data = csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
print("學號\t姓名\t國文\t英語\t數學\t總分")
for row in data:  # 逐一印出字典的內容，並計算總分
    print(
        "{}\t{}\t{}\t{}\t{}\t{}".format(
            row["學號"],
            row["姓名"],
            row["國文"],
            row["英語"],
            row["數學"],
            (int(row["國文"]) + int(row["英語"]) + int(row["數學"])),
        )
    )
f.close()

print("------------------------------------------------------------")  # 60個

import csv

# searchName=input('請輸入學生姓名進行查詢成績：') #輸入查詢姓名

searchName = "david"

f = open("data/StudentScore.csv")
data = csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in data:  # 逐一比對姓名是否符合searchName
    if row["姓名"] == searchName:
        print("{}成績資訊如下：".format(row["姓名"]))
        print("學號：{}".format(row["學號"]))
        print("國文：{}".format(row["國文"]))
        print("英語：{}".format(row["英語"]))
        print("數學：{}".format(row["數學"]))
        print("總分：{}".format((int(row["國文"]) + int(row["英語"]) + int(row["數學"]))))
        break  # 離開迴圈
else:  # 當迴圈沒有執行break，即會執行else區域，表示沒有找到符合姓名
    print("查無{}成績".format(searchName))
f.close()

print("------------------------------------------------------------")  # 60個

import csv

f = open("tmp_dictWriterProduct.csv", "w", newline="")
# 建立writer物件，同時指定欄位名稱
csvWriter = csv.DictWriter(f, fieldnames=["產品編號", "品名", "單價"])
csvWriter.writeheader()  # 寫入欄位名稱
csvWriter.writerow({"產品編號": "A02", "品名": "黑松沙士", "單價": 90})
# 寫入兩筆產品記錄到csv檔中
csvWriter.writerow({"產品編號": "A02", "品名": "草苺蛋糕", "單價": 120})
f.close()

print("------------------------------------------------------------")  # 60個

import csv

f = open("data/StudentScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csvReader = csv.reader(f)  # 使用csv的reader()方法取得檔案物件f的資料並傳回Reader物件
listData = list(csvReader)  # 使用list()函數將data轉換串列再指定給listData
for row in listData:  # 將二維串列listData 逐列印出
    print(row)
f.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

import csv

f = open("data/StudentScore.csv")  # 建立檔案物件f，此物件操作StudentScore.csv
csvReader = csv.reader(f)  # 使用csv的reader()方法取得檔案物件f的資料並傳回Reader物件
listData = list(csvReader)  # 使用list()函數將csvReader轉成串列再指定給listData
for row in listData:  # 使用巢狀迴圈將ListData串列逐欄印出
    for col in row:
        print(col, "  ", end="")
    print()
f.close()

print("------------------------------------------------------------")  # 60個

import csv

f = open("tmp_writerProduct.csv", "w", newline="")  # 開啟writerProduct.csv檔案
csvWriter = csv.writer(f)  # 建立writer物件，物件名稱為csvWriter
# 建立listProduct二維串列有兩筆產品
listProduct = [["B01", "小林煎餅", "78"], ["B02", "五香豆干", "90"]]
# 寫入一維串列當做標題
csvWriter.writerow(["編號", "品名", "單價"])
csvWriter.writerows(listProduct)  # 將二維串列的兩筆產品寫入csv內
f.close()  # 關閉檔案

print("------------------------------------------------------------")  # 60個

"""
import csv

listProduct=["","",""] # 建立listProduct串列，用來存放一筆產品記錄
while True:
     option = input("功能選單：1.新增 2.查詢 3.離開：")
     if option=="1":
         # 以附加模式開啟tProduct.csv檔案
         f=open('tProduct.csv','a', newline='') 
         csvWriter=csv.writer(f) 
         listProduct[0] = input("編號：")   #listProduct[0]存放編號
         listProduct[1] = input("品名：")   #listProduct[1]存放品名
         listProduct[2] = input("單價：")   #listProduct[2]存放單價
         csvWriter.writerow(listProduct)
         print("新增成功")
         f.close()
     elif option=="2" :
         # 以讀檔模式開啟tProduct.csv檔案
         f=open ('tProduct.csv')
         data=csv.DictReader(f)  
         print("編號\t品名\t單價")
         for row in data:   		
             print("{}\t{}\t{}".format(row['編號'],row['品名'],row['單價']))
         f.close()
     else:
         break
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
