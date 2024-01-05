import os
 
new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(new_path))
os.remove("aa.txt")
print("remove(): ", os.listdir(new_path))
