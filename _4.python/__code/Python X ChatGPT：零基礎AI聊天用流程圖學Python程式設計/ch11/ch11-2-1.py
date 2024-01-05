import os
 
path = os.getcwd() + "\\temp"
os.chdir(path)
print(path)
print(os.listdir(path))
