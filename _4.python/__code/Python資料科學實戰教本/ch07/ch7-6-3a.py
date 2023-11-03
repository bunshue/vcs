import numpy as np 

a = np.array([1.0,5.55, 123, 0.567, 25.532]) 
print("a=" + str(a))

print(np.around(a))
print(np.around(a, decimals = 1))
print(np.around(a, decimals = -1))

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print("a=" + str(a))

b = np.floor(a)
print("floor()=" + str(b))
b = np.ceil(a)
print("ceil()=" + str(b))