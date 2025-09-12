import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

# 24 Exploring data

import pandas as pd
import numpy as np

mars = pd.read_json("mars_data_01.json")
print(mars)

temp = pd.read_csv("temp_data_01.csv", header=0, names=range(18), usecols=range(4,18))

print(temp)

temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'])
print(temp)

temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'], header=0, names=range(18), usecols=range(4,18))
print(temp)

calls = pd.read_csv("sales_calls.csv")
print(calls)

revenue = pd.read_csv("sales_revenue.csv")
print(revenue)

calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
print(calls_revenue)

print(calls_revenue[calls_revenue.Territory==3])

print(calls_revenue[calls_revenue.Amount/calls_revenue.Calls>500])


calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls
print(calls_revenue)

# 24.5.3 Grouping and aggregation

print(calls_revenue.Calls.sum())
print(calls_revenue.Calls.mean())
print(calls_revenue.Calls.median())
print(calls_revenue.Calls.max())
print(calls_revenue.Calls.min())

print(calls_revenue.Call_Amount.median())
print(calls_revenue[calls_revenue.Call_Amount >= calls_revenue.Call_Amount.median()])

print(calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum())

print(calls_revenue[['Territory', 'Calls', 'Amount']].groupby(['Territory']).sum())

# 24.6 Plotting data

calls_revenue[['Territory', 'Calls']].groupby(['Territory']).sum().plot.bar()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



