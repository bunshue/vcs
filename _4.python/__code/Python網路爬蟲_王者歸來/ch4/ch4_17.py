# ch4_17.py
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000, 850, 800, 1500, 600, 800],
          'area':[400, 500, 850, 300, 200, 320],
          'town':['New York','Chicago','Bangkok','Tokyo',
                   'Singapore','HongKong']}
tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])
          
tw.plot(title='Population in the World')
plt.xlabel('City')
plt.show()








