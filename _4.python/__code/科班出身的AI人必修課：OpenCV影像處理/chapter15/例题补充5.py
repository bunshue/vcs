# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:49:50 2018

@author:  天津职业技术师范大学  
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
t = (x,y,z)
print(t)
for i in zip(*t):
    print(i)

