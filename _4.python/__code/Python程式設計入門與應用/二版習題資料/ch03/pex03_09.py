# Filename: pex03_09.py
pnum = int(input("請輸入一個整數:"))
print("整數%d"%(pnum),end="")
prev = 0
while(pnum > 0):
    prem = pnum % 10
    prev = (prev*10)+prem
    pnum = pnum //10
print("反轉順序為%d"%(prev))

# Filename: pex03_09.py
pnum = int(input("請輸入一個整數:"))
print("整數:%d"%(pnum))
print("反轉整數為:",end="")
while(pnum != 0):
    print(pnum%10,end="")
    pnum = pnum//10