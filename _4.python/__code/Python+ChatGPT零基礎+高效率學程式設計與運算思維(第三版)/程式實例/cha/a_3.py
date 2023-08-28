# a_3.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 可以顯示中文
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10)    # 串列squares數據是y軸的值, 線條寬度是10
plt.title('圖表')
plt.xlabel('X 軸值')
plt.ylabel('平方')
plt.show()


