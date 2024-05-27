# -*- coding: utf-8 -*-
import func

lst1 = [62, 47, 36, 53, 100]
print (f"原始資料={lst1}")
print ("方法一調整後的數值")
for x in range(len(lst1)):
    print(func.func1(lst1[x]), end = '  ')
    
print ()
print ("方法二調整後的數值")
for x in range(len(lst1)):
    print(func.func2(lst1[x]), end = '  ')
