import numpy as np 

a = np.arange(11,36)
a = a.reshape(5,5)
print("a=")
print(a)

b = a[0, 1:4]     # 索引 [0,1~3]
print("a[0,1:4]=")
print(b)
b = a[1:4, 0]     # 索引 [1~3,0]
print("a[1:4,0]=")
print(b)
b = a[:2, 1:3]    # 索引 [0~1,1~2]
print("a[:2,1:3]=")
print(b)
b = a[:,1]        # 索引 [0~4,1]
print("a[:,1]=")
print(b)
b = a[::2, ::2]   # 索引 [0~2~4,0~2~4]
print("a[::2,::2]=")
print(b)