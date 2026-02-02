# ch4_9.py
import pandas as pd
cities = {'Country':['China','China','Thailand','Japan','Singapore'],
          'Town':['Beijing','Shanghai','Bangkok', 'Tokyo','Singapore'],
          'Population':[2000, 2300, 900, 1600, 600]}
df = pd.DataFrame(cities, columns=["Town","Population"],
                  index=cities["Country"])
print(df)









