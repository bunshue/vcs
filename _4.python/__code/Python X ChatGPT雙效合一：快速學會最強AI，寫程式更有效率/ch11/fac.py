def factorial(i):
    if i==0:
        return 1
    else:
        ans=i * factorial(i-1)  #反覆執行的遞迴過程
    return ans 

n=int(input('請輸入要計算的階乘數值: '))
print('%d!=%d' %(n,factorial(n)))
