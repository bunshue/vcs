"""
讀寫 Excel 檔案, 使用 xlrd(讀) xlwt(寫)

在新版python3.9中，windows中使用的更新删除了getiterator方法
sugar要先到
#C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/xlrd/xlsx.py
把兩個 getiterator() 改成 iter()

"""

import sys

import xlrd  # 讀 Excel 檔案
import xlwt  # 寫 Excel 檔案

print("------------------------------------------------------------")  # 60個

print("讀取excel檔案 1")
filename_r = "data/python_ReadWrite_EXCEL.xlsx"

# 讀取excel檔案成 活頁簿 Workbook 物件
workbook = xlrd.open_workbook(filename_r)

print("這個excel檔案的工作表頁數 :", len(workbook.sheets()))

print("工作表名稱:")
cc = workbook.sheet_names()
print(cc)

print("第0頁 內容")
sh0 = workbook.sheets()[0]
for row in range(sh0.nrows):
    print(sh0.row_values(row))

print("第1頁 內容")
sh1 = workbook.sheets()[1]
for row in range(sh1.nrows):
    print(sh1.row_values(row))

print("取出所有頁面")
sheets = workbook.sheets()
for sheet in sheets:
    print(sheet)
    for row in range(sheet.nrows):
        print(sheet.row_values(row))

print("取出所有頁面 至 字典格式")

scores = dict()
for sheet in sheets:
    rows = list()
    for i in range(sheet.nrows):
        row = dict()
        if i == 0:
            columns = sheet.row_values(i)
        else:
            for f, field in enumerate(sheet.row_values(i)):
                row[columns[f]] = field
            rows.append(row)
    scores[sheet.name] = rows

print(scores)

print("第0頁 內容")
sh0 = workbook.sheets()[0]
print("第0頁 ROW數 :", sh0.nrows)
print("第0頁 COL數 :", sh0.ncols)
ROW = sh0.nrows
COL = sh0.ncols
print(sh0.cell(3, 0).value)
for i in range(0, ROW):
    print(
        sh0.cell(i, 0).value,
        sh0.cell(i, 1).value,
        sh0.cell(i, 2).value,
        sh0.cell(i, 3).value,
    )

# 已知工作表的名稱
# sh0 = workbook.sheets("Sheet5")

print("------------------------------------------------------------")  # 60個

print("讀取excel檔案 2")
filename_r = "data/python_ReadWrite_EXCEL.xlsx"

# 讀取excel檔案成 活頁簿 Workbook 物件
workbook = xlrd.open_workbook(filename_r)

print("這個excel檔案的工作表頁數 :", len(workbook.sheets()))

print("取出所有工作表, 看rows")
for n in range(len(workbook.sheet_names())):
    sheet = workbook.sheets()[n]

    for i in range(sheet.nrows):
        print("Page {}: ".format(n), end="")
        print(sheet.row_values(i))

# workbook.sheets()[n] 可以指定我們要讀第幾個工作表，在這裡 n 便是我工作表的 index。
# sheet.nrows 可以顯示我列數有幾列，在這裡我用 row_values(i) 將每一張工作表、每一列 print 出來。
# 當然，你要一行行地印出來也是可行的。

print("------------------------------------------------------------")  # 60個

print("讀取excel檔案 3")
filename_r = "data/python_ReadWrite_EXCEL.xlsx"

# 讀取excel檔案成 活頁簿 Workbook 物件
workbook = xlrd.open_workbook(filename_r)

print("取出所有工作表, 看columns")
for n in range(len(workbook.sheet_names())):
    sheet = workbook.sheets()[n]

    for i in range(sheet.ncols):
        print("Page {}: ".format(n), end="")
        print(sheet.col_values(i))

print("------------------------------------------------------------")  # 60個

print("用xlwt寫入xls檔案")

filename_w = "tmp_excel_xlwt1.xls"

datahead = ["中文名", "英文名", "體重"]

animal01 = ["鼠", "mouse", "3"]
animal02 = ["牛", "ox", "48"]
animal03 = ["虎", "tiger", "33"]
animal04 = ["兔", "rabbit", "8"]
animals = [animal01, animal02, animal03, animal04]

# 建立活頁簿
workbook = xlwt.Workbook()  # 建立活頁簿 Workbook 物件

# (從活頁簿物件)建立工作表物件 sh0
sh0 = workbook.add_sheet("第一頁", cell_overwrite_ok=True)

# 將資料寫入儲存格 工作表物件.write(row, col, data)

# 寫第1列 標題
sh0.write(0, 0, datahead[0])
sh0.write(0, 1, datahead[1])
sh0.write(0, 2, datahead[2])

# 寫第2列 鼠
sh0.write(1, 0, animals[0][0])
sh0.write(1, 1, animals[0][1])
sh0.write(1, 2, animals[0][2])

# 寫第3列 牛
sh0.write(2, 0, animals[1][0])
sh0.write(2, 1, animals[1][1])
sh0.write(2, 2, animals[1][2])

# 寫第4列 虎
sh0.write(3, 0, animals[2][0])
sh0.write(3, 1, animals[2][1])
sh0.write(3, 2, animals[2][2])

# 寫第5列 兔
sh0.write(4, 0, animals[3][0])
sh0.write(4, 1, animals[3][1])
sh0.write(4, 2, animals[3][2])

# (從活頁簿物件)建立工作表物件 sh1
sh1 = workbook.add_sheet("第二頁")  # 建立新工作表，設定名稱

for j in range(0, 5):  # 0~4 => A B C D E
    for i in range(10, 20):  # 10~19 => 11~20
        #          ROW COL Data
        sh1.write(i, j, 123)

# 儲存檔案
# 活頁簿 => Excel 檔案 wb.save(filename)
workbook.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
