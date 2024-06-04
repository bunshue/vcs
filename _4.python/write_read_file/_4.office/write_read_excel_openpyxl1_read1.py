"""
使用 openpyxl 讀取 Excel 檔案

pip3 install openpyxl

專有名詞
workbook（活頁簿）：也就是一個excel檔案
worksheet（工作表）：一個excel可以有很多個工作表，目前正在觀看或處理的工作表又稱作「活動中的工作表（active sheet）」
欄（column）：工作表中的直欄，以A、B、C…代表
行（row）：工作表中的橫列，以1、2、3…代表
儲存格（cell）：工作表中的每一個都是一個儲存格

1. 讀取檔案info
2. 讀取檔案所有資料

"""

import os
import sys
import time
import openpyxl

print("------------------------------------------------------------")  # 60個

print("openpyxl test 01 通用訊息")

filename_r = "data/python_ReadWrite_EXCEL.xlsx"

print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)

names = workbook.sheetnames  # 讀取 excel檔案 裏所有工作表名稱
print("所有工作表名稱 :", names)

# 取得最後編輯的那個工作表
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print(workbook.active)
print(workbook.active.title)

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 取得工作表參數
sheet_name = sheet.title
ROW = sheet.max_row
COL = sheet.max_column
print("此工作表名稱、總列數、總行數 :", sheet_name, ROW, COL)
print("工作表有資料最大欄數", COL)
print("工作表有資料最小欄數", sheet.min_column)
print("工作表有資料最大列數", ROW)
print("工作表有資料最小列數", sheet.min_row)

# 取得第 0 個工作表 same
sheet = workbook[workbook.sheetnames[0]]
print("第 0 個工作表名稱 :", sheet.title)

sheet1 = workbook["animals1"]  # 取得工作表名稱為「工作表1」的內容
sheet2 = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數")
print(sheet1.title, sheet1.max_row, sheet1.max_column)
print(sheet2.title, sheet2.max_row, sheet2.max_column)

print(sheet2.sheet_properties)  # 印出工作表屬性

from openpyxl.utils import get_column_letter, column_index_from_string

print(column_index_from_string("A"))  # 1
print(column_index_from_string("Z"))  # 26
print(column_index_from_string("AA"))  # 27
print(column_index_from_string("ZZ"))  # 702

print("A = ", column_index_from_string('A'))
print("B = ", column_index_from_string('B'))

print(get_column_letter(5))  # E
print(get_column_letter(100))  # CV

ROW = sheet.max_row
COL = sheet.max_column

for i in range(1, COL+1):
    print(i, ' = ', get_column_letter(i))

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("目前工作表： ", workbook.active.title)

workbook.active = workbook["animals2"]
print("目前工作表： ", workbook.active.title)

print("------------------------------------------------------------")  # 60個

print("顯示最大、最小 欄數、列數")

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("儲存格 欄名", sheet["A1"].column)
print("儲存格 列名", sheet["A1"].row)
print("儲存格名", sheet["A1"].coordinate)

print("------------------------------")  # 30個

print("顯示資料 方法一")

print("使用cell方法取得資料")
sheet1 = workbook["animals1"]
sheet2 = workbook["animals2"]

# 取得指定儲存格資料
print(sheet1["A1"], sheet1["A1"].value)

print(sheet1["A1"].value)  # 取出 A1 的內容
print(sheet1.cell(1, 1).value)  # 等同取出 A1 的內容

print(sheet2["B2"].value)  # 取出 B2 的內容
print(sheet2.cell(2, 2).value)  # 等同取出 B2 的內容

# 顯示 cell資料
for i in range(1, ROW + 1):
    for j in range(1, COL + 1):
        print(sheet.cell(row=i, column=j).value, end="   ")
    print()

print("------------------------------")  # 30個

print("顯示資料 方法二")

list_values = list(sheet.values)
print("所有資料")
print(list_values)
print()

print("標題欄")
cols = list_values[0]
print(cols)

cnt = 0
for value_tuple in list_values[1:]:
    print("第", cnt, "筆資料 :", value_tuple)
    # print(type(value_tuple))
    cnt += 1

print("------------------------------")  # 30個

print("顯示資料 方法三 所有工作表")

for sheet in workbook:
    print("工作表 sheet :", sheet)
    for row in sheet:
        # print('row')
        for cell in row:
            print(cell.value, end=" ")
        print()
    print()

print("------------------------------")  # 30個

print("顯示資料 方法四")

workbook = openpyxl.load_workbook(filename_r)
for sheetname in workbook.sheetnames:  # 所有工作表
    sheet = workbook[sheetname]
    ROW = sheet.max_row
    COL = sheet.max_column
    print("此工作表名稱、總列數、總行數 :", sheet_name, ROW, COL)
    for c in range(1, COL + 1):  # 欄1〜最後
        for r in range(1, ROW + 1):  # 列1〜最後
            cell = sheet.cell(row=r, column=c)  # 儲存格
            if cell.value != None:
                print(cell.value, end=" ")
        print()

print("------------------------------")  # 30個

print("顯示資料 方法五")


def get_values(sheet):
    arr = []  # 第一層串列
    for row in sheet:
        arr2 = []  # 第二層串列
        for column in row:
            arr2.append(column.value)  # 寫入內容
        arr.append(arr2)
    return arr


sheet1 = workbook["animals1"]
sheet2 = workbook["animals2"]

print("印出工作表1 所有內容")
print(get_values(sheet1))

print("印出工作表2 所有內容")
print(get_values(sheet2))

print("------------------------------")  # 30個

print("顯示資料 方法六")

sheet1 = workbook["animals1"]
v = sheet1.iter_rows(min_row=1, min_col=1, max_col=5, max_row=4)  # 取出四格內容
#print(v)
for i in v:
    for j in i:
        print(j.value, end=" ")
    print()

print("------------------------------")  # 30個
print('之前先顯示工作表')
print("目前工作表： ", workbook.active.title)

print("顯示資料 方法七 讀取工作表所有內容")

filename_r = "data/python_ReadWrite_EXCEL.xlsx"
workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("excel活動工作表： ", sheet)

for row in sheet:
    for cell in row:
        print(cell.value, end = " ")
    print()
print()

print('之後先顯示工作表')
print("目前工作表： ", workbook.active.title)

print("------------------------------")  # 30個

print("讀取工作表某欄某列的資料")

print("讀取 C 欄的所有資料")
for cell in sheet["C"]:  # 讀取C欄所有資料，並列印出來
    print(cell.value, end = " ")
print()

print("讀取 第 4 列的所有資料")
for cell in sheet["4"]:  # 讀取第2列所有資料，並列印出來
    print(cell.value, end = " ")
print()

print("------------------------------")  # 30個

print("顯示資料 方法八")

filename_r = "data/python_ReadWrite_EXCEL.xlsx"
workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("excel活動工作表： ", sheet)

select_data = sheet["A2":"D7"]
for a, b, c, d in select_data:
    print("{0} {1} {2} {3}".format(a.value, b.value, c.value, d.value))
print()

print('sheet.dimensions', sheet.dimensions)

for a, b, c, d in sheet[sheet.dimensions]:
    print(a.value, b.value, c.value, d.value)

print("------------------------------")  # 30個

print("openpyxl test 03 循欄列印 ＆ 循列列印")

for cell in list(sheet.columns)[0]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.columns)[1]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.columns)[2]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.columns)[3]:
    print(cell.value, end = " ")
print()

print("------------------------------")  # 30個

for cell in list(sheet.rows)[0]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.rows)[1]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.rows)[2]:
    print(cell.value, end = " ")
print()

for cell in list(sheet.rows)[3]:
    print(cell.value, end = " ")
print()


print("------------------------------")  # 30個

print("openpyxl test 04 讀取指定區域內容")

for row in sheet["A2":"D5"]:
    for cell in row:
        print(cell.value, end=" ")
    print()

print("------------------------------------------------------------")  # 60個

workbook = openpyxl.load_workbook(filename_r)
sheet = workbook.active

print('印出整個工作表1')
i = 0
for row in sheet:
    print('第', i, 'row', end = " : ")
    i += 1
    for cell in row:
        print(cell.value, end = " ")
    print()
print()

print('印出整個工作表2')
i = 0
for row in range(1, sheet.max_row+1):
    print('第', i, 'row', end = " : ")
    i += 1
    for col in range(1, sheet.max_column+1):
        print(sheet.cell(row,col).value, end = " ")
    print()
print()

print('印出工作表部分資料1')
i = 0
for rows in sheet["B2":"C3"]:
    for cell in rows:
        print(cell.value, end = " ")
    print()
print()

print('印出工作表部分資料2')

getted_list = []
i = 0
for rows in sheet.iter_rows(min_row=2, min_col=2, max_row=3, max_col=3):
    print('第', i, 'row', end = " : ")
    for cell in rows:
        print(cell.value, end = ' ')
    print()
print()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename_r = "data/python_ReadWrite_EXCEL.xlsx"

"""
#開啟舊檔 + 參數
workbook = openpyxl.load_workbook(filename_r, data_only=True)  # 要excel開啟才可以看到值，否則會顯示None
workbook = openpyxl.load_workbook(filename_r, data_only=False) # 要excel開啟才可以看到值，否則會顯示None
"""

workbook = openpyxl.load_workbook(filename_r)

results = []

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

for row in sheet.iter_rows():
    results.append([cell.value for cell in row])

#print(results)
for _ in results:
    print(_)

print("------------------------------")  # 30個

workbook = openpyxl.load_workbook(filename_r)

sheets = workbook.sheetnames
print(sheets)

for i in range(len(sheets)):
    sheet = workbook[sheets[i]]
    print('title', sheet.title)
    for col in sheet.iter_cols(min_row=0, min_col=0, max_row=3, max_col=3):
        for cell in col:
            print(cell.value, end = " ")
    print()

print("------------------------------")  # 30個

for row in range(2, 7):  # 第 2~6 ROW
    for col in range(65, 70): # 65~69 A~E
        cell_index = chr(col) + str(row)
        print(sheet[cell_index].value, end='\t')
    print()

print("------------------------------------------------------------")  # 60個

for i in range(2, sheet.max_row+1):
    sheet.row_dimensions[i].height = 18
    for j in range(3, sheet.max_column+1):
        print(sheet.cell(row=i,column=j).value, end = " ")
    print()
        
print("------------------------------------------------------------")  # 60個

sys.exit()

""" CSV 轉 EXCEL
import csv
data_rows = [fields for fields in csv.reader(open("animals.csv"))]

sheet = workbook.active
for row in data_rows:
    sheet.append(row)

workbook.save("temp_data_02.xlsx")
"""

print("------------------------------------------------------------")  # 60個

workbook = openpyxl.load_workbook(filename_r, data_only=True)  # 設定 data_only=True 只讀取計算後的數值

print("修改目前工作表")

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("excel活動工作表： ", workbook.active)

workbook.active = 0
print("excel活動工作表： ", workbook.active)

print("隱藏/取消隱藏工作表")
sheet = workbook["animals2"]
sheet.sheet_state = "hidden"
# sheet = workbook['BBB']
# sheet.sheet_state = 'visible'

print("刪除工作表")
sheet = workbook["animals1"]
workbook.remove(sheet)

print("複製工作表")
sheet = workbook["animals2"]
target = workbook.copy_worksheet(sheet)
target.title = "new_animals2"

workbook.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)


"""
print("------------------------------------------------------------")  # 60個

所有的修改都只是針對記憶體中的excel檔
只有save才會把修改的內容寫到儲存媒體上

print("------------------------------------------------------------")  # 60個

print("建立大綱並折疊")
sheet.column_dimensions.group("A", "D", hidden=True)
sheet.row_dimensions.group(1, 10, hidden=True)

print("------------------------------------------------------------")  # 60個

print("改變字體 ＆ 加上註解")
sheet["A1"].font = openpyxl.styles.Font(name="Courier", size=24, color="FF0000")
sheet["A2"].comment = openpyxl.comments.Comment(text="這是註解", author="Amos")

print(sheet["A2"].comment.text)
print(sheet["A2"].comment.author)

sheet["A2"].comment = None  # 取消註解 不能無此行

print("------------------------------------------------------------")  # 60個

print('新增列在第4列')
sheet.insert_rows(4)

print('新增欄在第3欄, 插入兩欄')
sheet.insert_cols(3, 2)

print('刪除列 刪除第4列 刪除2列')
sheet.delete_rows(4, 2)

print('刪除欄 刪除第3欄 刪除2欄')
sheet.delete_cols(3, 2)

print("------------------------------------------------------------")  # 60個

print("鎖定、解除鎖定")

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
# sheet.freeze_panes = 'B2'
sheet.freeze_panes = None

print("------------------------------------------------------------")  # 60個

設定粗體
sheet.cell(row=i,column=j).font = Font(bold=True)

#千分位樣式
sheet.cell(row=i,column=j).number_format = "#,##0"

#固定為第1列、第2欄
sheet.freeze_panes = "C2"

#隱藏A欄
#sheet.column_dimensions["A"].hidden=False

print("------------------------------------------------------------")  # 60個


"""



print("------------------------------------------------------------")  # 60個
""" write excel
# color_scale.py

from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule
from openpyxl.formatting.rule import ColorScaleRule

workbook = openpyxl.Workbook()
sheet = workbook.active

values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 55]

# A欄 Sugar可看出漸層效果  Kilo看不出效果
for i, value in enumerate(values):
    sheet.cell(i + 1, 1 ).value = value

two_color_scale = ColorScaleRule(        
    start_type="min", start_color="FF0000",
    end_type="max", end_color="FFFFFF"
)

sheet.conditional_formatting.add("A1:A10", two_color_scale)

print("------------------------------")  # 60個

# C欄

for i, value in enumerate(values):
    sheet.cell(i + 1, 3).value = value

less_than_rule = CellIsRule( 
    operator="lessThan",
    formula=[100],
    stopIfTrue=True,
    fill=PatternFill("solid", start_color="FF0000", end_color="FF0000")
)
sheet.conditional_formatting.add("C1:C10", less_than_rule)

workbook.save("tmp_01_fill_red.xlsx")
"""

