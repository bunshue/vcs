'''
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_excel/python_ReadWrite_EXCEL1.xlsx'

import xlrd

data = xlrd.open_workbook(filename)

s1 = data.sheets()[0]
s2 = data.sheets()[1]

print(data)
print(s1)
print(s2)


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



import xlrd

data = xlrd.open_workbook(filename)
s1 = data.sheets()[0]
for row in range(s1.nrows):
    print(s1.row_values(row))

'''


import xlrd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_excel/python_ReadWrite_EXCEL2.xlsx'

data = xlrd.open_workbook(filename)

#取出工作表的index
for n in range(len(data.sheet_names())):
    print(n)
    table = data.sheets()[n]

    for i in range(table.nrows):
        print('Page {}: '.format(n), end='')
        print(table.row_values(i))

'''
data.sheets()[n] 可以指定我們要讀第幾個工作表，在這裡 n 便是我工作表的 index。
table.nrows 可以顯示我列數有幾列，在這裡我用 row_values(i) 將每一張工作表、每一列 print 出來。
當然，你要一行行地印出來也是可行的。
'''

data = xlrd.open_workbook(filename)

for n in range(len(data.sheet_names())):
    table = data.sheets()[n]

    for i in range(table.ncols):
        print('Page {}: '.format(n), end='')
        print(table.col_values(i))

        

