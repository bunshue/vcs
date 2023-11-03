# ch20_24.py
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.figure(1)                                   # 建立圖表1              
plt.plot(seq, data1, '-*')                      # 繪製圖表1
plt.figure(2)                                   # 建立圖表2
plt.plot(seq, data2, '-o')                      # 以下皆是繪製圖表2
plt.title("Test Chart 2", fontsize=24)
plt.xlabel("x-Value", fontsize=14)
plt.ylabel("y-Value", fontsize=14)
plt.show()



