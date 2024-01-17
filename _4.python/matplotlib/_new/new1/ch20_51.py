# ch20_51.py
import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return np.exp(-(0.5*X**2+0.5*Y**2))
def f2(x, y):                                # 右邊曲面函數
    return np.exp(-(0.1*X**2+0.1*Y**2))

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
np.random.seed(10)
c = np.random.rand(N, N)            # 取隨機色彩值
# 建立子圖
fig,ax = plt.subplots(1,3,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
sc = ax[0].scatter(X, Y, f1(X,Y), c=c, marker='o', cmap='hsv')
# 中間子圖乎叫 f2
sc = ax[1].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[1].set_axis_off()
# 右邊子圖乎叫 f2, 但是用不同的仰角和方位角
sc = ax[2].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[2].set_axis_off()
ax[2].view_init(60,-30)
ax[2].set_title(f"仰角={ax[2].elev},方位角={ax[2].azim}",color='b')

plt.show()



      
