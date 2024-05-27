# -*- coding: utf-8 -*-
from random import randint

def getRan(i, lstA):
    while (i > 0):
        lstA.append(randint(40, 100))
        i -= 1
    
lst1 = []
i = int(input("請輸入數量："))
getRan(i, lst1)
print(lst1)
print(i)
