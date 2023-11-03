import numpy as np 

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

print(a[0], a[2], a[-1])  # 索引 0,2,最後1個 
b = a[[1, 3, 5, 7]]       # 索引 1,3,5,7
print("a[[1,3,5,7]]=" + str(b))
b = a[range(6)]           # 索引 0,1,2,3,4,5
print("a[range(6)]=" + str(b))
a[[2, 6]] = 10            # 同時更改多個索引值
print("a[[2,6]]=10->" + str(a))