# ch2_14.py
import matplotlib.pyplot as plt

d1 = [1, 2, 3, 4, 5, 6, 7, 8]           # data1線條之y值
d2 = [1, 3, 6, 10, 15, 21, 28, 36]      # data2線條之y值
d3 = [1, 4, 9, 16, 25, 36, 49, 64]      # data3線條之y值
d4 = [1, 7, 15, 26, 40, 57, 77, 100]    # data4線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq,d1,'-',marker='x')
plt.plot(seq,d2,'-',marker='o')
plt.plot(seq,d3,'-',marker='^')
plt.plot(seq,d4,'-',marker='s') 
plt.show()


