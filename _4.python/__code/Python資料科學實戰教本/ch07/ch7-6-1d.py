import numpy as np 

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.concatenate((a,b))
print("c=np.concatenate((a,b))->")
print(c)
c = np.concatenate((a,b), axis=0)
print("c=np.concatenate((a,b), axis=0)->")
print(c)
c = np.concatenate((a,b), axis=1)
print("c=np.concatenate((a,b), axis=1)->")
print(c)