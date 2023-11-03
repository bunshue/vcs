import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()

