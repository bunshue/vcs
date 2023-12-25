MIN= 99999
num=int(input("準備輸入數字的個數："))
for i in range(num): #利用for迴圈來輸入與尋找最小值
    print(">",end="")
    temp=int(input())
    if MIN>temp:
        MIN=temp
print("這些數字中的最大小值為：%d" %MIN)
