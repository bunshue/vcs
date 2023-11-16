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


print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\02-Pandas1_csv.py

#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import pandas as pd
df = pd.read_csv('ExpensesRecord.csv')
print(df.head(5) )
df.to_csv("test.csv")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\03-Pandas1_web.py

#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0].head(5) )


#df = pd.read_html('http://news.baidu.com/tech')
#print(df[0].head(5) )






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\04-Columns.py

# -*- coding: utf-8 -*-

__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
import numpy as np
DataFrame = pd.read_csv('ExpensesRecord.csv')
print(DataFrame["說明"])
print(DataFrame[["說明","支出金額"]] )


df = pd.DataFrame({'Math': [90, 91,92, 93, 94],'English': np.arange(80,85,1) })
print(df[["Math","English"]])


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\05-Math.py

# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
DataFrame = pd.read_csv('ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["數量","支出金額","單價"]] )



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\06-AppleStock.py

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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\07-AppleStock_info.py

#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\08-filter.py

#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'

print("--------------------")
print(df['Date'] == '2018-01-05')
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\09-calculation.py

#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())



# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch16_Pandas\10-matplot.py

#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())



# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())







#  5 matplotlib
import matplotlib.pyplot as plt
df.plot(x='Date', y='Open',grid=True, color='blue')
plt.show()


import matplotlib.pyplot as plt
df.plot( y='diff',grid=True, color='red',kind='hist')
plt.show()




fig, ax = plt.subplots()
for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
plt.show()

fileds=['Open','Close','High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
plt.show()

dfMonths = df.loc[df['month'].isin([1,2,3,4,5,6,7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values = 'High', columns = 'month', index = 'day')
dfMonthsPivot.plot(kind = 'box',title = 'Months High')
plt.show()



print('------------------------------------------------------------')	#60個

