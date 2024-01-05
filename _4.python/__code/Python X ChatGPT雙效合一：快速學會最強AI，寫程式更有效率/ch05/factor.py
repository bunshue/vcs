a=1
n=int(input("請輸入一個整數數字："))
print("%d的所有正因數為:" %n)
while a<=n:
    if n%a==0: #當n能夠被a整除時~則a就是n的因數
        print(a,end="")
        if n!=a: print(",",end="")
    a+=1 #a值遞增1
