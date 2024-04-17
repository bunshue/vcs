# Filename: pex03_032.py
num = int(input("請輸入繪製層數:"))   
for i in range(0,num+1,1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")