import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('載入字型範例')

'''
我們這裡以翰字鑄造的台北黑體為例, 這裡選了 regular 的版本。

TaipeiSansTCBeta-Regular.ttf 

https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
'''

import matplotlib as mpl
import matplotlib.font_manager as fm
fm.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

#把預設狀態存起來
saved_state = mpl.rcParams.copy()

#plt.xkcd()  #搞笑風格

#多此兩行 變成海生風格
import seaborn as sns
sns.set()

x = np.linspace(-5, 5, 200)
y = np.sinc(x)

plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個


plt.plot(x, y)

plt.show()




print('------------------------------------------------------------')	#60個

mpl.rcParams.update(saved_state)

plt.plot(x, y)

plt.show()


print('------------------------------------------------------------')	#60個

#試著做三群的數據。

cx0 = 0
cy0 = 0

cx1 = -3
cy1 = 3

cx2 = 3
cy2 = 3

#每一群都是 500 個點

x0 = np.random.randn(500) + cx0
y0 = np.random.randn(500) + cy0

x1 = np.random.randn(500) + cx1
y1 = np.random.randn(500) + cy1

x2 = np.random.randn(500) + cx2
y2 = np.random.randn(500) + cy2

#合併三群的點到 x, y 之中。
x = np.concatenate((x0, x1, x2))
y = np.concatenate((y0, y1, y2))


c = np.repeat([0,1,2], 500)

plt.scatter(x, y, c=c, cmap='Set1')

plt.show()


print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt 

#x，y，大小，颜色
plt.scatter([1,2,3,4],[2,4,6,8],[10,20,30,400],['r', 'b','y','k'])   
plt.scatter([1,2,3,4],[9,8,7,6],s=10,c='b', marker='v')   

plt.show()


print('------------------------------------------------------------')	#60個
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

