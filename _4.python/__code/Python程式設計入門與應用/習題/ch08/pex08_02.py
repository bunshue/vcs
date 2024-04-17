# Filename: pex08_02.py
from random import randint
import os.path

pfile = input("請輸入檔名：").strip()
if os.path.isfile(pfile):
    print("此檔案已經存在，程式終止")
else:
    poutfile = open(pfile, "w")
        
    for i in range(100):
        print(randint(0, 999), file = poutfile, end = " ")
       
    poutfile.close()
        
    pinfile = open(pfile, "r")
    ps = pinfile.read()
    
    pnumber = [eval(items) for items in ps.split()]
    pnumber.sort()
        
    for i in range(len(pnumber)):
        print(pnumber[i], end = " ")
            
    pinfile.close()