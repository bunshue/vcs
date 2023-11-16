#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import pandas as pd
#data = pd.read_csv('ExpensesRecord.csv')
df = pd.read_excel('ExpensesRecord.xls', 'sheet')
#data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head(5) )



from pandas import ExcelWriter
writer = ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')
writer.save()