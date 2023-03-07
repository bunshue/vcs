# Python 新進測試 12

import glob
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for file in files:
    print(file)
    

import os
cur_path=os.path.dirname(__file__) # 取得目前目錄路徑
print("現在目錄路徑："+cur_path)


import os
print(os.getcwd())   
 

import os
filename=os.path.abspath("test10_new10.py")
if os.path.exists(filename): #檢查檔案是否存在
    print("完整路徑名稱：" + filename)
    print("檔案大小：" , os.path.getsize(filename))
    

import os,shutil
cur_path=os.path.dirname(__file__) # 取得目前路徑
destfile= cur_path + "\\" + "test10_new1022222.py"
print("拷貝檔案 " + destfile)
shutil.copy("test10_new10.py",destfile )  # 檔案複製
print("拷貝檔案 " + destfile)
shutil.copyfile("test10_new10.py","C:\\dddddddddd\\new.py" )  # 檔案複製



import os,shutil
cur_path=os.path.dirname(__file__) # 取得目前路徑
destfile= cur_path + "\\" + "newfile.py"
shutil.copy("test10_new10.py",destfile )  # 檔案複製
shutil.copyfile("test10_new10.py","C:\\dddddddddd\\new2.py" )  # 檔案複製



import os
cur_path=os.getcwd() # 取得目前路徑  
os.system("cls")  # 清除螢幕
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案 
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔



import os
foldername = "myDir"
if os.path.exists(foldername):
    os.rmdir(foldername)
else:
    print(foldername + "目錄未建立!")  

 
import os
filename = "myFile.txt"
if os.path.exists(filename):
    os.remove(filename)
else:
    print(filename + "檔案未建立!")   


import os
filename=os.path.abspath("ospath.py")
if os.path.exists(filename):   
    basename=os.path.basename(filename)
    print("最後的檔案或路徑名稱：" + basename)
    
    dirname=os.path.dirname(filename)
    print("目前檔案目錄路徑：" + dirname) 
    
    print("是否為目錄：",os.path.isdir(filename))
    
    fullpath,fname=os.path.split(filename)
    print("目錄路徑：" + fullpath)
    print("檔名：" + fname)
    
    Drive,fpath=os.path.splitdrive(filename)
    print("磁碟機：" + Drive)
    print("路徑名稱：" + fpath)   
    
    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑= " + fullpath)




print("測試mkdir")
import os
dir = "myDir"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + "已經存在!")   


print("刪除目錄, 直接刪除, 不會放入資源回收筒")
import shutil
shutil.rmtree("C:\\dddddddddd\\aaa" )  # 刪除目錄



#import ast
import json
data = dict()
with open('password.txt','r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)
print(type(data),data)




   
