# ch3_30.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 正常顯示
x1 = np.linspace(-1.5,1.5,31)
y1 = np.cos(x1)**2

# 移除 y1 > 0.6 的點
x2 = x1[y1 <= 0.6]
y2 = y1[y1 <= 0.6]

# 遮罩 y1 > 0.7 的點
y3 = np.ma.masked_where(y1 > 0.7, y1)

# 將 y1 > 0.8 的點設為 NaN
y4 = y1.copy()
y4[y4 > 0.8] = np.nan

plt.plot(x1*0.1, y1, 'o-', label='正常顯示')
plt.plot(x2*0.4, y2, 'o-', label='移除點')
plt.plot(x1*0.7, y3, 'o-', label='遮罩點')
plt.plot(x1*1.0, y4, 'o-', label='將點設為NaN')
plt.legend()
plt.title('Cos函數顯示與遮蔽點的應用')
plt.show()




