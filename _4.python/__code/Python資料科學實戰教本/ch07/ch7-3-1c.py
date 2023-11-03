import numpy as np 

a = np.array([1, 2, 3]) 
print("c=" + str(a))
s = np.array([4, 5, 6])  
print("s=" + str(s))
b = np.add(a, s)       
print("np.add(a,s)=" + str(b))    
b = np.subtract(a, s)       
print("np.subtract(a,s)=" + str(b))   
b = np.multiply(a, s)       
print("np.multiply(a,s)=" + str(b))  
b = np.divide(a, s)       
print("np.divide(a,s)=" + str(b))  