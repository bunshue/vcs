import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
s = pd.Series(data, index=weekday)
s.plot()
plt.show()

'''
weight = [3, 48,33,8,38,16,36,29,22,6,12,42]
animals = ["鼠牛虎兔龍蛇馬羊猴雞狗豬"]
'''


