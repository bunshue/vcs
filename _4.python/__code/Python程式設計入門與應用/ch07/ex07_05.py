# Filename: ex07_05.py
# 循序搜尋
#資料排序
def printdata(pdata):
    for item in pdata:
        print(item, end=" ")
    print()
def insert_search(pdata):
    #n=len(pdata)-1
    for i in range(1, len(pdata)): #第一個元素固定，從第二個開始
        tmp = pdata[i]
        j = i - 1 #固定元素的前一個數字
        while j >= 0 and tmp < pdata[j]:
            pdata[j + 1] = pdata[j] #值向右
            j = j - 1
        pdata[ j + 1 ] = tmp
    return pdata   
    
# main program
pdata = [128,246,732,945,489,242,647,819,935,767]
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
no = int(input("請輸入搜尋的編號(3位數字):"))
while (min<=max):
    mid=int((min+max)/2)
    c += 1
    if (pdata[mid]==no):
        isfound=True
        break
    if (pdata[mid]>no):
        max=mid-1
    else:
        min=mid+1
if (isfound==True):
    print("第%d個編號，編號為%d:"%(c,pdata[mid]))
else:
    print("無此數字!")
print("共比對%d次"%(c))