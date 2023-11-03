import numpy as np 

a = np.array([14,8,10,11,6,3,18,13,12,9])
print("a=" + str(a))
mask = (a % 3 == 0)        # 建立布林值陣列
print("mask=" + str(mask))
b = a[mask]                # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a % 3 == 0] = -1         # 同時更改多個True索引
print("a[a%3==0]=-1->" + str(a))