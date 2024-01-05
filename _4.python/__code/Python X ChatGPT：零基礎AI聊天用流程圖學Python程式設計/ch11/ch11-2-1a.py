import os
 
path = os.getcwd()
new_path = os.getcwd() + "\\temp"
print("目前工作路徑: ", path)
print(new_path)
os.chdir(new_path)
print("chdir(): ", new_path)
os.mkdir('newDir')
print("mkdir(): ", os.listdir(new_path))
