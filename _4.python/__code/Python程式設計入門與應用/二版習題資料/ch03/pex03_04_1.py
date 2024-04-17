# Filename: pex03_041.py
num = int(input("請輸入繪製層數:"))
pend = int(num/2+0.5)
for i in range(0,pend+1,1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")
pend = int(num/2)    
for i in range(pend, 0, -1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")