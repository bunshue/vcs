"""
讀寫 Excel 檔案, 使用 xlrd(讀) xlwt(寫)


在新版python3.9中，windows中使用的更新删除了getiterator方法
sugar要先到
#C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/xlrd/xlsx.py
把兩個 getiterator() 改成 iter()

"""

import sys
import pprint as pp
import xlrd

print('------------------------------------------------------------')	#60個

print('讀取excel檔案 1')
filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

data = xlrd.open_workbook(filename_r)
print('這個excel檔案的工作表頁數 :', len(data.sheets()))

print('工作表名稱:')
cc= data.sheet_names()
for _ in cc:
    print(_)

print('第0頁 內容')
sh0 = data.sheets()[0]
for row in range(sh0.nrows):
    print(sh0.row_values(row))

print('第1頁 內容')
sh1 = data.sheets()[1]
for row in range(sh1.nrows):
    print(sh1.row_values(row))

print('取出所有頁面')
sheets = data.sheets()
for sheet in sheets:
    print(sheet)
    for row in range(sheet.nrows):
        print(sheet.row_values(row))
        
print('取出所有頁面 至 字典格式')

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

sh0 = data.sheets()[0]
#sh0 = data.sheets("Sheet5")
print('第0頁 ROW數 :', sh0.nrows)
print('第0頁 COL數 :', sh0.ncols)
ROW = sh0.nrows
COL = sh0.ncols
print(sh0.cell(3,0).value)
for i in range(0, ROW):
    print(sh0.cell(i, 0).value, sh0.cell(i, 1).value, sh0.cell(i, 2).value, sh0.cell(i, 3).value, sh0.cell(i, 4).value)

print('------------------------------------------------------------')	#60個

import xlrd

filename_r = 'data/python_ReadWrite_EXCEL1.xlsx'

data = xlrd.open_workbook(filename_r)
print('這個excel檔案的工作表頁數 :', len(data.sheets()))

print('取出所有工作表, 看rows')
for n in range(len(data.sheet_names())):
    sheet = data.sheets()[n]

    for i in range(sheet.nrows):
        print('Page {}: '.format(n), end='')
        print(sheet.row_values(i))

#data.sheets()[n] 可以指定我們要讀第幾個工作表，在這裡 n 便是我工作表的 index。
#sheet.nrows 可以顯示我列數有幾列，在這裡我用 row_values(i) 將每一張工作表、每一列 print 出來。
#當然，你要一行行地印出來也是可行的。

data = xlrd.open_workbook(filename_r)

print('取出所有工作表, 看columns')
for n in range(len(data.sheet_names())):
    sheet = data.sheets()[n]

    for i in range(sheet.ncols):
        print('Page {}: '.format(n), end='')
        print(sheet.col_values(i))

print('------------------------------------------------------------')	#60個

print('用xlwt寫入xls檔案')

import xlwt

filename_w = 'tmp_excel_xlwt1.xls'

datahead = ['中文名', '英文名', '體重']

animal01 = ['鼠', 'mouse', '3']
animal02 = ['牛', 'ox', '48']
animal03 = ['虎', 'tiger', '33']
animal04 = ['兔', 'rabbit', '8']

animals = [animal01, animal02, animal03, animal04]

write = xlwt.Workbook()
sh = write.add_sheet('sheet1', cell_overwrite_ok=True)

for i in range(len(datahead)):
    sh.write(0, i, datahead[i])     # 寫入datahead list

for j in range(len(animals[0])):
    sh.write(1, j, animals[0][j])

for j in range(len(animals[1])):
    sh.write(2, j, animals[1][j])

for j in range(len(animals[2])):
    sh.write(3, j, animals[2][j])

for j in range(len(animals[3])):
    sh.write(4, j, animals[3][j])



# 儲存檔案
write.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)

print('------------------------------------------------------------')	#60個

import xlwt

filename_w = 'tmp_excel_xlwt2.xls'

write = xlwt.Workbook()
write2 = write.add_sheet('MySheet') # 建立新工作表，設定名稱
for i in range(10, 36):
    #          ROW COL Data
    write2.write(i, 0, 123)

# 儲存檔案
write.save(filename_w)
print("建立 xlsx OK, 檔案 : " + filename_w)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

