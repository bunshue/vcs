# ch4_21.py
import pandas as pd
import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Grapes', 'Pears', 'Oranges']
s = pd.Series([2300, 5000, 1200, 2500, 2900], index=fruits,
              name='Fruits Shop')
explode = [0.4, 0, 0, 0.2, 0]
s.plot.pie(explode = explode, autopct='%1.2f%%')
plt.show()













