import xlrd

print('------------------------------------------------------------')	#60個

filename = 'data/python_ReadWrite_EXCEL1.xlsx'

print('------------------------------------------------------------')	#60個
"""
data = xlrd.open_workbook(filename)

s1 = data.sheets()[0]
s2 = data.sheets()[1]

print(data)
print(s1)
print(s2)

print('------------------------------------------------------------')	#60個

import pprint as pp
import xlrd

data = xlrd.open_workbook(filename)
sheets = data.sheets()

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
pp.pprint(scores)

print('------------------------------------------------------------')	#60個

import xlrd

data = xlrd.open_workbook(filename)
s1 = data.sheets()[0]
for row in range(s1.nrows):
    print(s1.row_values(row))

print('------------------------------------------------------------')	#60個

import xlrd

filename = 'data/python_ReadWrite_EXCEL2.xlsx'

data = xlrd.open_workbook(filename)

#取出工作表的index
for n in range(len(data.sheet_names())):
    print(n)
    table = data.sheets()[n]

    for i in range(table.nrows):
        print('Page {}: '.format(n), end='')
        print(table.row_values(i))

#data.sheets()[n] 可以指定我們要讀第幾個工作表，在這裡 n 便是我工作表的 index。
#table.nrows 可以顯示我列數有幾列，在這裡我用 row_values(i) 將每一張工作表、每一列 print 出來。
#當然，你要一行行地印出來也是可行的。

data = xlrd.open_workbook(filename)

for n in range(len(data.sheet_names())):
    table = data.sheets()[n]

    for i in range(table.ncols):
        print('Page {}: '.format(n), end='')
        print(table.col_values(i))
"""
print('------------------------------------------------------------')	#60個

print('用xlwt寫入xls檔案')

import xlwt

filename = 'tmp_excel.xls'
datahead = ['Phone', 'TV', 'Notebook']
price = ['35000', '18000', '28000']
wb = xlwt.Workbook()
sh = wb.add_sheet('sheet1', cell_overwrite_ok=True)
for i in range(len(datahead)):
    sh.write(0, i, datahead[i])     # 寫入datahead list
for j in range(len(price)):
    sh.write(1, j, price[j])        # 寫入price list

wb.save(filename)

print('------------------------------------------------------------')	#60個

print('用xlrd讀取xls檔案')
import xlrd

filename = 'tmp_excel.xls'
wb = xlrd.open_workbook(filename)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))
    
print('------------------------------------------------------------')	#60個


import xlrd
import xlwt

filename_r = 'data/water10705.xls'
filename_w = 'tmp_excel2.xls'

print('讀取xls檔, 檔案 :', filename_r)

read = xlrd.open_workbook(filename_r)

sheet = read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

write = xlwt.Workbook()
x1 = 0
write2 = write.add_sheet('MySheet')
for i in range(10,36):
    print(sheet.cell(i,12).value)
    value=sheet.cell(i,12).value
    try:
      x1=x1+float(value)
    except:
      print("")
    write2.write(i, 0, value)

print("total:",x1)

print('寫入xls檔, 檔案 :', filename_w)

write.save(filename_w)

print('------------------------------------------------------------')	#60個

import xlrd
import xlwt

filename_r = 'data/workfile.xls'
filename_w = 'tmp_excel3.xls'

print('讀取xls檔, 檔案 :', filename_r)

read=xlrd.open_workbook(filename_r)
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

print(sheet.cell(5,1).value)

write = xlwt.Workbook()
write2 = write.add_sheet('MySheet')
for i in range(0,sheet.nrows):
    print(sheet.cell(i,1).value)
    value=sheet.cell(i,1).value
    write2.write(i, 0, value)

print('寫入xls檔, 檔案 :', filename_w)
write.save(filename_w)

print('------------------------------------------------------------')	#60個

import xlwt

filename = 'tmp_excel_file1.xls'
datahead = ['Phone', 'TV', 'Notebook']
price = ['35000', '18000', '28000']
wb = xlwt.Workbook()
sh = wb.add_sheet('sheet1', cell_overwrite_ok=True)
for i in range(len(datahead)):
    sh.write(0, i, datahead[i])     # 寫入datahead list
for j in range(len(price)):
    sh.write(1, j, price[j])        # 寫入price list

wb.save(filename)

print("------------------------------------------------------------")  # 60個

import xlrd

filename = 'tmp_excel_file1.xls'
wb = xlrd.open_workbook(filename)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))


print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


