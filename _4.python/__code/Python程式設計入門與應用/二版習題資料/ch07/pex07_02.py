# Filename: pex07_02.py
# 泡沫排序
def printdata():
    for item in pdata:
        print(item, end=" ")
    print()
# main program
# input data
pdata = []
while True:
    pinkey = input("請輸入數字[ENTER]結束：")
    if len(pinkey)>0:
        pdata.append(int(pinkey))
    else:
        break
print("泡沫排序前:",end=" ")
printdata()
n=len(pdata)-1
for i in range(0,n):
    for j in range(0,n-i):
        if (pdata[j]<pdata[j+1]):
            pdata[j],pdata[j+1]=pdata[j+1],pdata[j]
print("泡沫排序後:", end=" ")
printdata()