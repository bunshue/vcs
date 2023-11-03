import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("a=")
print(a)

b = a[[0,1,2],[0,1,0]]   # 索引 [0,0][1,1][2,0]
print("a[[0,1,2],[0,1,0]]=")
print(b)
b = np.array([a[0,0],a[1,1],a[2,0]])  # 索引 [0,0][1,1][2,0]
print("np.array([a[0,0],a[1,1],a[2,0]])")
print(b)

idx = np.array([0, 2, 0, 1])
print("idx=" + str(idx))
b = a[np.arange(4), idx]     # 索引 [0,0][1,2][2,0][3,1]
print("a[np.arange(4),idx]=")
print(b)
a[np.arange(4), idx] += 10
print("a[np.arange(4), idx] += 10->")
print(a)
