import numpy as np 

a = np.random.rand(5)
print("np.random.rand(5)=")
print(a)
b = np.random.rand(3, 2)  
print("np.random.rand(3,2)=")
print(b)
c = np.random.randint(5, 10, size=5)
print("np.random.randint(5,10,size=5)")
print(c)
d = np.random.randint(5, 10, size=(2,3))
print("np.random.randint(5,10,size=(2,3))")
print(d)