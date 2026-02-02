# ch4_18.py
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[10000000,8500000,8000000,15000000,6000000,8000000],
          'area':[400, 500, 850, 300, 200, 320],
          'town':['New York','Chicago','Bangkok','Tokyo',
                   'Singapore','HongKong']}
tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])
          
tw.plot(title='Population in the World')
plt.xlabel('City')
plt.show()








