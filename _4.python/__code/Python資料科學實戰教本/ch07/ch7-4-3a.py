import numpy as np 

a = np.array([[1,2],[3,4],[5,6]])
print("a=")
print(a)

mask = (a > 2)
print("mask=")
print(mask)
b = a[mask]           # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a > 2] = -1         # 同時更改多個True索引
print("a[a>2]=-1->")
print(a)

