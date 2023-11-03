import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)
s = 5 
print("s=" + str(s))
b = np.add(a, s)       
print("np.add(a,s)=")
print(b)    
b = np.subtract(a, s)       
print("np.subtract(a,s)=")
print(b)   
b = np.multiply(a, s)       
print("np.multiply(a,s)=")
print(b)  
b = np.divide(a, s)       
print("np.divide(a,s)=")
print(b)  