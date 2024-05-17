"""
讀寫 Excel 檔案, 使用 openpyxl

"""

import sys
import openpyxl

print('------------------------------------------------------------')	#60個

print('excel讀寫測試 1')

print("寫讀 xlsx")

print("建立 xlsx")

workbook=openpyxl.Workbook()    # 建立一個工作簿

# 取得第 1 個工作表
sheet = workbook.worksheets[0]

# 以儲存格位置寫入資料
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# 以串列寫入資料
listtitle=["姓名","電話"]
sheet.append(listtitle)  
listdata=["David","0999-1234567"]
sheet.append(listdata)

# 儲存檔案
filename = 'tmp_test1.xlsx'
workbook.save(filename)

print("建立 xlsx OK, 檔案 : " + filename)

print('------------------------------------------------------------')	#60個

import csv
import openpyxl

print('excel讀寫測試 2')

filename = 'C:/_git/vcs/_4.python/_data/animals2.csv'
csvfile = open(filename)  # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)  # 讀取 CSV 檔案
data = list(raw_data)  # 轉換成二維串列
print(data)

workbook = openpyxl.Workbook()  # 建立空白的 Excel 活頁簿物件
sheet = workbook.create_sheet("animal")  # 建立新工作表 名為animal

"""
# 以儲存格位置寫入資料
sheet['A1'] = '中文名'
sheet['B1'] = '英文名'
sheet['C1'] = '體重'
sheet['D1'] = '全名'
"""

for i in data:
    print(i)
    sheet.append(i)  # 逐筆添加到最後一列

# 儲存檔案
filename = "tmp_test2_fail.xlsx"
workbook.save(filename)

print("建立 xlsx OK, 檔案 : " + filename)

print('------------------------------------------------------------')	#60個

print('excel讀寫測試 3')

filename = 'data/python_ReadWrite_EXCEL3.xlsx'

print("讀取 xlsx, 檔案 : " + filename)

#  讀取檔案
workbook = openpyxl.load_workbook(filename)
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
print("顯示資料");
# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)
# 取得總行、列數
print(sheet.max_row, sheet.max_column)
# 顯示 cell資料
for i in range(1, sheet.max_row+1):
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()
sheet['A3'] = 'David' 

print("另存新檔");
filename2 = 'tmp_test2b.xlsx'
workbook.save(filename2)
print("另存新檔 OK, 檔案 : " + filename2)

print('------------------------------------------------------------')	#60個
print('excel讀寫測試 4')

#各種檔案寫讀範例 xlsx 2

import openpyxl
filename = 'data/python_ReadWrite_EXCEL5_population2.xlsx'

print("讀取 xlsx, 檔案 : " + filename)

workbook = openpyxl.load_workbook(filename)
sheet = workbook.active

list_values = list(sheet.values)
print('所有資料')
print(list_values)
print()

print('標題欄')
cols = list_values[0]
print(cols)

cnt = 0
for value_tuple in list_values[1:]:
    print('第', cnt, '筆資料 :', value_tuple)
    #print(type(value_tuple))
    cnt += 1

print('------------------------------------------------------------')	#60個

import openpyxl

filename = 'data/sample.xlsx'

workbook = openpyxl.load_workbook(filename)
for sheet in workbook:
    print('sheet')
    for row in sheet:
        #print('row')
        for cell in row:
            print(cell.value, end = ' ')
        print()

print('------------------------------------------------------------')	#60個

import os
import time
import openpyxl

# User info
firstname = 'David'
lastname = 'Wang'
        
title = 'kkkkkkkk'
age = 22
nationality = 'Taiwan'
            
# Course info
registration_status = 'aaa'
numcourses = 'cccc'
numsemesters = 'ddddd'
            
print("First name: ", firstname, "Last name: ", lastname)
print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
print("Registration status", registration_status)
print("------------------------------------------")

filepath = 'tmp_excel_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.xlsx'
            
if not os.path.exists(filepath):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
               "# Courses", "# Semesters", "Registration status"]
    sheet.append(heading)
    workbook.save(filepath)
workbook = openpyxl.load_workbook(filepath)
sheet = workbook.active
sheet.append([firstname, lastname, title, age, nationality, numcourses,
              numsemesters, registration_status])
workbook.save(filepath)



print('------------------------------------------------------------')	#60個

import openpyxl
from openpyxl.chart import RadarChart, Reference

print('在excel檔案內加入雷達圖')

workbook = openpyxl.load_workbook(r"data/radar_chart.xlsx")
sh = workbook.active

data = Reference(sh, min_col=2, max_col=4, min_row=1, max_row=sh.max_row)
labels = Reference(sh, min_col=1, min_row=2, max_row=sh.max_row)

chart = RadarChart()
#預設為standard
#filled為填色
#chart.type = "filled"
chart.title = "各部門業績"
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)

sh.add_chart(chart, "F2")
workbook.save(r"tmp_add_radar_chart.xlsx")


print('------------------------------------------------------------')	#60個

#創建Excel文件

# 這個有問題

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    ['1001', '白元芳', '男', '13123456789'],
    ['1002', '白潔', '女', '13233445566']
]
sheet.append(['學號', '姓名', '性別', '電話'])
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")
tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./tmp_全班學生數據.xlsx')


print('------------------------------------------------------------')	#60個

#讀取Excel文件

from openpyxl import load_workbook
from openpyxl import Workbook

workbook = load_workbook('./data/學生明細表.xlsx')
print(workbook.sheetnames)
sheet = workbook[workbook.sheetnames[0]]
print(sheet.title)
for row in range(2, 7):
    for col in range(65, 70):
        cell_index = chr(col) + str(row)
        print(sheet[cell_index].value, end='\t')
    print()

print('------------------------------------------------------------')	#60個
""" 無檔案
import openpyxl

wb = openpyxl.load_workbook("oxxostudio.xlsx")  # 開啟 Excel 檔案

names = wb.sheetnames  # 讀取 Excel 裡所有工作表名稱
s1 = wb["工作表1"]  # 取得工作表名稱為「工作表1」的內容
s2 = wb.active  # 取得開啟試算表後立刻顯示的工作表 ( 範例為工作表 2 )

print(names)
# 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數
print(s1.title, s1.max_row, s1.max_column)
print(s2.title, s2.max_row, s2.max_column)
"""
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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



