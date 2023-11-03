import numpy as np

a = np.array([[11,22,13,74,35,6,27,18]])

min_value = np.min(a)
max_value = np.max(a)
print("最小值: " + str(min_value))
print("最大值: " + str(max_value))

min_idx = np.argmin(a)
max_idx = np.argmax(a)
print("最小值索引: " + str(min_idx))
print("最大值索引: " + str(max_idx))