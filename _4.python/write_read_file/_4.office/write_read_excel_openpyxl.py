"""
讀寫 Excel 檔案, 使用 openpyxl


"""

import os
import sys
import time
import openpyxl
'''
print("------------------------------------------------------------")  # 60個
print('openpyxl test 01')
print('建立excel檔案 xlsx a')

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 修改工作表的名稱
sheet.title = "Animal"

# 以儲存格位置寫入資料
sheet['A1'] = '中文名'
sheet['B1'] = '英文名'
sheet['C1'] = '體重'
sheet['D1'] = '全名'

# 以串列寫入資料
animal01 = ['鼠', 'mouse', '3']
animal02 = ['牛', 'ox', '48']
animal03 = ['虎', 'tiger', '33']
animal04 = ['兔', 'rabbit', '8']
sheet.append(animal01)  # 逐筆添加到最後一列
sheet.append(animal02)  # 逐筆添加到最後一列
sheet.append(animal03)  # 逐筆添加到最後一列
sheet.append(animal04)  # 逐筆添加到最後一列

#設定格式
#sheet = workbook["Animal"]
sheet["A1"].fill = openpyxl.styles.PatternFill(fill_type="solid", fgColor="FFFF00")  # 設定 f1 儲存格的背景樣式
sheet["B1"].font = openpyxl.styles.Font(name="Arial", color="ff0000", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
sheet["C1"].font = openpyxl.styles.Font(name="Arial", color="00ff00", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
sheet["D1"].font = openpyxl.styles.Font(name="Arial", color="0000ff", size=30, bold=True)  # 設定 g1 儲存格的文字樣式

filename_w = 'tmp_excel_openpyxl01.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print('------------------------------------------------------------')	#60個
print('openpyxl test 02')
print('excel讀寫測試 3')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
print('所有工作表名稱 :', workbook.sheetnames)

names = workbook.sheetnames  # 讀取 excel檔案 裏所有工作表名稱
print(names)

# 取得第 0 個工作表
sheet = workbook.worksheets[0]

# 取得最後編輯的那個工作表
# sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

#取得工作表參數
sheet_name = sheet.title
ROW = sheet.max_row
COL = sheet.max_column

print('此工作表名稱、總列數、總行數 :', sheet_name, ROW, COL)

# 取得第 0 個工作表 same
sheet = workbook[workbook.sheetnames[0]]
print('此工作表名稱 :', sheet.title)

print('------------------------------')	#60個
print("顯示資料 方法一");

"""
# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)

#修改資料
sheet['B3'] = 'Chris' 
"""

# 顯示 cell資料
for i in range(1, ROW+1):
    for j in range(1, COL+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()

print('------------------------------')	#60個
print("顯示資料 方法二");

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

print('------------------------------')	#60個
print("顯示資料 方法三");

for sheet in workbook:
    print('sheet', sheet)
    for row in sheet:
        #print('row')
        for cell in row:
            print(cell.value, end = ' ')
        print()
    print()

print('------------------------------------------------------------')	#60個
print('openpyxl test 03')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'
print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
print('所有工作表名稱 :', workbook.sheetnames)

names = workbook.sheetnames  # 讀取 exam1 裡所有工作表名稱
s1 = workbook["exam1"]  # 取得工作表名稱為「工作表1」的內容
s2 = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
print(names)

print('印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數')
print(s1.title, s1.max_row, s1.max_column)
print(s2.title, s2.max_row, s2.max_column)

print("------------------------------------------------------------")  # 60個
print('openpyxl test 04')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)  # 設定 data_only=True 只讀取計算後的數值
print('所有工作表名稱 :', workbook.sheetnames)

s1 = workbook["exam1"]
s2 = workbook["exam2"]

print(s1["A1"].value)  # 取出 A1 的內容
print(s1.cell(1, 1).value)  # 等同取出 A1 的內容

print(s2["B2"].value)  # 取出 B2 的內容
print(s2.cell(2, 2).value)  # 等同取出 B2 的內容

print("------------------------------------------------------------")  # 60個
print('openpyxl test 05')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)  # 設定 data_only=True 只讀取計算後的數值
print('所有工作表名稱 :', workbook.sheetnames)

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


print(get_values(s1))  # 印出工作表 1 所有內容
print(get_values(s2))  # 印出工作表 2 所有內容

"""
[[12, 34, 56, 78, 180, 180], [11, 22, 33, 44, 110, 110]]
[['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a4', 'b4', 'c4'], ['a5', 'b5', 'c5']]
"""

print("------------------------------------------------------------")  # 60個
print('openpyxl test 06')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s1 = workbook["exam1"]
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
print('openpyxl test 07')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'
print("讀取 xlsx, 檔案 : " + filename_r)
workbook = openpyxl.load_workbook(filename_r)
print('所有工作表名稱 :', workbook.sheetnames)

s1 = workbook["exam1"]  # 取得工作表名稱為「工作表1」的內容
s2 = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

print(
    s1.title, s1.max_row, s1.max_column
)  # 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數
print(
    s2.title, s2.max_row, s2.max_column
)  # 印出 title ( 工作表名稱 )、max_row 最大列數、max_column 最大行數

print(s1.sheet_properties)  # 印出工作表屬性

print("------------------------------------------------------------")  # 60個
print('openpyxl test 08')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s1 = workbook["exam1"]  # 開啟工作表 1
s2 = workbook["exam2"]  # 開啟工作表 2
s1.sheet_properties.tabColor = "ff0000"  # 修改工作表 1 頁籤顏色為紅色
s2.sheet_properties.tabColor = "ffff00"  # 修改工作表 2 頁籤顏色為黃色

workbook.create_sheet("工作表3")  # 插入工作表 3 在最後方
workbook.create_sheet("工作表1.5", 1)  # 插入工作表 1.5 在第二個位置 ( 工作表 1 和 2 的中間 )
workbook.create_sheet("工作表0", 0)  # 插入工作表 0 在第一個位置

workbook.copy_worksheet(s2)  # 複製工作表 2 放到最後方

s1.title = "oxxo"  # 修改工作表 1 的名稱為 oxxo
s2.title = "studio"  # 修改工作表 2 的名稱為 studio

filename_w = 'tmp_excel_openpyxl09.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print('openpyxl test 09')

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

print("------------------------------------------------------------")  # 60個
print('openpyxl test 10')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s3 = workbook.create_sheet("工作表3")  # 新增工作表 3
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 二維陣列資料
for i in data:
    s3.append(i)  # 逐筆添加到最後一列

filename_w = 'tmp_excel_openpyxl11.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print('openpyxl test 11')
filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s2 = workbook["exam2"]  # 開啟工作表 2
data = [[1, 2], [3, 4]]  # 二維陣列資料
for y in range(len(data)):
    for x in range(len(data[y])):
        row = 2 + y  # 寫入資料的範圍從 row=2 開始
        col = 2 + x  # 寫入資料的範圍從 column=2 開始
        s2.cell(row, col).value = data[y][x]

filename_w = 'tmp_excel_openpyxl12.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print('openpyxl test 12')

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

workbook = openpyxl.load_workbook(filename_r, data_only=True)
print('所有工作表名稱 :', workbook.sheetnames)

s2 = workbook["exam2"]
s2["d1"] = "=sum(a1:c1)"  # 寫入公式
s2["d2"] = "=sum(a2:c2)"  # 寫入公式
s2["d3"] = "=sum(a3:c3)"  # 寫入公式
s2["d4"] = "=sum(a4:c4)"  # 寫入公式
s2["d5"] = "=sum(a5:c5)"  # 寫入公式

filename_w = 'tmp_excel_openpyxl13.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個

print('openpyxl test 13')
print('從檔案後面附加資料')

filename_w = 'tmp_excel_openpyxl06.xlsx'
            
if not os.path.exists(filename_w):
    workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
    sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)
    heading = ["中文名", "英文名", "體重", "全名"]
    sheet.append(heading)
    workbook.save(filename_w)

workbook = openpyxl.load_workbook(filename_w)
print('所有工作表名稱 :', workbook.sheetnames)

sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

animal01 = ['鼠', 'mouse', '3', '米老鼠']
sheet.append(animal01)

workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)


print('------------------------------------------------------------')	#60個
print('openpyxl test 14')
#創建Excel文件

# 這個有問題

from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
sheet = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

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

filename_w = 'tmp_excel_openpyxl08_全班學生數據.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print("------------------------------------------------------------")  # 60個
print('openpyxl test 15')

from openpyxl.utils import get_column_letter, column_index_from_string

print(column_index_from_string("A"))  # 1
print(column_index_from_string("AA"))  # 27

print(get_column_letter(5))  # E
print(get_column_letter(100))  # CV

print("------------------------------------------------------------")  # 60個
print('openpyxl test 16')
from openpyxl.chart import RadarChart, Reference

print('在excel檔案內加入雷達圖')

filename_r = 'data/radar_chart.xlsx'
workbook = openpyxl.load_workbook(filename_r)
print('所有工作表名稱 :', workbook.sheetnames)

sh = workbook.active  # 取得開啟試算表後立刻顯示的工作表(即最後編輯的工作表)

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

filename_w = 'tmp_excel_openpyxl07_add_radar_chart.xlsx'
workbook.save(filename_w)  # 儲存檔案
print("建立 xlsx OK, 檔案 : " + filename_w)

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
保留
sheet = workbook.create_sheet("animal")  # 建立新工作表 名為animal

workbook = openpyxl.load_workbook(filename_r, data_only=True)


for row in range(2, 7):  # 第 2~6 ROW
    for col in range(65, 70): # 65~69 A~E
        cell_index = chr(col) + str(row)
        print(sheet[cell_index].value, end='\t')
    print()


"""

#新進

print("------------------------------------------------------------")  # 60個

import openpyxl

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

try:
    wb = openpyxl.load_workbook(filename_r)
    for sheetname in wb.sheetnames:                 #所有工作表
        sheet = wb[sheetname]
        for c in range(1, sheet.max_column+1):      #欄1〜最後
            for r in range(1, sheet.max_row+1):     #列1〜最後
                cell = sheet.cell(row=r, column=c)  #儲存格
                if cell.value != None:
                    print(cell.value, end = " ")
            print()
except:
    print("程式執行失敗。")
    
print("------------------------------------------------------------")  # 60個

import calendar
import openpyxl

year = 2022
month = 12
dayname = ["日","一","二","三","四","五","六"]

#【在Excel檔新增月曆的函數】
def makecalendar(value1, value2):
    year = int(value1)
    month = int(value2)
    savefile = "tmp_"+str(year)+"_"+str(month)+".xlsx"

    cal = calendar.Calendar(calendar.SUNDAY)
    wb = openpyxl.Workbook()
    ws = wb.active
    c = ws.cell(1,4)
    c.value = str(year)+"年"+str(month)+"月"
    for col in range(7):                        #一週的每一天
        c = ws.cell(2, col+1)
        c.value = dayname[col]
    for (col, week) in enumerate(cal.monthdayscalendar(year, month)):
        for (row, day) in enumerate(week):
            if day > 0 :
                c = ws.cell((col + 3), row+1)
                c.value = day
    wb.save(savefile)   #Excel轉存檔案
    return "轉存"+savefile+"了。"

msg = makecalendar(year, month)
print(msg)

print("------------------------------------------------------------")  # 60個

import calendar
import openpyxl

value1 = "2022"
value2 = "12"
dayname = ["日","一","二","三","四","五","六"]

fontN = openpyxl.styles.Font(size=24)
fontB = openpyxl.styles.Font(size=24, color="0000FF")
fontR = openpyxl.styles.Font(size=24, color="FF0000")
fillB = openpyxl.styles.PatternFill(patternType="solid", fgColor="AAAAFF")
fillR = openpyxl.styles.PatternFill(patternType="solid", fgColor="FFAAAA")

#【在Excel檔新增月曆的函數】
def makecalendar(value1, value2):
    year = int(value1)
    month = int(value2)
    savefile = str(year)+"_"+str(month)+".xlsx"

    cal = calendar.Calendar(calendar.SUNDAY)
    wb = openpyxl.Workbook()
    ws = wb.active
    for c in ["A","B","C","D","E","F","G"]:
        ws.column_dimensions[c].width = 20
    c = ws.cell(1,4)
    c.value = str(year)+"年"+str(month)+"月"
    c.font = fontN
    for row in range(7):
        c = ws.cell(2, row+1)
        c.value = dayname[row]
        c.font = fontN
        c.alignment = openpyxl.styles.Alignment("center")
        if row == 6:
            c.font = fontB
            c.fill = fillB
        if row == 0:
            c.font = fontR
            c.fill = fillR
    for (col, week) in enumerate(cal.monthdayscalendar(year, month)):
        ws.row_dimensions[col+3].height = 50
        for (row, day) in enumerate(week):
            if day > 0 :
                c = ws.cell((col + 3), row+1)
                c.value = day
                c.font = fontN
                if row == 6:
                    c.font = fontB
                if row == 0:
                    c.font = fontR
    wb.save(savefile)   #Excel轉存檔案
    return "轉存"+savefile+"了。"

msg = makecalendar(value1, value2)
print(msg)

print("------------------------------------------------------------")  # 60個

import openpyxl

filename_r = "test.xlsx"
filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

value1 = "tmp_output.xlsx"
try:
    wb = openpyxl.load_workbook(filename_r)
    wb.save(value1)   #Excel轉存檔案
except:
    print("程式執行失敗。")

print("------------------------------------------------------------")  # 60個

import openpyxl

value1 = "tmp_output0.xlsx"

wb = openpyxl.Workbook()
ws = wb.active 

c = ws.cell(1,1)
c.value = "第1列,第1欄"
c = ws.cell(5,3)
c.value = "第5列,第3欄"

wb.save(value1)     #Excel轉存檔案

print("------------------------------------------------------------")  # 60個

import openpyxl

value1 = "tmp_output1.xlsx"

wb = openpyxl.Workbook()
ws = wb.active 

c = ws.cell(1,1)
c.value = "第1列,第1欄"
c.font = openpyxl.styles.Font(size = 24, color="0000CC") # 設定儲存格的文字大小與文字顏色
c.fill = openpyxl.styles.PatternFill("solid", fgColor="66CCFF") # 設定儲存格的背景色
c = ws.cell(5,3)
c.value = "第5列,第3欄"
c.font = openpyxl.styles.Font(size = 24, color="0000CC")
c.fill = openpyxl.styles.PatternFill("solid", fgColor="66CCFF")

ws.column_dimensions["A"].width = 20 #設定欄寬
ws.column_dimensions["C"].width = 20
ws.row_dimensions[1].height = 50 #設定列高
ws.row_dimensions[5].height = 50

wb.save(value1)     #Excel轉存檔案

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
'''

print("------------------------------------------------------------")  # 60個

import openpyxl   
# 建立一個工作簿     
workbook=openpyxl.Workbook()   
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
workbook.save('tmp_cccc_test.xlsx')


import openpyxl
#  讀取檔案
workbook = openpyxl.load_workbook('tmp_cccc_test.xlsx')
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)
# 取得總行、列數
print(sheet.max_row, sheet.max_column)
# 顯示 cell資料
for i in range(1, sheet.max_row+1):
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()
sheet['A3'] = 'Perry' 
workbook.save('tmp_cccc_test222.xlsx')





import openpyxl   
# 建立一個工作簿     
workbook=openpyxl.Workbook()   
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 以儲存格位置寫入資料
sheet['A1'] = '一年甲班'
# 以串列寫入資料
listtitle=['座號', '姓名', '國文', '英文', '數學']
sheet.append(listtitle)  
listdatas=[[1, '葉大雄', 65, 62, 40],
           [2, '陳靜香', 85, 90, 87],
           [3, '王聰明', 92, 90, 95]]
for listdata in listdatas:
    sheet.append(listdata)
# 儲存檔案   
workbook.save('tmp_test5555.xlsx')


import openpyxl
#  讀取檔案
workbook = openpyxl.load_workbook('tmp_test5555.xlsx')
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)
# 取得總行、列數
print(sheet.max_row, sheet.max_column)
# 顯示 cell資料
for i in range(1, sheet.max_row+1):
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()
sheet['A1'] = '二年甲班' 
workbook.save('tmp_test5555b.xlsx')      

print("------------------------------------------------------------")  # 60個

# xlsx_write.py
import openpyxl   
# 建立一個工作簿     
workbook=openpyxl.Workbook()   
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 以儲存格位置寫入資料
sheet['A1'] = '一年甲班'
# 以串列寫入資料
listtitle=['座號', '姓名', '國文', '英文', '數學']
sheet.append(listtitle)  
listdatas=[[1, '葉大雄', 65, 62, 40],
           [2, '陳靜香', 85, 90, 87],
           [3, '王聰明', 92, 90, 95]]
for listdata in listdatas:
    sheet.append(listdata)
# 儲存檔案   
workbook.save('test.xlsx')

# xlsx_read.py
import openpyxl
#  讀取檔案
workbook = openpyxl.load_workbook('test.xlsx')
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)
# 取得總行、列數
print(sheet.max_row, sheet.max_column)
# 顯示 cell資料
for i in range(1, sheet.max_row+1):
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()
sheet['A1'] = '二年甲班' 
workbook.save('test.xlsx')      



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

