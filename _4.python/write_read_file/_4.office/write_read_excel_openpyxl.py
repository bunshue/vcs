"""
讀寫 Excel 檔案, 使用 openpyxl


"""

import os
import sys
import time
import openpyxl

print("------------------------------------------------------------")  # 60個
'''
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
sheet.add_table(tab)

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
    sheet = workbook.active
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
    sheet = workbook.active
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

#aggregate_orders

import openpyxl

categorys = ((0,""),(10,"POLO衫"), (11,"禮服襯衫"), (12,"休閒襯衫"), \
            (13,"T恤"), (15,"開襟羊毛衫"),(16,"毛衣"),(17,"吸汗上衣"), \
            (18,"連帽T"))
sizes = ("代碼","分類名稱","S","M","L","LL","XL")
#製作二維列表
# 下面的程式不行，因為元素的列表會是相同的物件
#order_amount= [[0]*len(sizes)] * len(categorys)
order_amount= [[0]*len(sizes) for i in range(len(categorys))]

for j in range(len(sizes)):
    order_amount[0][j] = sizes[j]
for i in range(1,len(categorys)):
    order_amount[i][0] = categorys[i][0]
    order_amount[i][1] = categorys[i][1]
#print(order_amount)   

wb = openpyxl.load_workbook("data\ordersList.xlsx")
sh = wb.active
for row in range(2, sh.max_row + 1):
    category = sh["I" + str(row)].value
    size = sh["L" + str(row)].value
    amount = sh["M" + str(row)].value
    for i in range(1,len(categorys)):
        if category == order_amount[i][0]:
            for j in range(2,len(sizes)):
                if size == order_amount[0][j]:
                    order_amount[i][j] += amount


owb = openpyxl.Workbook()
osh = owb.active
row = 1
for order_row in order_amount:
    col = 1
    size_sum = 0 
    for order_col in order_row:
        osh.cell(row, col).value = order_col
        if  row > 1 and col > 2: 
            #print(order_col)
            size_sum += order_col
        col += 1
    if row == 1:
        osh.cell(row, col).value =  "合計"
    else:
        osh.cell(row, col).value =  size_sum
    row += 1

owb.save("tmp_orders_aggregate.xlsx")
'''
print("------------------------------------------------------------")  # 60個

import openpyxl

def print_header():
    osh["A1"].value = "負責人"
    osh["B1"].value = "數量"
    osh["C1"].value = "金額"
    osh["D1"].value = "客戶"
    osh["E1"].value = "數量"
    osh["F1"].value = "金額"

wb = openpyxl.load_workbook("data\salesList.xlsx")
sh = wb.active
sales_data = {}
for row in range(1, sh.max_row + 1):
    person = sh["E" + str(row)].value
    customer = sh["C" + str(row)].value
    quantity = sh["J" + str(row)].value
    amount = sh["L" + str(row)].value
    sales_data.setdefault(person, {"name": sh["F" + str(row)].value , "quantity": 0, "amount":0})
    sales_data[person].setdefault(customer, {"name": sh["D" + str(row)].value , "quantity": 0, "amount":0})
    sales_data[person][customer]["quantity"] += int(quantity)
    sales_data[person][customer]["amount"] += int(amount)
    sales_data[person]["quantity"] += int(quantity)
    sales_data[person]["amount"] += int(amount)
    #print(sales_data)

owb = openpyxl.Workbook()
osh = owb.active
print_header()

row = 2
for person_data in sales_data.values():
    osh["A" + str(row)].value = person_data["name"]
    osh["B" + str(row)].value = person_data["quantity"]
    osh["C" + str(row)].value = person_data["amount"]
    for customer_data in person_data.values():
        #print(customer_data)
        if isinstance(customer_data,dict):
            for item in customer_data.values():
                osh["D" + str(row)].value = customer_data["name"]
                osh["E" + str(row)].value = customer_data["quantity"]
                osh["F" + str(row)].value = customer_data["amount"]
            row +=1 

osh["F" + str(row)].value =  "=SUM(F2:F" + str(row-1) + ")"
osh["E" + str(row)].value =  "合計"

owb.save("tmp_sales_aggregate222.xlsx")

print("------------------------------------------------------------")  # 60個

import pathlib  # 標準函式庫
import openpyxl # 外部函式庫　pip install openpyxl
import csv      # 標準函式庫

lwb = openpyxl.Workbook()           #業績一覽表活頁簿
lsh = lwb.active                    #業績一覽工作表
list_row = 1
path = pathlib.Path("data\sales")    #指定相對路徑
for pass_obj in path.iterdir():
    if pass_obj.match("*.xlsx"):
        wb = openpyxl.load_workbook(pass_obj)
        for sh in wb:
            for dt_row in range(9,19):
                if sh.cell(dt_row, 2).value != None:
                    #更便於說明的代碼
                    #lsh.cell(row=list_row, column=1).value = \
                    #    sh.cell(row=2, column=7).value   #傳票NO
                    lsh.cell(list_row, 1).value = sh.cell(2, 7).value   #傳票NO
                    lsh.cell(list_row, 2).value = sh.cell(3, 7).value   #日期
                    lsh.cell(list_row, 3).value = sh.cell(4, 3).value   #客戶代碼
                    lsh.cell(list_row, 4).value = sh.cell(3, 2).value.strip("敬啟")   #客戶名稱
                    lsh.cell(list_row, 5).value = sh.cell(7, 8).value   #負責人代碼
                    lsh.cell(list_row, 6).value = sh.cell(7, 7).value   #負責人姓名
                    lsh.cell(list_row, 7).value = sh.cell(dt_row, 1).value #No                    
                    lsh.cell(list_row, 8).value = sh.cell(dt_row, 2).value #商品代碼 
                    lsh.cell(list_row, 9).value = sh.cell(dt_row, 3).value #商品名稱
                    lsh.cell(list_row, 10).value = sh.cell(dt_row, 4).value #數量
                    lsh.cell(list_row, 11).value = sh.cell(dt_row, 5).value #單價
                    lsh.cell(list_row, 12).value = sh.cell(dt_row, 4).value * \
                                                sh.cell(dt_row, 5).value #金額
                    lsh.cell(list_row, 13).value = sh.cell(dt_row, 7).value #備註                                      
                    list_row += 1

lwb.save("tmp_salesList555555.xlsx")




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
