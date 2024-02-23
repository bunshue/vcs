import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(1,100,20)
bx = np.linspace(1,20,200)

ay = ax
by = np.sin(bx)

# 產生子圖表，第一個數值為縱軸要有幾張圖，第二個數值為橫軸，第三個數值為排在哪裡
plt.subplot(2,  1,  1) 
plt.plot(ax, ay) 
plt.title('a') 
plt.xlabel("ax")
plt.ylabel("ay") 


plt.subplot(2,  1,  2) 
plt.plot(bx, by) 
plt.title('b') 
plt.xlabel("bx")
plt.ylabel("by") 

plt.show()


