import os
import os.path as path
 
fpath = os.getcwd() + "\\temp"
if path.exists(fpath+"\\ball0.jpg"):
    print("存在!")
if path.isdir(fpath+"\\test"):
    print("是目錄!")
if path.isfile(fpath+"\\ball0.jpg"):
    print("是檔案!")
