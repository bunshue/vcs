"""
讀寫 Excel 檔案, 使用 openpyxl

python讀取/修改excel

pip3 install openpyxl

專有名詞

workbook（活頁簿）：也就是一個excel檔案
worksheet（工作表）：一個excel可以有很多個工作表，目前正在觀看或處理的工作表又稱作「活動中的工作表（active sheet）」
欄（column）：工作表中的直欄，以A、B、C…代表
行（row）：工作表中的橫列，以1、2、3…代表
儲存格（cell）：工作表中的每一個都是一個儲存格

"""

import os
import sys
import time
import openpyxl

print("------------------------------------------------------------")  # 60個

print("openpyxl test 01 通用訊息")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
print("所有工作表名稱 :", workbook.sheetnames)

names = workbook.sheetnames  # 讀取 excel檔案 裏所有工作表名稱
print("所有工作表名稱 :", names)

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 取得最後編輯的那個工作表
# sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# 取得工作表參數
sheet_name = sheet.title
ROW = sheet.max_row
COL = sheet.max_column
print("此工作表名稱、總列數、總行數 :", sheet_name, ROW, COL)

# 取得第 0 個工作表 same
sheet = workbook[workbook.sheetnames[0]]
print("此工作表名稱 :", sheet.title)

s1 = workbook["exam1"]  # 取得工作表名稱為「工作表1」的內容
s2 = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數")
print(s1.title, s1.max_row, s1.max_column)
print(s2.title, s2.max_row, s2.max_column)

print(s2.sheet_properties)  # 印出工作表屬性

from openpyxl.utils import get_column_letter, column_index_from_string

print(column_index_from_string("A"))  # 1
print(column_index_from_string("Z"))  # 26
print(column_index_from_string("AA"))  # 27
print(column_index_from_string("ZZ"))  # 702

print(get_column_letter(5))  # E
print(get_column_letter(100))  # CV

print("------------------------------------------------------------")  # 60個
print("openpyxl test 02 讀取 excel 檔案")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
print("所有工作表名稱 :", workbook.sheetnames)

names = workbook.sheetnames  # 讀取 excel檔案 裏所有工作表名稱
print("所有工作表名稱 :", names)

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 取得最後編輯的那個工作表
# sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# 取得工作表參數
sheet_name = sheet.title
ROW = sheet.max_row
COL = sheet.max_column
print("此工作表名稱、總列數、總行數 :", sheet_name, ROW, COL)

# 取得第 0 個工作表 same
sheet = workbook[workbook.sheetnames[0]]
print("此工作表名稱 :", sheet.title)

print("------------------------------")  # 30個
print("顯示資料 方法一")

"""
#修改資料
sheet['B3'] = 'Chris' 
"""

print("使用cell方法取得資料")
sheet1 = workbook["exam1"]
sheet2 = workbook["exam2"]

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
print("顯示資料 方法三")

for sheet in workbook:
    print("sheet", sheet)
    for row in sheet:
        # print('row')
        for cell in row:
            print(cell.value, end=" ")
        print()
    print()

print("------------------------------")  # 30個
print("顯示資料 方法四")

try:
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
except:
    print("程式執行失敗。")

print("------------------------------")  # 30個
print("顯示資料 方法五")

workbook = openpyxl.load_workbook(
    filename_r, data_only=True
)  # 設定 data_only=True 只讀取計算後的數值
print("所有工作表名稱 :", workbook.sheetnames)

s1 = workbook["exam1"]
s2 = workbook["exam2"]


def get_values(sheet):
    arr = []  # 第一層串列
    for row in sheet:
        arr2 = []  # 第二層串列
        for column in row:
            arr2.append(column.value)  # 寫入內容
        arr.append(arr2)
    return arr


print("印出工作表1 所有內容")
print(get_values(s1))

print("印出工作表2 所有內容")
print(get_values(s2))

print("------------------------------")  # 30個
print("顯示資料 方法六")

workbook = openpyxl.load_workbook(
    filename_r, data_only=True
)  # 設定 data_only=True 只讀取計算後的數值
print("所有工作表名稱 :", workbook.sheetnames)

s1 = workbook["exam1"]
v = s1.iter_rows(min_row=1, min_col=1, max_col=5, max_row=4)  # 取出四格內容
print(v)
for i in v:
    for j in i:
        print(j.value, end=" ")
    print()

print("------------------------------------------------------------")  # 60個

print("建立多工作表之Excel活頁簿")

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

# 預設為名為Sheet之工作表

workbook.create_sheet("工作表3")  # 插入工作表 3 在最後方
workbook.create_sheet("工作表1.5", 1)  # 插入工作表 1.5 在第二個位置 ( 工作表 1 和 2 的中間 )
workbook.create_sheet("工作表0", 0)  # 插入工作表 0 在第一個位置
workbook.create_sheet("工作表aa")  # 插入工作表aa 在最後方
workbook.create_sheet("工作表bb")  # 插入工作表bb 在最後方

# 將工作表的頁箋著色
s1 = workbook["工作表aa"]  # 開啟工作表aa
s2 = workbook["工作表bb"]  # 開啟工作表bb
s1.sheet_properties.tabColor = "ff0000"  # 修改工作表 1 頁籤顏色為紅色
s2.sheet_properties.tabColor = "ffff00"  # 修改工作表 2 頁籤顏色為黃色

workbook.copy_worksheet(s1)  # 複製工作表aa 放到最後方

# 修改工作表的名稱
s1.title = "new title111"  # 修改工作表aa 的名稱為 new title111
s2.title = "new title222"  # 修改工作表bb 的名稱為 new title222

filename_w = "tmp_excel_openpyxl01.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 01 建立excel檔案 xlsx a")

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 修改工作表的名稱
sheet.title = "Animal"

# 以儲存格位置寫入資料, 直接修改/設定工作表內的資料
sheet["A1"] = "中文名"
sheet["B1"] = "英文名"
sheet["C1"] = "體重"
sheet["D1"] = "全名"

""" same
listtitle=['中文名', '英文名', '體重', '全名']
sheet.append(listtitle)  
"""

# 以串列寫入資料
animal01 = ["鼠", "mouse", "3"]
animal02 = ["牛", "ox", "48"]
animal03 = ["虎", "tiger", "33"]
animal04 = ["兔", "rabbit", "8"]
sheet.append(animal01)  # 逐筆添加到最後一列
sheet.append(animal02)  # 逐筆添加到最後一列
sheet.append(animal03)  # 逐筆添加到最後一列
sheet.append(animal04)  # 逐筆添加到最後一列

# 設定格式
# sheet = workbook["Animal"]
sheet["A1"].fill = openpyxl.styles.PatternFill(
    fill_type="solid", fgColor="FFFF00"
)  # 設定 f1 儲存格的背景樣式
sheet["B1"].font = openpyxl.styles.Font(
    name="Arial", color="ff0000", size=30, bold=True
)  # 設定 g1 儲存格的文字樣式
sheet["C1"].font = openpyxl.styles.Font(
    name="Arial", color="00ff00", size=30, bold=True
)  # 設定 g1 儲存格的文字樣式
sheet["D1"].font = openpyxl.styles.Font(
    name="Arial", color="0000ff", size=30, bold=True
)  # 設定 g1 儲存格的文字樣式

# 使用.cell()填入資料
c = sheet.cell(7, 1)
c.value = "第7列,第1欄"
c.font = openpyxl.styles.Font(size=24, color="0000CC")  # 設定儲存格的文字大小與文字顏色
c.fill = openpyxl.styles.PatternFill("solid", fgColor="66CCFF")  # 設定儲存格的背景色

c = sheet.cell(7, 4)
c.value = "第7列,第4欄"
c.font = openpyxl.styles.Font(size=24, color="0000CC")
c.fill = openpyxl.styles.PatternFill("solid", fgColor="66CCFF")

# 設定欄寬
sheet.column_dimensions["A"].width = 30  # 設定A欄欄寬
sheet.column_dimensions["B"].width = 15  # 設定B欄欄寬
sheet.column_dimensions["C"].width = 15  # 設定C欄欄寬
sheet.column_dimensions["D"].width = 30  # 設定D欄欄寬

# 設定列高
sheet.row_dimensions[2].height = 50  # 設定第2列列高
sheet.row_dimensions[5].height = 50  # 設定第5列列高

filename_w = "tmp_excel_openpyxl02.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 01 建立excel檔案 xlsx b")

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

s3 = workbook.create_sheet("工作表3")  # 新增工作表 3
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 二維陣列資料
for i in data:
    s3.append(i)  # 逐筆添加到最後一列

filename_w = "tmp_excel_openpyxl03.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print("openpyxl test 11 讀 寫")
filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(
    filename_r, data_only=True
)  # 設定 data_only=True 只讀取計算後的數值
print("所有工作表名稱 :", workbook.sheetnames)

s2 = workbook["exam2"]  # 開啟工作表 2
data = [[1, 2], [3, 4]]  # 二維陣列資料
for y in range(len(data)):
    for x in range(len(data[y])):
        row = 2 + y  # 寫入資料的範圍從 row=2 開始
        col = 2 + x  # 寫入資料的範圍從 column=2 開始
        s2.cell(row, col).value = data[y][x]

filename_w = "tmp_excel_openpyxl04.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print("openpyxl test 12 讀 寫")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(
    filename_r, data_only=True
)  # 設定 data_only=True 只讀取計算後的數值
print("所有工作表名稱 :", workbook.sheetnames)

s2 = workbook["exam2"]
s2["d1"] = "=sum(a1:c1)"  # 寫入公式
s2["d2"] = "=sum(a2:c2)"  # 寫入公式
s2["d3"] = "=sum(a3:c3)"  # 寫入公式
s2["d4"] = "=sum(a4:c4)"  # 寫入公式
s2["d5"] = "=sum(a5:c5)"  # 寫入公式

filename_w = "tmp_excel_openpyxl05.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 13 讀 寫")
print("從檔案後面附加資料")

filename_w = "tmp_excel_openpyxl06.xlsx"

if not os.path.exists(filename_w):
    workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
    sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
    heading = ["中文名", "英文名", "體重", "全名"]
    sheet.append(heading)
    workbook.save(filename_w)

workbook = openpyxl.load_workbook(filename_w)
print("所有工作表名稱 :", workbook.sheetnames)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

animal01 = ["鼠", "mouse", "3", "米老鼠"]
sheet.append(animal01)

workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print("openpyxl test 14")
# 創建Excel文件

# 這個有問題

from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

data = [["1001", "白元芳", "男", "13123456789"], ["1002", "白潔", "女", "13233445566"]]
sheet.append(["學號", "姓名", "性別", "電話"])
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")
tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=True,
)
#sheet.add_table(tab) 問題在這裡

filename_w = "tmp_excel_openpyxl07_全班學生數據.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print("openpyxl test 16")
from openpyxl.chart import RadarChart, Reference

print("在excel檔案內加入雷達圖")

filename_r = "data/radar_chart.xlsx"
workbook = openpyxl.load_workbook(filename_r)
print("所有工作表名稱 :", workbook.sheetnames)

sh = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

data = Reference(sh, min_col=2, max_col=4, min_row=1, max_row=sh.max_row)
labels = Reference(sh, min_col=1, min_row=2, max_row=sh.max_row)

chart = RadarChart()
# 預設為standard
# filled為填色
# chart.type = "filled"
chart.title = "各部門業績"
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)

sh.add_chart(chart, "F2")

filename_w = "tmp_excel_openpyxl08_add_radar_chart.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

import calendar

year = 2024
month = 5
dayname = ["日", "一", "二", "三", "四", "五", "六"]


# 【在Excel檔新增月曆的函數】
def makecalendar(value1, value2):
    year = int(value1)
    month = int(value2)
    savefile = "tmp_excel_openpyx_" + str(year) + "_" + str(month) + "a.xlsx"

    cal = calendar.Calendar(calendar.SUNDAY)
    workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
    sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
    c = sheet.cell(1, 4)
    c.value = str(year) + "年" + str(month) + "月"
    for col in range(7):  # 一週的每一天
        c = sheet.cell(2, col + 1)
        c.value = dayname[col]
    for col, week in enumerate(cal.monthdayscalendar(year, month)):
        for row, day in enumerate(week):
            if day > 0:
                c = sheet.cell((col + 3), row + 1)
                c.value = day
    workbook.save(savefile)  # Excel轉存檔案
    return "轉存" + savefile + "了。"


msg = makecalendar(year, month)
print(msg)

print("------------------------------------------------------------")  # 60個

import calendar

value1 = "2024"
value2 = "5"
dayname = ["日", "一", "二", "三", "四", "五", "六"]

fontN = openpyxl.styles.Font(size=24)
fontB = openpyxl.styles.Font(size=24, color="0000FF")
fontR = openpyxl.styles.Font(size=24, color="FF0000")
fillB = openpyxl.styles.PatternFill(patternType="solid", fgColor="AAAAFF")
fillR = openpyxl.styles.PatternFill(patternType="solid", fgColor="FFAAAA")


# 【在Excel檔新增月曆的函數】
def makecalendar(value1, value2):
    year = int(value1)
    month = int(value2)
    savefile = "tmp_excel_openpyx_" + str(year) + "_" + str(month) + "b.xlsx"

    cal = calendar.Calendar(calendar.SUNDAY)
    workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
    sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
    for c in ["A", "B", "C", "D", "E", "F", "G"]:
        sheet.column_dimensions[c].width = 20
    c = sheet.cell(1, 4)
    c.value = str(year) + "年" + str(month) + "月"
    c.font = fontN
    for row in range(7):
        c = sheet.cell(2, row + 1)
        c.value = dayname[row]
        c.font = fontN
        c.alignment = openpyxl.styles.Alignment("center")
        if row == 6:
            c.font = fontB
            c.fill = fillB
        if row == 0:
            c.font = fontR
            c.fill = fillR
    for col, week in enumerate(cal.monthdayscalendar(year, month)):
        sheet.row_dimensions[col + 3].height = 50
        for row, day in enumerate(week):
            if day > 0:
                c = sheet.cell((col + 3), row + 1)
                c.value = day
                c.font = fontN
                if row == 6:
                    c.font = fontB
                if row == 0:
                    c.font = fontR
    workbook.save(savefile)  # Excel轉存檔案
    return "轉存" + savefile + "了。"


msg = makecalendar(value1, value2)
print(msg)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import pathlib  # 標準函式庫
import openpyxl  # 外部函式庫　pip install openpyxl
import csv  # 標準函式庫
workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

list_row = 1
path = pathlib.Path("data\sales")  # 指定相對路徑
for pass_obj in path.iterdir():
    if pass_obj.match("*.xlsx"):
        print(pass_obj)
        workbook = openpyxl.load_workbook(pass_obj)
        for sh in workbook:
            for dt_row in range(9, 19):
                if sh.cell(dt_row, 2).value != None:
                    # 更便於說明的代碼
                    # sheet.cell(row=list_row, column=1).value = \
                    #    sh.cell(row=2, column=7).value   #傳票NO
                    sheet.cell(list_row, 1).value = sh.cell(2, 7).value  # 傳票NO
                    sheet.cell(list_row, 2).value = sh.cell(3, 7).value  # 日期
                    sheet.cell(list_row, 3).value = sh.cell(4, 3).value  # 客戶代碼
                    sheet.cell(list_row, 4).value = sh.cell(3, 2).value.strip(
                        "敬啟"
                    )  # 客戶名稱
                    sheet.cell(list_row, 5).value = sh.cell(7, 8).value  # 負責人代碼
                    sheet.cell(list_row, 6).value = sh.cell(7, 7).value  # 負責人姓名
                    sheet.cell(list_row, 7).value = sh.cell(dt_row, 1).value  # No
                    sheet.cell(list_row, 8).value = sh.cell(dt_row, 2).value  # 商品代碼
                    sheet.cell(list_row, 9).value = sh.cell(dt_row, 3).value  # 商品名稱
                    sheet.cell(list_row, 10).value = sh.cell(dt_row, 4).value  # 數量
                    sheet.cell(list_row, 11).value = sh.cell(dt_row, 5).value  # 單價
                    sheet.cell(list_row, 12).value = (
                        sh.cell(dt_row, 4).value * sh.cell(dt_row, 5).value
                    )  # 金額
                    sheet.cell(list_row, 13).value = sh.cell(dt_row, 7).value  # 備註
                    list_row += 1

workbook.save("tmp_salesList3333.xlsx")


print("------------------------------------------------------------")  # 60個


# 新進

print("------------------------------------------------------------")  # 60個


"""
保留

sheet = workbook.create_sheet("animal")  # 建立新工作表 名為animal

for row in range(2, 7):  # 第 2~6 ROW
    for col in range(65, 70): # 65~69 A~E
        cell_index = chr(col) + str(row)
        print(sheet[cell_index].value, end='\t')
    print()

"""

print("------------------------------------------------------------")  # 60個

print("新增空白excel")

filename_w = "tmp_excel_openpyxl11.xlsx"

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("新增工作表並指定放置位置")

filename_w = "tmp_excel_openpyxl12.xlsx"

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
workbook.create_sheet("Mysheet1", 1)  # 新增工作表並指定放置位置
workbook.create_sheet("Mysheet0", 0)

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個


print("修改工作表名稱")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_a.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam1"]
sheet.title = "第一次月考"

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("修改工作表顏色")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_b.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
sheet.sheet_properties.tabColor = "ff0000"

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("隱藏/取消隱藏工作表")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_c.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam2"]
sheet.sheet_state = "hidden"

# sheet = workbook['BBB']
# sheet.sheet_state = 'visible'

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("修改目前工作表")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("excel活動工作表： ", workbook.active)

workbook.active = 0
print("excel活動工作表： ", workbook.active)


from openpyxl.utils import get_column_letter, column_index_from_string

workbook = openpyxl.load_workbook(filename_r)
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("目前工作表： ", workbook.active.title)

workbook.active = workbook["exam2"]
print("目前工作表： ", workbook.active.title)

print("------------------------------------------------------------")  # 60個

print("複製工作表")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_d_copy.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam2"]
target = workbook.copy_worksheet(sheet)
target.title = "new_exam2"
workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("刪除工作表")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_e.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam1"]
workbook.remove(sheet)
workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("讀取工作表所有內容")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print("excel活動工作表： ", sheet)


for row in sheet:
    for cell in row:
        print(cell.value)

print()
print("D1內容： ", sheet["D1"].value)


filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(filename_r)
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

range = sheet["A1":"B6"]

for a, b in range:
    print("{0} {1}".format(a.value, b.value))
print()
""" fail
for a, b, c in sheet[sheet.dimensions]:
    print(a.value, b.value, c.value)
"""
print("------------------------------------------------------------")  # 60個

print("寫入儲存格")
"""
所有的修改都只是針對記憶體中的excel檔
只有save才會把修改的內容寫到儲存媒體上
"""

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_f.xlsx"

workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("B2內容： ", sheet["B2"].value)

sheet["B2"].value = 20
print("B2內容： ", sheet["B2"].value)

sheet.cell(column=2, row=3).value = 999

workbook.save(filename_w)  # 若給予不同檔名代表另存新檔的意思

print("------------------------------------------------------------")  # 60個

print("顯示最大、最小 欄數、列數")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print("儲存格 欄名", sheet["A1"].column)
print("儲存格 列名", sheet["A1"].row)
print("儲存格名", sheet["A1"].coordinate)

print("工作表有資料最大欄數", sheet.max_column)
print("工作表有資料最小欄數", sheet.min_column)
print("工作表有資料最大列數", sheet.max_row)
print("工作表有資料最小列數", sheet.min_row)

print("------------------------------------------------------------")  # 60個

print("循欄列印 ＆ 循列列印")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(
    filename_r, data_only=True
)  # 要excel開啟才可以看到值，否則會顯示None

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

for cell in list(sheet.columns)[1]:
    print(cell.value)

print()
for cell in list(sheet.rows)[1]:
    print(cell.value)

print("------------------------------------------------------------")  # 60個

print("欄名 vs 欄數 轉換")
""" fail
filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

from openpyxl.utils import get_column_letter, column_index_from_string

workbook = openpyxl.load_workbook(filename_r, data_only=False) # 要excel開啟才可以看到值，否則會顯示None

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

for i in range(1, sheet.max_column+1):
    print(i, ' = ', get_column_letter(i))

print("A = ", column_index_from_string('A'))
print("B = ", column_index_from_string('B'))
"""
print("------------------------------------------------------------")  # 60個

print("讀取指定區域內容")

from openpyxl.utils import get_column_letter, column_index_from_string

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(
    filename_r, data_only=False
)  # 要excel開啟才可以看到值，否則會顯示None

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

for row in sheet["A2":"D5"]:
    for cell in row:
        print(cell.value, end=" ")
    print()

print("------------------------------------------------------------")  # 60個

print("新增工作表 ＆ 修改工作表名稱")

from openpyxl.utils import get_column_letter, column_index_from_string

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_g.xlsx"

workbook = openpyxl.load_workbook(
    filename_r, data_only=False
)  # 要excel開啟才可以看到值，否則會顯示None

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet.title = "hello"
workbook.create_sheet("新工作表")
workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("新增、修改、刪除工作表")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_h.xlsx"

workbook = openpyxl.load_workbook(filename_r)

workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# 新增工作表，若名稱已經存在則原本名稱之後加數字
workbook.create_sheet(title="amos")

# 修改工作表
workbook["amos"].title = "carol"

# 刪除工作表
workbook.remove(workbook["carol"])

workbook.save(filename_w)


workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam1"]

for cell in sheet["C"]:  # 讀取C欄所有資料，並列印出來
    print(cell.value)

for cell in sheet["2"]:  # 讀取第2列所有資料，並列印出來
    print(cell.value)

print("------------------------------------------------------------")  # 60個

print("合併、解除合併儲存格")
""" fail
filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_i.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# sheet.merge_cells('A5:D9')
# sheet.unmerge_cells('A5:D9')

# or equivalently
# sheet.merge_cells(start_row=5, start_column=1, end_row=9, end_column=4)
sheet.unmerge_cells(start_row=5, start_column=1, end_row=9, end_column=4)

workbook.save(filename_w)
"""
print("------------------------------------------------------------")  # 60個

print("插入圖片")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_j_pic.xlsx"

from openpyxl.drawing.image import Image

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = Image(filename)
sheet.add_image(img, "B5")  # 把圖貼在B5

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("建立大綱並折疊")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_k.xlsx"

from openpyxl.drawing.image import Image

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet.column_dimensions.group("A", "D", hidden=True)
sheet.row_dimensions.group(1, 10, hidden=True)

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("改變字體 ＆ 加上註解")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_l.xlsx"

from openpyxl.styles import Font
from openpyxl.comments import Comment

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet["A1"].font = Font(name="Courier", size=24, color="FF0000")
sheet["A2"].comment = Comment(text="這是註解", author="Amos")

print(sheet["A2"].comment.text)
print(sheet["A2"].comment.author)

sheet["A2"].comment = None  # 取消註解

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("新增/刪除 欄、列")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_m.xlsx"

from openpyxl.styles import Font

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# sheet.insert_rows(1)
# sheet.insert_cols(1, 2)
sheet.delete_rows(1, 2)
sheet.delete_cols(1, 2)

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("畫統計圖(openpyxl範例)")

# 官方範例

from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference

workbook = Workbook(write_only=True)
sheet = workbook.create_sheet()

rows = [
    ("Number", "Batch 1", "Batch 2"),
    (2, 10, 30),
    (3, 40, 60),
    (4, 50, 70),
    (5, 20, 10),
    (6, 10, 40),
    (7, 50, 30),
]


for row in rows:
    sheet.append(row)


chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "Bar Chart"
chart1.y_axis.title = "Test number"
chart1.x_axis.title = "Sample length (mm)"

data = Reference(sheet, min_col=2, min_row=1, max_row=7, max_col=3)
cats = Reference(sheet, min_col=1, min_row=2, max_row=7)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
chart1.shape = 4
sheet.add_chart(chart1, "A10")

from copy import deepcopy

chart2 = deepcopy(chart1)
chart2.style = 11
chart2.type = "bar"
chart2.title = "Horizontal Bar Chart"

sheet.add_chart(chart2, "G10")


chart3 = deepcopy(chart1)
chart3.type = "col"
chart3.style = 12
chart3.grouping = "stacked"
chart3.overlap = 100
chart3.title = "Stacked Chart"

sheet.add_chart(chart3, "A27")


chart4 = deepcopy(chart1)
chart4.type = "bar"
chart4.style = 13
chart4.grouping = "percentStacked"
chart4.overlap = 100
chart4.title = "Percent Stacked Chart"

sheet.add_chart(chart4, "G27")

filename_w = "tmp_excel_openpyxl13_EXCEL1_bar.xlsx"
workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("鎖定、解除鎖定")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_o.xlsx"

from openpyxl.styles import Alignment

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

# sheet.freeze_panes = 'B2'
sheet.freeze_panes = None

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("設定日期格式")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_p.xlsx"

import datetime

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam1"]
sheet["A1"] = datetime.datetime(2010, 7, 21)

# sheet['A1'].number_format = 'yyyy-mm-dd h:mm:ss'
# sheet['A1'].number_format = 'yyyy-mm-dd'
sheet["A1"].number_format = "dd-mm-yyyy"

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("設定公式")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_formula.xlsx"

import datetime

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook["exam2"]
# sheet['A1'] = 6
# sheet['A2'] = 10
sheet["F1"] = "總分"
sheet["F2"] = "=SUM(B2:E2)"
sheet["F3"] = "=SUM(B3:E3)"
sheet["F4"] = "=SUM(B4:E4)"
sheet["F5"] = "=SUM(B5:E5)"
sheet["F6"] = "=SUM(B6:E6)"

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個

print("移動資料")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"
filename_w = "tmp_excel_openpyxl13_EXCEL1_r.xlsx"

workbook = openpyxl.load_workbook(filename_r)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet.move_range("B4:E6", rows=1, cols=4)  # 區塊向下移1 向右移4

workbook.save(filename_w)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

""" 暫存文字資料
workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet["A" + str(row)].value = person_data["name"]
sheet["B" + str(row)].value = person_data["quantity"]
sheet["C" + str(row)].value = person_data["amount"]
sheet["D" + str(row)].value = customer_data["name"]
sheet["E" + str(row)].value = customer_data["quantity"]
sheet["F" + str(row)].value = customer_data["amount"]

sheet["F" + str(row)].value =  "=SUM(F2:F" + str(row-1) + ")"
sheet["E" + str(row)].value =  "合計"

workbook.save("tmp_sales_aggregate222.xlsx")




print("顯示資料 方法七");

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s1 = workbook["exam1"]  # 開啟工作表 1
s1["A1"].value = "apple"  # 儲存格 A1 內容為 apple
s1["A2"].value = "orange"  # 儲存格 A2 內容為 orange
s1["A3"].value = "banana"  # 儲存格 A3 內容為 banana
s1.cell(1, 2).value = 100  # 儲存格 B1 內容 ( row=1, column=2 ) 為 100
s1.cell(2, 2).value = 200  # 儲存格 B2 內容 ( row=2, column=2 ) 為 200
s1.cell(3, 2).value = 300  # 儲存格 B3 內容 ( row=3, column=2 ) 為 300

filename_w = 'tmp_excel_openpyxl10.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)






#from openpyxl.styles import Font, PatternFill  # 載入 Font 和 PatternFill 模組




s1 = workbook["exam1"]
s1["A1"].fill = openpyxl.styles.PatternFill(fill_type="solid", fgColor="FFFF00")  # 設定 f1 儲存格的背景樣式
s1["B1"].font = openpyxl.styles.Font(name="Arial", color="ff0000", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
s1["C1"].font = openpyxl.styles.Font(name="Arial", color="00ff00", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
s1["D1"].font = openpyxl.styles.Font(name="Arial", color="0000ff", size=30, bold=True)  # 設定 g1 儲存格的文字樣式









21.3 Excel files

>>> from openpyxl import load_workbook
>>> workbook = load_workbook('temp_data_01.xlsx')
>>> results = []
>>> sheet = workbook.worksheets[0]
>>> for row in sheet.iter_rows():
...     results.append([cell.value for cell in row])
...  
>>> print(results)

[['Notes', 'State', 'State Code', 'Month Day, Year', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)', 'Min Temp for Daily Max Air Temp (F)', 'Max Temp for Daily Max Air Temp (F)', 'Avg Daily Max Heat Index (F)', 'Record Count for Daily Max Heat Index (F)', 'Min for Daily Max Heat Index (F)', 'Max for Daily Max Heat Index (F)', 'Daily Max Heat Index (F) % Coverage'], [None, 'Illinois', 17, 'Jan 01, 1979', '1979/01/01', 17.48, 994, 6, 30.5, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 02, 1979', '1979/01/02', 4.64, 994, -6.4, 15.8, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 03, 1979', '1979/01/03', 11.05, 994, -0.7, 24.7, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 04, 1979', '1979/01/04', 9.51, 994, 0.2, 27.6, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 15, 1979', '1979/05/15', 68.42, 994, 61, 75.1, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 16, 1979', '1979/05/16', 70.29, 994, 63.4, 73.5, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 17, 1979', '1979/05/17', 75.34, 994, 64, 80.5, 82.6, 2, 82.4, 82.8, '0.20%'], [None, 'Illinois', 17, 'May 18, 1979', '1979/05/18', 79.13, 994, 75.5, 82.1, 81.42, 349, 80.2, 83.4, '35.11%'], [None, 'Illinois', 17, 'May 19, 1979', '1979/05/19', 74.94, 994, 66.9, 83.1, 82.87, 78, 81.6, 85.2, '7.85%']]




21.5.2 Writing Excel files

>>> import csv
>>> from openpyxl import Workbook
>>> data_rows = [fields for fields in csv.reader(open("temp_data_01.csv"))]
>>> workbook = Workbook()
>>> sheet = workbook.active
>>> sheet.title = "temperature data"
>>> for row in data_rows:
...     sheet.append(row)
... 
>>> workbook.save("temp_data_02.xlsx")




import openpyxl

workbook = openpyxl.load_workbook('tmp.xlsx')
sheets = workbook.sheetnames
print(sheets)
for i in range(len(sheets)):
    sheet = workbook[sheets[i]]
    print('title', sheet.title)
    for col in sheet.iter_cols(min_row=0, min_col=0, max_row=3, max_col=3):
        for cell in col:
            print(cell.value)








"""



print("讀取excel檔案每個工作表的名稱")

filename_r = "data/python_ReadWrite_EXCEL1.xlsx"

workbook = openpyxl.load_workbook(filename_r)

print(workbook.sheetnames)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print(workbook.active)
print(workbook.active.title)

print("------------------------------------------------------------")  # 60個


