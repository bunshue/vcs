# ch20_49.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (1.2-x**2+y**5)*np.exp(-x**2-y**2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 建立 2 個子圖
fig, ax = plt.subplots(1,2, figsize=(8,4))
# 繪製左圖 level 是預設
con = ax[0].contourf(X,Y,Z,cmap='Greens') # 填充輪廓圖
plt.colorbar(con,ax=ax[0])
oval = ax[0].contour(X,Y,Z,colors='b')    # 輪廓圖
ax[0].clabel(oval,colors='b')             # 增加高度標記
ax[0].set_title('指數函數等高圖level是預設',fontsize=16,color='b')
# 繪製右圖 level=12
ax[1].contourf(X,Y,Z,12,cmap='Greens')    # 填充輪廓圖
oval = ax[1].contour(X,Y,Z,12,colors='b') # 輪廓圖
ax[1].clabel(oval,colors='b')             # 增加高度標記
ax[1].set_title('指數函數等高圖level=12',fontsize=16,color='b')
plt.show()



      
