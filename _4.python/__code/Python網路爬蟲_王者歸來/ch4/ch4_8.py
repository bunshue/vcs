# ch4_8.py
import pandas as pd
cities = {'country':['China', 'Japan', 'Singapore'],
          'town':['Beijing','Tokyo','Singapore'],
          'population':[2000, 1600, 600]}
citydf = pd.DataFrame(cities, columns=["town","population"],
                      index=cities["country"])
print(citydf)









