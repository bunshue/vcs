sigma=0
k=int(input("請輸入k值：")) #輸入k值
for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))
