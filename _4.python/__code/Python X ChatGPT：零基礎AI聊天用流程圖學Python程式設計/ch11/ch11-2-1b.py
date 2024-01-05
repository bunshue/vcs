import os
 
new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(new_path))
