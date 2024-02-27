"""
相關抽出

各種檔案讀寫


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxostudio.xlsx")  # 開啟 Excel 檔案

names = wb.sheetnames  # 讀取 Excel 裡所有工作表名稱
s1 = wb["工作表1"]  # 取得工作表名稱為「工作表1」的內容
s2 = wb.active  # 取得開啟試算表後立刻顯示的工作表 ( 範例為工作表 2 )

print(names)
# 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數
print(s1.title, s1.max_row, s1.max_column)
print(s2.title, s2.max_row, s2.max_column)


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("test.xlsx", data_only=True)  # 設定 data_only=True 只讀取計算後的數值

s1 = wb["工作表1"]
s2 = wb["工作表2"]

print(s1["A1"].value)  # 取出 A1 的內容
print(s1.cell(1, 1).value)  # 等同取出 A1 的內容
print(s2["B2"].value)  # 取出 B2 的內容
print(s2.cell(2, 2).value)  # 等同取出 B2 的內容


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("test.xlsx", data_only=True)  # 設定 data_only=True 只讀取計算後的數值

s1 = wb["工作表1"]
s2 = wb["工作表2"]


def get_values(sheet):
    arr = []  # 第一層串列
    for row in sheet:
        arr2 = []  # 第二層串列
        for column in row:
            arr2.append(column.value)  # 寫入內容
        arr.append(arr2)
    return arr


print(get_values(s1))  # 印出工作表 1 所有內容
print(get_values(s2))  # 印出工作表 2 所有內容

"""
[[12, 34, 56, 78, 180, 180], [11, 22, 33, 44, 110, 110]]
[['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a4', 'b4', 'c4'], ['a5', 'b5', 'c5']]
"""


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("test.xlsx", data_only=True)

s1 = wb["工作表1"]
v = s1.iter_rows(min_row=1, min_col=1, max_col=2, max_row=2)  # 取出四格內容
print(v)
for i in v:
    for j in i:
        print(j.value)
"""
12
34
11
22
"""


print("------------------------------------------------------------")  # 60個

import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

print(column_index_from_string("A"))  # 1
print(column_index_from_string("AA"))  # 27

print(get_column_letter(5))  # E
print(get_column_letter(100))  # CV


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.Workbook()  # 建立空白的 Excel 活頁簿物件
wb.save("empty.xlsx")  # 儲存檔案


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx")  # 開啟現有的 Excel 活頁簿物件
wb.save("new.xlsx")  # 儲存檔案


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx")  # 開啟 Excel 檔案

s1 = wb["工作表1"]  # 取得工作表名稱為「工作表1」的內容
s2 = wb.active  # 取得開啟試算表後立刻顯示的工作表 ( 範例為工作表 2 )

print(
    s1.title, s1.max_row, s1.max_column
)  # 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數
print(
    s2.title, s2.max_row, s2.max_column
)  # 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數

print(s1.sheet_properties)  # 印出工作表屬性


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s1 = wb["工作表1"]  # 開啟工作表 1
s2 = wb["工作表2"]  # 開啟工作表 2
s1.sheet_properties.tabColor = "ff0000"  # 修改工作表 1 頁籤顏色為紅色
s2.sheet_properties.tabColor = "ffff00"  # 修改工作表 2 頁籤顏色為黃色

wb.create_sheet("工作表3")  # 插入工作表 3 在最後方
wb.create_sheet("工作表1.5", 1)  # 插入工作表 1.5 在第二個位置 ( 工作表 1 和 2 的中間 )
wb.create_sheet("工作表0", 0)  # 插入工作表 0 在第一個位置

wb.copy_worksheet(s2)  # 複製工作表 2 放到最後方

s1.title = "oxxo"  # 修改工作表 1 的名稱為 oxxo
s2.title = "studio"  # 修改工作表 2 的名稱為 studio

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s1 = wb["工作表1"]  # 開啟工作表 1
s1["A1"].value = "apple"  # 儲存格 A1 內容為 apple
s1["A2"].value = "orange"  # 儲存格 A2 內容為 orange
s1["A3"].value = "banana"  # 儲存格 A3 內容為 banana
s1.cell(1, 2).value = 100  # 儲存格 B1 內容 ( row=1, column=2 ) 為 100
s1.cell(2, 2).value = 200  # 儲存格 B2 內容 ( row=2, column=2 ) 為 200
s1.cell(3, 2).value = 300  # 儲存格 B3 內容 ( row=3, column=2 ) 為 300

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s3 = wb.create_sheet("工作表3")  # 新增工作表 3
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 二維陣列資料
for i in data:
    s3.append(i)  # 逐筆添加到最後一列

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s2 = wb["工作表2"]  # 開啟工作表 2
data = [[1, 2], [3, 4]]  # 二維陣列資料
for y in range(len(data)):
    for x in range(len(data[y])):
        row = 2 + y  # 寫入資料的範圍從 row=2 開始
        col = 2 + x  # 寫入資料的範圍從 column=2 開始
        s2.cell(row, col).value = data[y][x]

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import openpyxl

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s2 = wb["工作表2"]
s2["d1"] = "=sum(a1:c1)"  # 寫入公式
s2["d2"] = "=sum(a2:c2)"  # 寫入公式
s2["d3"] = "=sum(a3:c3)"  # 寫入公式
s2["d4"] = "=sum(a4:c4)"  # 寫入公式
s2["d5"] = "=sum(a5:c5)"  # 寫入公式

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import openpyxl
from openpyxl.styles import Font, PatternFill  # 載入 Font 和 PatternFill 模組

wb = openpyxl.load_workbook("oxxo.xlsx", data_only=True)

s1 = wb["工作表1"]
s1["e1"].font = Font(name="Arial", color="ff0000", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
s1["f1"].fill = PatternFill(fill_type="solid", fgColor="DDDDDD")  # 設定 f1 儲存格的背景樣式

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個

import csv

csvfile = open("csv-demo.csv")  # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)  # 讀取 CSV 檔案
data = list(raw_data)  # 轉換成二維串列
print(data)
"""
[['name', 'id', 'color', 'price'],
 ['apple', '1', 'red', '10'],
 ['orange', '2', 'orange', '15'],
 ['grap', '3', 'purple', '20'],
 ['watermelon', '4', 'green', '30']]
"""


print("------------------------------------------------------------")  # 60個

import csv
import openpyxl

csvfile = open("csv-demo.csv")  # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)  # 讀取 CSV 檔案
data = list(raw_data)  # 轉換成二維串列

wb = openpyxl.Workbook()  # 建立空白的 Excel 活頁簿物件
sheet = wb.create_sheet("csv")  # 建立空白的工作表
for i in data:
    sheet.append(i)  # 逐筆添加到最後一列

wb.save("test2.xlsx")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
