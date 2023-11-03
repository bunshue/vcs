import random

val=0
data=[3,5,7,8,1,12,16,17,15,10,
      23,25,27,29,20,32,34,45,56,37]
      
while val!=-1:
    find=0
    val=int(input('請輸入搜尋鍵值(1-100)，輸入-1離開：'))
    for i in range(20):
        if data[i]==val:
            print('在第 %3d個位置找到鍵值 [%3d]' %(i+1,data[i]))
            find+=1
    if find==0 and val !=-1 :
        print('######沒有找到 [%3d]######' %val)
print('資料內容：')
for i in range(4):
    for j in range(5):
        print('%2d[%3d] ' %(i*5+j+1,data[i*5+j]),end='')
    print('')
