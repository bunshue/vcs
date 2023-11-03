import numpy as np 

a = np.array([1,2,3,4,5,6])
print("a=" + str(a))

b = np.reshape(a,(3,2))
print("b=np.reshape(a,(3,2))->")
print(b)
c = b.T
print("c=b.T->")
print(c)
c = b.transpose()
print("c=b.transpose()->")
print(c)
c = np.transpose(b)
print("c=np.transpose(b)->")
print(c)