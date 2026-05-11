import os

path = os.getcwd() + "/temp"
os.chdir(path)
print(path)
print(os.listdir(path))
os.mkdir('newDir')
print("mkdir(): ", os.listdir(path))
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(path))
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(path))
os.remove("aa.txt")
print("remove(): ", os.listdir(path))
