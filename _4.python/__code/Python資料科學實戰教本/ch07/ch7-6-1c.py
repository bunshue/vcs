import numpy as np 

a = np.array([1,2,3])
print("a=" + str(a))

b = a.copy()
print("b=a.copy()->" + str(b))
b.fill(4)
print("b.fill(0)=" + str(b))
c = np.concatenate((a,b))
print("c=np.concatenate((a,b))->" + str(c))
