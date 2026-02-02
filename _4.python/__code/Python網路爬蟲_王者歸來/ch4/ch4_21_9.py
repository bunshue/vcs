# ch4_21_9.py
import pandas as pd

dates = pd.date_range('3/11/2019', '3/15/2019')
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index=dates)
print(type(ts))
print(ts)










