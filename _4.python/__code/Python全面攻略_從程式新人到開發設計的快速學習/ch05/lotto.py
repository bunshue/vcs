# -*- coding: utf-8 -*-
from random import randint
rand = set()

while (len(rand) < 7):
    rand.add(randint(1,49))
print ("本期樂透彩號碼：")
for idx,num in enumerate(rand, 1):
    print (f"({idx})={num}", end='  ')

