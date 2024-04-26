import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import sys
import linecache
import random

filename = 'C:/_git/vcs/_4.python/_data/王之渙_涼州詞.txt'
filename = 'C:/_git/vcs/_4.python/_data/song1.txt'
times = 5

getLines = linecache.getlines(filename)
print(getLines)

#print("取得{}檔案原內容：\n{}".format(filename), getLines)

for i in range(times):
    random.shuffle(getLines)

print("\n隨機抽取：", random.choice(getLines))


print("------------------------------------------------------------")  # 60個


name = "david"
age = 18

print(f"Hi, My name is {name}, I'm {age}")



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
