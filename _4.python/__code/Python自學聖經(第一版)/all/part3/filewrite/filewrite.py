import os
import sys

def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

tmp=base_path("") #取得暫存目錄
cwd=os.getcwd()   #取得目前的工作目錄

file1="file1.txt"
file2=os.path.join(tmp,"file2.txt")
file3=os.path.join(cwd,"file3.txt")

f1=open(file1,'w')  #寫入工作目錄
f1.write("file1 txt")
f1.close()
print(file1,"寫入成功!")

f2=open(file2,'w')  #寫入 tmp 目錄
f2.write("file2 txt")
f2.close()
print(file2,"寫入成功!")

f3=open(file3,'w') #寫入 pwd 目錄
f3.write("file3 txt")
f3.close()
print(file3,"寫入成功!")

key=input("按任意鍵結束!")
