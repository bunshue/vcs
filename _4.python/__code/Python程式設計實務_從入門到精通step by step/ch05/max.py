MAX= 0
num=int(input("準備輸入數字的個數："))
for i in range(num): #利用for迴圈來輸入與尋找最大值
    print(">",end="")
    temp=int(input())
    if MAX<temp:
        MAX=temp
print("這些數字中的最大值為：%d" %MAX)
