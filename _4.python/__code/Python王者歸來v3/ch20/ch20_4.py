# ch20_4.py
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]       # data1線條
data2 = [1, 3, 6, 10, 15, 21, 28, 36]       # data2線條
seq = [1,2,3,4,5,6,7,8]
plt.plot(seq, data1, seq, data2)            # data1&2線條
plt.title("Test Chart")                     # 字型大小是預設
plt.xlabel("x-Value")                       # 字型大小是預設
plt.ylabel("y-Value")                       # 字型大小是預設
plt.show()


