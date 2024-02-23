# ex2_2.py
from array import *      

x = array('l', [1, 11, 22, 33, 44, 55])
print('陣列內容如下: ')
for data in x:
    print(data)
index = eval(input('請輸入欲刪除的索引 : '))
if index > 5 and index < 0:
    print("輸入錯誤")
else:
    x.pop(index)
    for data in x:
        print(data)







