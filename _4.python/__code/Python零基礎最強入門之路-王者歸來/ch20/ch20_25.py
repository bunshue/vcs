# ch20_25.py
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.subplot(2, 1, 1)                            # 子圖1
plt.plot(seq, data1, '-*')
plt.subplot(2, 1, 2)                            # 子圖2
plt.plot(seq, data2, '-o')                      
plt.show()



