# Filename: pex07_03.py
def printdata(pdata):
    for item in pdata:
        print(item, end=" ")
    print()
def insert_search(pdata):
    for i in range(1, len(pdata)): #第一個元素固定，從第二個開始
        tmp = int(pdata[i])
        j = i - 1 #固定元素的前一個數字
        while j >= 0 and tmp < int(pdata[j]):
            pdata[j + 1] = pdata[j] #值向右
            j = j - 1
        pdata[ j + 1 ] = str(tmp)
    return pdata      
# main program
pdata = ["055","816","292","891","491","437"]
print("原始資料:",end=" ")
printdata(pdata)
pdata = insert_search(pdata)
print("排序資料:", end=" ")
printdata(pdata)
# 開始搜尋
n=len(pdata)-1
isfound=False
min=0
max=n
c=0
no = input("請輸入中獎者的號碼：")
while (min<=max):
    mid=int((min+max)/2)
    c += 1
    if (int(pdata[mid])==int(no)):
        isfound=True
        break
    if (int(pdata[mid])>int(no)):
        max=mid-1
    else:
        min=mid+1
if (isfound==True):
    print("第%d個號碼，號碼為%s:"%(c,pdata[mid]))
else:
    print("無此中獎號碼！")
print("共比對%d次"%(c))