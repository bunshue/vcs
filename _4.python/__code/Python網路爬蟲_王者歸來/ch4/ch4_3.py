# ch4_3.py
import pandas as pd
years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index = years)
hongkong = pd.Series([25, 26, 27], index = years)
singapore = pd.Series([30, 29, 31], index = years)
citydf = pd.concat([beijing, hongkong, singapore],axis=1)  # axis=1
cities = ["Beijing", "HongKong", "Singapore"]
citydf.columns = cities
print(citydf)





