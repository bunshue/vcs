# ch22_25.py
import xlrd

fn = 'out24.xls'
wb = xlrd.open_workbook(fn)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))





