a=1
n=int(input("請輸入一個數字："))
print("%d 的所有因數為:" %n,end="")
while a<=n: #定義while迴圈,且設定條件為a<=n
    if n%a==0: #當n能夠被a整除時~則a就是n的因數
        print("%d " %a,end="")
        if n!=a: print(",",end="")
    a+=1 #a值遞增1
