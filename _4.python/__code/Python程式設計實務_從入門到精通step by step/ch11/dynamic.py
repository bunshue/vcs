#[示範]:費伯那序列的動態規劃法

output=[0]*100

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        output[0]=0
        output[1]=1
        for i in range(2,n+1):
            output[i]=output[i-1]+output[i-2]
    return output[n]

n=int(input("請輸入所要計算第幾個費式數列:"))
print(fib(n))
    


