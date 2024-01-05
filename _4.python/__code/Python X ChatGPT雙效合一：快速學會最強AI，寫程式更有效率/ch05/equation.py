total=0
n=int(input("請輸入任一整數:"))
if n>=1 or n<=100:
    for i in range(n+1):
        total+=i*i  #1*1+2*2+3*3+..n*n
    print("1*1+2*2+3*3+...+%d*%d=%d" %(n,n,total))
else:
    print("輸入數字超出範圍了!")
