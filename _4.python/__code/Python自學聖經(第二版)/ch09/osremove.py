import os
file = "myFile.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print(file + "檔案未建立!")   
 