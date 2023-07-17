import os
dir = "myDir"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + "已經存在!")   
 