import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import datetime
today = datetime.date.today()
print('今天的日期 :', today)



print("------------------------------------------------------------")  # 60個

print("enumerate() 一個串列")

animals = ['鼠', '牛', '虎', '兔']

print('用 for')
for _ in enumerate(animals):
    print(_)

print('用 list')
print(list(enumerate(animals)))

print('用 unpacking 取出內容')

for index, ani in enumerate(animals):
    print(index, ani)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
