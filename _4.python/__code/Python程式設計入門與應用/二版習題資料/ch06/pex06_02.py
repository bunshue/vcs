# Filename: pex06_02.py
import random as r
list1 = r.sample(range(1,50),7)
print(list1)
special = list1.pop()
print(special)
list1.sort()
print("本期大樂透中獎號碼為:", end="")
for i in range(0,6):
    if (i==5):
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=",")
print("本期大樂透特別號為:"+str(special))