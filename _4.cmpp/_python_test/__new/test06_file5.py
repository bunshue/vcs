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



#撰寫接受任意數目引數的函式
def avg(first, *rest):
    return (first + sum(rest)) / (1+len(rest))

a = avg(1,2)
b = avg(1,2,3,4)

print("average 1", a, "\n")
print("average 2", b, "\n")



t = time.localtime()
print(t)
print("年" , t.tm_year)
print("月" , t.tm_mon)
print("日" , t.tm_mday)
print("星" , t.tm_wday)
print("時" , t.tm_hour)
print("分" , t.tm_min)
print("秒" , t.tm_sec)


import sys
print("目前路徑 : ", sys.path)


import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

#countdown(1)


def add(x,y):
    return x+y

z = add(1234,5678)
print(z)




        


