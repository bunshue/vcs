# ex20_6.py
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條
data5 = [1, 6, 11, 16, 21, 26, 31, 36]          # data5線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 3, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 3, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 3, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 3, 4)
plt.plot(seq, data4, '-s')

plt.subplot(2, 3, 6)
plt.plot(seq, data5, '-v')

plt.show()


