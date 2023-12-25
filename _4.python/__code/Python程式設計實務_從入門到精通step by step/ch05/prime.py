n=int(input("請輸入n的值,n表示2~n之間的所有質數:"))
i=2;
while i<=n:
    no_prime=0
    for j in range(2,i,1):
        if i%j==0:
            no_prime=1
            break  #跳出迴圈
    if no_prime==0:
        print("%d " %i); #輸出質數
    i+=1
