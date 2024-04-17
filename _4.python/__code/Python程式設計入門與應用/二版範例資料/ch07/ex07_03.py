# Filename: ex07_03.py
# 插入排序
def printdata():
    for item in pdata:
        print(item, end=" ")
    print()
# main program
pdata=[7,2,6,4]
print("插入排序前:",end=" ")
printdata()
n=len(pdata)-1
for i in range(1, len(pdata)): #第一個元素固定，從第二個開始
    tmp = pdata[i]
    j = i - 1 #固定元素的前一個數字
    while j >= 0 and tmp < pdata[j]:
        pdata[j + 1] = pdata[j] #值向右
        j = j - 1
    pdata[ j + 1 ] = tmp
    print("循環", i, "->", pdata)            
print("插入排序後:", end=" ")
printdata()