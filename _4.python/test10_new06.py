import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import numpy as np

N = 5


'''
#plt.plot(np.random.randn(N))
plt.plot(range(N), np.random.randn(N))
plt.scatter(range(N), np.random.randn(N))
'''

ccc = np.random.randn(N)

print(type(ccc))
print(len(ccc))
print(ccc)
print(max(ccc))
print(min(ccc))



print('------------------------------------------------------------')	#60個

'''
import datetime

dt = datetime.datetime.strptime('ttttt', '%Y-%m-%dT%H:%M')  #讀取日期時間
dt = dt.strftime('{d}%Y-%m-%d, {t}%H:%M').format(d='日期為：', t='時間為：')  #轉為字串
'''




print('------------------------------------------------------------')	#60個





from calendar import monthrange

day_start, num_days = monthrange(2023, 10)
    
print('本月的第一天為星期 :', day_start)
print('本月的天數 :', num_days)







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



