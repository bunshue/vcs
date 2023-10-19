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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

