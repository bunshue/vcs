# Filename: ex07_01.py
# 泡沫排序
def printdata():
    for item in pdata:
        print(item, end=" ")
    print()
# main program
pdata=[7,2,6,4]
print("泡沫排序前:",end=" ")
printdata()
n=len(pdata)-1

for i in range(0,n):
    for j in range(0,n-i):
        print("i=%d j=%d"%(i,j))
        if (pdata[j]>pdata[j+1]):
            print("%d, %d 互換後"%(pdata[j],pdata[j+1]), end="->")
            pdata[j],pdata[j+1]=pdata[j+1],pdata[j]
            print(pdata)
            
print("泡沫排序後:", end=" ")
printdata()