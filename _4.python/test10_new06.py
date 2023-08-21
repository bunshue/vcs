'''
import numpy as np
import matplotlib.pyplot as plt


from datetime import date, timedelta

d0 = date(1993, 12, 15)
d1 = date(2020, 12, 15)

delta = timedelta(days=1)

print(d0 + delta)

delta = timedelta(days=10000)

print(d0 + delta)

print(d1-d0)

d0 = date(2021, 5, 24)
d1 = date(2023, 8, 21)

print(d1-d0)
'''


import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

x = np.arange(5)
height = [90, 175, 110, 186, 125]

plt.xkcd()  #xkcd漫畫風格

plt.bar(x, height)

plt.xticks(x, ('apple', 'banana', 'cat', 'dog', 'elephant'))

'''
#plt.plot(x, y)

plt.xkcd()

plt.plot(x,y)
'''

plt.show()








