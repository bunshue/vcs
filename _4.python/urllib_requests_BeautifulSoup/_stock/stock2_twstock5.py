# Python 測試 twstock 5

import twstock
import time
import requests

import matplotlib.pyplot as plt

from twstock import Stock
tsmc = Stock('2330')
print(tsmc.price)

print('------------------------------------------------------------')	#60個

from twstock import Stock
tsmc = Stock('2330')
print(tsmc.moving_average(tsmc.price, 5))
print(tsmc.moving_average(tsmc.capacity, 5))

print('------------------------------------------------------------')	#60個

from twstock import Stock
tsmc = Stock('2330')
data = tsmc.moving_average(tsmc.price, 5)
plt.plot(list(range(len(data))), data)

plt.show()

print('------------------------------------------------------------')	#60個

