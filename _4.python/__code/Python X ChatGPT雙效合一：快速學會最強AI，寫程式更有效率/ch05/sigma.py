k=int(input("請輸入k值："))
sigma=0
for n in range(int(k)+1):
    if(n % 2!=0): #如果n是奇數
        sigma += float(-1/(2*n+1))
    else:  #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))
