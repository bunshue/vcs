import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


# ch23_1.ipynb
#!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
import matplotlib as mpl
from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額

print(f"相關係數 = {np.corrcoef(temperature,rev).round(2)}")
plt.scatter(temperature, rev)
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()


print('------------------------------------------------------------')	#60個



# ch23_2.ipynb
import numpy as np

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(coef.round(2))
print(reg)         

print('------------------------------------------------------------')	#60個


# ch23_3.ipynb
import numpy as np

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")


print('------------------------------------------------------------')	#60個


# ch23_4.ipynb
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
import matplotlib as mpl
from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
     
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()



print('------------------------------------------------------------')	#60個

# ch23_5.ipynb
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
import matplotlib as mpl
from matplotlib.font_manager import fontManager
import matplotlib.pyplot as plt
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
temperature = [22,25,26,27,28,29,30,31,32,33]           # 天氣溫度
rev = [600,900,1100,720,950,1020,1000,1200,1420,1500]   # 營業額

coef = np.polyfit(temperature, rev, 2)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(reg)     
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





