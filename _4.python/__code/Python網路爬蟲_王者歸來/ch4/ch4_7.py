# ch4_7.py
import pandas as pd
cities = {'country':['China', 'Japan', 'Singapore'],
          'town':['Beijing','Tokyo','Singapore'],
          'population':[2000, 1600, 600]}
rowindex = ['first', 'second', 'third']
citydf = pd.DataFrame(cities, index=rowindex)
print(citydf)









