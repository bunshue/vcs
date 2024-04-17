# Filename: pex03_031.py
num = int(input("請輸入繪製層數:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")