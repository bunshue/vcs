str1="I love python."
print("原字串內容: ",str1)
print("轉換成串列: ",list(str1))
print("轉換成值組: ",tuple(str1))
print("字串長度: ",len(str1))

list1=[8,23,54,33,12,98]
print("原串列內容: ",list1)
print("串列中最大值: ",max(list1))
print("串列中最小值: ",min(list1))

relist=reversed(list1)#反轉串列
for i in relist: #將反轉後的串列內容依序印出
    print(i,end=' ')
print()#換行
print("串列所有元素總和: ",sum(list1))#印出總和
print("串列元素由小到大排序: ",sorted(list1))
