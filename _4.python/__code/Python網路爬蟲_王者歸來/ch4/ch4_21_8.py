# ch4_21_8.py
import pandas as pd
from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)   
dates1 = [start + timedelta(days=x) for x in range(0, ndays)]
data1 = [34, 44, 65, 53, 39]
ts1 = pd.Series(data1, index=dates1)

dates2 = [start - timedelta(days=x) for x in range(0, ndays)]
data2 = [34, 44, 65, 53, 39]
ts2 = pd.Series(data2, index=dates2)

addts = ts1 + ts2
print("ts1+ts2")
print(addts)











