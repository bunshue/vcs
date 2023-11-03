import numpy as np 

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("a=")
print(a)
print("a 形狀: " + str(a.shape))
b = np.array([1,0,1])
print("b=" + str(b))
print("b 形狀: " + str(b.shape))

c = a + b
print(c)