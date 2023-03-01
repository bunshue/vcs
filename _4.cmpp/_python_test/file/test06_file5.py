#python讀和寫文件

filename_r = "poetry_long.txt"
filename_w = "poetry_another.txt"

with open(filename_r, 'rt') as f:
    data = f.read()
    
print("data :\n", data)

#關閉文件
f.close()

with open(filename_w, 'wt') as f:
    f.write(data)
    
#關閉文件
f.close()

import os.path
filesize = os.path.getsize(filename_r)
print("filesize : " , filesize)

print("檔案時間 : ", os.path.getmtime(filename_r))
import time
print("檔案時間 : ", time.ctime(os.path.getmtime(filename_r)))


print("檔案是否存在 : ", os.path.isfile(filename_r))

import os
files = os.listdir('.')
print("列出所有檔案", files)


import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

#countdown(1)

        


