# coding:utf-8
# 猜數字：大小區間簡單版

import random

a = -1
b = int(random.random()*100)
print(b)
while(a != b):
    a = int(input('請輸入一個數字'))
    if(a > b):
        print('太大囉')
    elif(a < b):
        print('太小囉')
    else:
        print('答對了！就是 ' + str(b))

print('程式結束')
