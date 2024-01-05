data=[16,25,39,27,12,8,45,63]	# 原始資料
print('氣泡排序法：原始資料為：')
for i in range(len(data)):
    print('%3d' %data[i],end='')
print()

for i in range(len(data)-1,0,-1): #掃描次數
    for j in range(i):
        if data[j]>data[j+1]:#比較,交換的次數
            data[j],data[j+1]=data[j+1],data[j]#比較相鄰兩數,如果第一數較大則交換
    print('第 %d 次排序後的結果是：' %(len(data)-i),end='') #把各次掃描後的結果印出
    for j in range(len(data)):
        print('%3d' %data[j],end='')
    print()
	
print('排序後結果為：')
for j in range(len(data)):
    print('%3d' %data[j],end='')
print()
