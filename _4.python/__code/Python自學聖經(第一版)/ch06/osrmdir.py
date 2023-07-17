import os
dir = "myDir"
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir + "目錄未建立!")  
 