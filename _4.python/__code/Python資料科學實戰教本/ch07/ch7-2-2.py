import numpy as np 

a = np.array([1, 2, 3, 4, 5]) 
b = np.array((1, 2, 3, 4, 5)) 
print(type(a), type(b))  
print("---------------------------")        
print(a[0], a[1], a[2], a[3], a[4])
print("---------------------------")
b[0] = 5    
print(b)
print("---------------------------")
b[4] = 0
print(b)    