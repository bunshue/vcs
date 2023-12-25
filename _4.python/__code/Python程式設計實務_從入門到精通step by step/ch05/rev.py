n=int(input("請輸入任一整數:"))
print("反向輸出的結果:",end="")
while n!=0:
    print("%d" %(n%10),end="") #求出餘數值
    n//=10
print()
