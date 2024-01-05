def fib(n):	# 定義函數fib()
    if n==0 :
        return 0 # 如果n=0 則傳回 0
    elif n==1 or n==2:
        return 1
    else:   # 否則傳回 fib(n-1)+fib(n-2)
        return (fib(n-1)+fib(n-2))

n=int(input('請輸入所要計算第幾個費式數列:'))
for i in range(n+1):# 計算前n個費氏數列
    print('fib(%d)=%d' %(i,fib(i)))
