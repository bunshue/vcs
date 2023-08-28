# ch30_8.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 定義資料資料
x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 用 3D 線框繪製曲線表面
ax.plot_wireframe(X, Y, Z, color = 'm')
ax.set_title('wireframe( )函數的實例',fontsize=16,color='b');
plt.show()



 




