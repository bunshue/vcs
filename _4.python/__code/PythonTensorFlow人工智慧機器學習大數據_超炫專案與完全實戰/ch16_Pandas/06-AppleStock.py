#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data, wb
import pandas_datareader.data as web


import fix_yahoo_finance as yf
yf.pdr_override()

df = web.get_data_yahoo("AAPL", start="2018-01-01", end="2018-12-02")
print(df.head())
writer=pd.ExcelWriter('AAPL.xlsx')
df.to_excel(writer,'AAPL')
writer.save()




from pandas import ExcelWriter
writer = ExcelWriter('testaapl.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')

df.to_csv("testaapl.csv")