total=0
n1=1
n=int(input("請輸入任一整數:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        n1*=j #n!的值
    total+=n1 #1!+2!+3!+..n!
    n1=1
print("1!+2!+3!+...+%d!=%d" %(n,total))
