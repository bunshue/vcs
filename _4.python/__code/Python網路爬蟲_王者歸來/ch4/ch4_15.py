# ch4_15.py
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000, 850, 800, 1500, 600, 800],
          'town':['New York','Chicago','Bangkok','Tokyo',
                   'Singapore','HongKong']}
tw = pd.DataFrame(cities, columns=['population'],index=cities['town'])
          
tw.plot(title='Population in the World')
plt.xlabel('City')
plt.ylabel("Population")
plt.show()








