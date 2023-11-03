import numpy as np 

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

b = a[1:3]     # 索引 1,2
print("a[1:3]=" + str(b))
b = a[:4]      # 索引 0,1,2,3
print("a[:4]=" + str(b))
b = a[3:]      # 索引 3,4,5,6,7,8
print("a[3:]=" + str(b))
b = a[2:9:3]   # 索引 2,5,8
print("a[2:9:3]=" + str(b))
b = a[::2]     # 索引 0,2,4,6,8
print("a[::2]=" + str(b))
b = a[::-1]    # 索引 8,7,6,5,4,3,2,1,0
print("a[::-1]=" + str(b))
b = a[2:-2]    # 索引 8,7,6,5,4,3,2,1,0
print("a[2:-2]=" + str(b))
