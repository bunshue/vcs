# Filename: ex03_08.py
# continue
n = int(input("請輸入正整數:"))
for i in range(1,n+1):
    if(i%7==0):
        continue
    print(i, end=" ")