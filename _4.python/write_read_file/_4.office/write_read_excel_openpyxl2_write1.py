"""
使用 openpyxl 寫入 Excel 檔案

pip3 install openpyxl

python讀取/修改excel

寫入檔案
1 建立新檔 簡易資料
2 建立新檔 完整資料 + 格式
2 建立新檔 多工作頁
3 建立新檔 寫入資料
4 建立新檔 寫入資料 加 格式
5 讀取檔案 修改、寫入資料
6 插入圖片 表格

"""

import os
import sys
import time
import openpyxl

print("------------------------------------------------------------")  # 60個

print("openpyxl test 01 建立多工作表之Excel活頁簿")

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

# 預設為名為Sheet之工作表

#新增工作表
workbook.create_sheet("工作表3")  # 插入工作表 3 在最後方
workbook.create_sheet("工作表1.5", 1)  # 插入工作表 1.5 在第二個位置 ( 工作表 1 和 2 的中間 )
workbook.create_sheet("工作表0", 0)  # 插入工作表 0 在第一個位置
workbook.create_sheet("工作表aa")  # 插入工作表aa 在最後方
workbook.create_sheet("工作表bb")  # 插入工作表bb 在最後方
workbook.create_sheet("Mysheet1", 1)  # 新增工作表並指定放置位置
workbook.create_sheet("Mysheet0", 0)

# 建立新工作表
sheet = workbook.create_sheet("新animal")  # 建立新工作表 名為 新animal
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 二維陣列資料
for i in data:
    sheet.append(i)  # 逐筆添加到最後一列

# 將工作表的頁箋著色
sheet1 = workbook["工作表aa"]  # 開啟工作表aa
sheet1.sheet_properties.tabColor = "ff0000"  # 修改工作表 1 頁籤顏色為紅色

sheet2 = workbook["工作表bb"]  # 開啟工作表bb
sheet2.sheet_properties.tabColor = "ffff00"  # 修改工作表 2 頁籤顏色為黃色

workbook.copy_worksheet(sheet1)  # 複製工作表aa 放到最後方

# 修改工作表的名稱
sheet1.title = "新工作表A"  # 修改工作表aa 的名稱為 新工作表A
sheet2.title = "新工作表B"  # 修改工作表bb 的名稱為 新工作表B

"""
# 新增工作表，若名稱已經存在則原本名稱之後加數字
workbook.create_sheet(title="amos")

# 修改工作表
workbook["amos"].title = "carol"

# 刪除工作表
workbook.remove(workbook["carol"])
"""

"""
print("openpyxl test 06 新增工作表 ＆ 修改工作表名稱")
workbook.active = 0
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
"""

filename_w = "tmp_excel_openpyxl_a_sheet.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 02a 建立新檔, 簡易資料")
print("開啟空白的活頁簿")
workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

"""
print("openpyxl test 02b 開啟舊檔, 修改資料, 存檔, 或另存新檔")
filename_r = "data/python_ReadWrite_EXCEL.xlsx"
print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
"""

print("開啟工作表")
# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 以儲存格位置寫入資料, 直接修改/設定工作表內的資料
sheet["A1"] = "中文名"
sheet["B1"] = "英文名"
sheet["C1"] = "體重"
sheet["D1"] = "全名"
sheet["A2"] = "鼠"
sheet["B2"] = "mouse"
sheet["C2"] = "3"
sheet["D2"] = "米老鼠"
sheet["A3"] = "牛"
sheet["B3"] = "ox"
sheet["C3"] = "48"
sheet["D3"] = "班尼牛"

filename_w = "tmp_excel_openpyxl_b1_new_simple.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 02c 建立新檔 完整資料 + 格式")
print("開啟空白的活頁簿")
workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

print("開啟工作表")
# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 以儲存格位置寫入資料, 直接修改/設定工作表內的資料
sheet["A1"] = "動物列表"
sheet["A3"] = "中文名"
sheet["B3"] = "英文名"
sheet["C3"] = "體重"
sheet["D3"] = "全名"

""" same
listtitle=['中文名', '英文名', '體重', '全名']
sheet.append(listtitle)  
"""

# 以串列寫入資料
animal01 = ["鼠", "mouse", 3]#直接使用數值, 這樣才可以計算
animal02 = ["牛", "ox", 48]
animal03 = ["虎", "tiger", 33]
animal04 = ["兔", "rabbit", 8]
sheet.append(animal01)  # 逐筆添加到最後一列
sheet.append(animal02)  # 逐筆添加到最後一列
sheet.append(animal03)  # 逐筆添加到最後一列
sheet.append(animal04)  # 逐筆添加到最後一列

# 使用.cell()填入資料 設定公式
sheet["C8"].value = "總體重"
sheet["C9"].value = "=SUM(C4:C7)" # 寫入公式

print("------------------------------")  # 30個

print("一次寫入一個二維陣列")
print("建立 二維串列, 裡面都是list")
animals_2d_list = [
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
    ["龍", "dragon", 38, "逗逗龍"],
    ["蛇", "snake", 16, "貪吃蛇"],
    ["馬", "horse", 31, "草泥馬"],
    ["羊", "goat", 29, "喜羊羊"],
    ["猴", "monkey", 22, "山道猴"],
    ["雞", "chicken", 5, "肯德雞"],
    ["狗", "dog", 17, "貴賓狗"],
    ["豬", "pig", 42, "佩佩豬"],
]
for y in range(len(animals_2d_list)):
    for x in range(len(animals_2d_list[y])):
        row = 13 + y  # 寫入資料的範圍從 row=13 開始
        col = 1 + x  # 寫入資料的範圍從 column=1 開始
        sheet.cell(row, col).value = animals_2d_list[y][x]

print("------------------------------")  # 30個

#移動資料位置
#sheet.move_range("A13:D24", rows=6, cols=4)  # 區塊向下移6格 向右移4格

print("------------------------------")  # 30個

print('使用數值與使用字串比較')
sheet.cell(10, 1).value = "使用數值"
sheet.cell(10, 2).value = 123  # 儲存格 B1 內容 ( row=12, column=1 ) 為 123
sheet.cell(10, 3).value = 456  # 儲存格 B2 內容 ( row=13, column=1 ) 為 456
sheet.cell(row=10, column=4).value = 789
sheet["E10"] = "總和"
sheet["F10"] = "=SUM(B10:D10)"  # 寫入公式

sheet.cell(11, 1).value = "使用字串"
sheet.cell(11, 2).value = str(123)  # 儲存格 B1 內容 ( row=12, column=2 ) 為 123
sheet.cell(11, 3).value = str(456)  # 儲存格 B2 內容 ( row=13, column=2 ) 為 456
sheet.cell(row=11, column=4).value = str(789)
sheet["E11"] = "總和"
#sheet["F11"] = "=SUM(B11:D11)"  # 寫入公式
sheet["F11"] = "不可對字串計算總和"

print("------------------------------")  # 30個

# 設定欄寬
sheet.column_dimensions["A"].width = 18  # 設定A欄欄寬
sheet.column_dimensions["B"].width = 18  # 設定B欄欄寬
sheet.column_dimensions["C"].width = 18  # 設定C欄欄寬
sheet.column_dimensions["D"].width = 18  # 設定D欄欄寬
sheet.column_dimensions["E"].width = 18  # 設定E欄欄寬

# 設定列高
sheet.row_dimensions[1].height = 30  # 設定第1列列高
sheet.row_dimensions[2].height = 30  # 設定第2列列高
sheet.row_dimensions[3].height = 30  # 設定第3列列高
sheet.row_dimensions[6].height = 30  # 設定第6列列高

print("------------------------------")  # 30個

#將 A1 B1 C1 D1 A2 B2 C2 D2 合併為一格

print("合併儲存格: 方法一")
print("合併儲存格 A1+B1+C1+D1+A2+B2+C2+D2 合成一格")
sheet.merge_cells('A1:D2')
#print("原本合併儲存格再解開")
#sheet.unmerge_cells('A1:D2')#解除合併儲存格

print("------------------------------")  # 30個
"""
print("合併儲存格: 方法二")
print("合併儲存格 A1+B1+C1+D1+A2+B2+C2+D2 合成一格")
sheet.merge_cells(start_row=1, start_column=1, end_row=2, end_column=4)
print("原本合併儲存格再解開")#解除合併儲存格
sheet.unmerge_cells(start_row=1, start_column=1, end_row=2, end_column=4)
"""
print("------------------------------")  # 30個

print("合併儲存格: 方法三")

print('合併儲存格的測試')
sheet["A28"] = "合併儲存格的測試"
sheet.merge_cells("A28:D31")
sheet["A28"].alignment = openpyxl.styles.Alignment(horizontal="center")
#sheet.unmerge_cells("A28:D31")

print("------------------------------")  # 30個

print("設定儲存格格式 字型 顏色 大小 背景色")
sheet.cell(1, 1).value = "動物列表"
sheet.cell(1, 1).font = openpyxl.styles.Font(size=24, color="0000CC")  # 設定儲存格的文字大小與文字顏色
sheet.cell(1, 1).fill = openpyxl.styles.PatternFill("solid", fgColor="66CCFF")  # 設定儲存格的背景色

sheet["A3"].font = openpyxl.styles.Font(name="Arial", color="ff0000", size=20, bold=True)  # 設定儲存格的文字樣式
sheet["B3"].font = openpyxl.styles.Font(name="Arial", color="00ff00", size=20, bold=True)  # 設定儲存格的文字樣式
sheet["C3"].font = openpyxl.styles.Font(name="Arial", color="0000ff", size=20, bold=True)  # 設定儲存格的文字樣式
sheet["D3"].fill = openpyxl.styles.PatternFill(fill_type="solid", fgColor="FFFF00")  # 設定儲存格的背景樣式

print("------------------------------")  # 30個

#預設靠左對齊
#改成中間對齊
sheet.cell(1, 1).alignment = openpyxl.styles.Alignment("center")

print("------------------------------")  # 30個

#貼上一張圖
from openpyxl.drawing.image import Image
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
img = Image(filename)
sheet.add_image(img, "E13")  # 把圖貼在E13

print("------------------------------")  # 30個

sheet["E3"] = "設定日期格式"
import datetime
#sheet = workbook["animals1"]
sheet["E4"] = datetime.datetime(1928, 11, 18, 12, 34, 56)
#sheet['E4'].number_format = 'yyyy-mm-dd h:mm:ss'
sheet['E4'].number_format = 'yyyy-mm-dd'
#sheet["E4"].number_format = "dd-mm-yyyy"

print("------------------------------")  # 30個

print("儲存格格式")
from openpyxl.styles import Border, Side

side1 = Side(style="hair", color="FF0000")  #R
side2 = Side(style="dashDotDot", color="00FF00") #G
side3 = Side(style="double", color="0000FF") #B

for rows in sheet["A13":"D15"]:
    for cell in rows:
        cell.border = Border(left=side1, right=side1, top=side1, bottom=side1 )

for rows in sheet["A17":"D19"]:
    for cell in rows:
        cell.border = Border(left=side2, right=side2, top=side2, bottom=side2)

for rows in sheet["A21":"D23"]:
    for cell in rows:
        cell.border = Border(left=side3, right=side3, top=side3, bottom=side3 )

print("------------------------------")  # 30個

filename_w = "tmp_excel_openpyxl_b2_new_all1.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 02 建立新檔 完整資料 + 格式")
print("開啟空白的活頁簿")
workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

print("開啟工作表")
# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 以儲存格位置寫入資料, 直接修改/設定工作表內的資料
sheet["A1"] = "動物列表"
sheet["A2"] = "中文名"
sheet["B2"] = "英文名"
sheet["C2"] = "體重"
sheet["D2"] = "全名"

""" same
listtitle=['中文名', '英文名', '體重', '全名']
sheet.append(listtitle)  
"""
# 以串列寫入資料
animal01 = ["鼠", "mouse", 3, "米老鼠"]#直接使用數值, 這樣才可以計算
animal02 = ["牛", "ox", 48, "班尼牛"]
animal03 = ["虎", "tiger", 33, "跳跳虎"]
animal04 = ["兔", "rabbit", 8, "彼得兔"]
sheet.append(animal01)  # 逐筆添加到最後一列
sheet.append(animal02)  # 逐筆添加到最後一列
sheet.append(animal03)  # 逐筆添加到最後一列
sheet.append(animal04)  # 逐筆添加到最後一列

print("------------------------------")  # 30個

#設定欄寬
col_widths = {"A":15, "B":15, "C":10, "D":10, "E":10, "F":10, "G":10, "H":10}
for col_name in col_widths:
    sheet.column_dimensions[col_name].width = col_widths[col_name]

#建立字體
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side
font_header = Font(name="MS PGothic",size=12,bold=True,color="FFFFFF")

#設定背景色
TITLE_CELL_COLOR = "AA8866"
for rows in sheet["A1":"H1"]:
    for cell in rows:
        #儲存格背景色
        cell.fill = PatternFill(patternType="solid", fgColor=TITLE_CELL_COLOR)
        #水平置中
        cell.alignment = Alignment(horizontal="distributed")
        #設定字型
        cell.font = font_header

side = Side(style="thin", color="000000")
border = Border(left=side, right=side, top=side, bottom=side)
for row in sheet:
    for cell in row:
        cell.border = border
        #sheet[cell.coordinate].border = border

print("------------------------------")  # 30個

filename_w = "tmp_excel_openpyxl_b2_new_all2.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 03 讀 寫 從檔案後面附加資料")

if not os.path.exists(filename_w):
    workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
    sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
    heading = ["中文名", "英文名", "體重", "全名"]
    sheet.append(heading)
    workbook.save(filename_w)

workbook = openpyxl.load_workbook(filename_w)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

animal01 = ["鼠", "mouse", "3", "米老鼠"]
sheet.append(animal01)

filename_w = "tmp_excel_openpyxl_c.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 03 讀 寫 讀後再寫")

filename_r = "data/python_ReadWrite_EXCEL.xlsx"

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

filename_w = "tmp_excel_openpyxl_c_sheet.xlsx"
workbook.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 04 創建Excel文件")

# 這個有問題

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

sheet.append(["中文名", "英文名", "體重", "全名"])
data =[
    ["鼠", "mouse", "3", "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", "33", "跳跳虎"]
]

for row in data:
    sheet.append(row)

tab = openpyxl.worksheet.table.Table(displayName="Table1", ref="A1:E5")
tab.tableStyleInfo = openpyxl.worksheet.table.TableStyleInfo(
    name="TableStyleMedium9",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=True,
)
#sheet.add_table(tab) 問題在這裡

filename_w = "tmp_excel_openpyxl_d_add_table.xlsx"
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print("openpyxl test 05")

import pathlib  # 標準函式庫
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

filename_w = "tmp_excel_openpyxl_e.xlsx"
workbook.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
'''
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
'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



#對齊方式 ST
import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.Workbook()
sh = wb.active


sh.column_dimensions["A"].width = 20 
sh["a1"] = "left,bottom"
sh["a1"].alignment = Alignment(horizontal="left",vertical="bottom")
sh["a2"] = "center,center"
sh["a2"].alignment = Alignment(horizontal="center",vertical="center")
sh["a3"] = "right,top"
sh["a3"].alignment = Alignment(horizontal="right",vertical="top")
sh["a4"] = "distributed,bottom"
sh["a4"].alignment = Alignment(horizontal="distributed",vertical="bottom")

wb.save(r"tmp_format_test.xlsx")
#對齊方式 SP



