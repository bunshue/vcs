import random

def bin_search(data,val):
    low=0
    high=49
    while low <= high and val !=-1:
        mid=int((low+high)/2)
        if val<data[mid]:
            print('%d 介於位置 %d[%3d]及中間值 %d[%3d]，找左半邊' \
                   %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print('%d 介於中間值位置 %d[%3d] 及 %d[%3d]，找右半邊' \
                  %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1

val=1
data=[0]*50
for i in range(50):
    data[i]=val
    val=val+random.randint(1,5)

while True:
    num=0
    val=int(input('請輸入搜尋鍵值(1-150)，輸入-1結束：'))
    if val ==-1:
        break
    num=bin_search(data,val)
    if num==-1:
        print('##### 沒有找到[%3d] #####' %val)
    else:
        print('在第 %2d個位置找到 [%3d]' %(num+1,data[num]))

print('資料內容：')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d' %(i*10+j+1,data[i*10+j]), end='')
    print()
