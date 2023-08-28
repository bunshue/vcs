# ch2_13_2.py
import matplotlib.pyplot as plt

d1 = [1, 2, 3, 4, 5, 6, 7, 8]           # data1線條之y值
d2 = [1, 3, 6, 10, 15, 21, 28, 36]      # data2線條之y值
d3 = [1, 4, 9, 16, 25, 36, 49, 64]      # data3線條之y值
d4 = [1, 7, 15, 26, 40, 57, 77, 100]    # data4線條之y值

plt.plot(d1, '-')                       # 預設實線
plt.plot(d2, ':')                       # 虛點樣式
plt.plot(d3, '--')                      # 虛線樣式
plt.plot(d4, '-.')                      # 虛線點樣式
plt.show()


