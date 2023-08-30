import numpy as np

list2d =np.arange(18).reshape(3,6)
print(list2d)
h,w=list2d.shape[::]
print(h,w)
w,h=list2d.shape[::-1]
print(w,h)
