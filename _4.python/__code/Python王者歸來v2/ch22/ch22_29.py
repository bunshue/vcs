# ch22_29.py
import xlrd

fn = 'out22_28.xls'
wb = xlrd.open_workbook(fn)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))





