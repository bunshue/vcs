#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import xlrd
import xlwt

read=xlrd.open_workbook('water10705.xls')
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

write = xlwt.Workbook()
x1=0
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
write.save('write.xls')
