# ch4_21_7.py
import pandas as pd
from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)   
dates = [start + timedelta(days=x) for x in range(0, ndays)]
data1 = [34, 44, 65, 53, 39]
ts1 = pd.Series(data1, index=dates)

data2 = [34, 44, 65, 53, 39]
ts2 = pd.Series(data2, index=dates)

addts = ts1 + ts2
print("ts1+ts2")
print(addts)

meants = (ts1 + ts2)/2
print("(ts1+ts2)/2")
print(meants)










