# ch16_1.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = eval(input("請輸入數列的資料個數 : "))
times = 10000000000000          # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24         # 一天秒數
year_secs = 365 * day_secs      # 一年秒數
combinations = factorial(N)     # 組合方式
years = combinations / (times * year_secs)
print("資料個數 %d, 數列組合數 = %d " % (N, combinations))
print("需要 %d 年才可以獲得結果" % years)




print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch16\ch16_2.py

# ch16_2.py
def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i+1))
        for j in range(length-1-i):
            if nLst[j] > nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print("第 %d 次內圈排序 : " % (j+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))










print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch16\ch16_3.py

# ch16_3.py
def sequential_search(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:      # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1

data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
key = eval(input("請輸入搜尋值 : "))
index = sequential_search(data)
if index != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (index, (index + 1)))
else:
    print("查無此搜尋號碼")





        






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch16\ch16_4.py

# ch16_4.py
def binary_search(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0                     # 串列的最小索引
    high = len(nLst) - 1        # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0                   # 搜尋次數
    while True:
        times += 1
        if key == nLst[middle]: # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1    # 下一次往右邊搜尋
        else:
            high = middle - 1   # 下依次往左邊搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:          # 所有元素比較結束
            rtn = -1
            break
    return rtn, times

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sorted_data = sorted(data)      # 排序串列
key = int(input("請輸入搜尋值 : "))
index, times = binary_search(sorted_data)
if index != -1:
    print("在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")





        






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch16\ch16_5.py

# ch16_5.py
def sequentialSearch(nDict):
    for i in nDict.keys():
        if i == key:            # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1

employee = {19:'John',
            32:'Tom',
            28:'Kevin',
            99:'Curry',
            10:'Peter',
           }
key = int(input("請輸入得獎號碼 : "))
rtn = sequentialSearch(employee)
if rtn != -1:
    print("得獎者是 : ", employee[rtn])
else:
    print("我們小組沒人獲獎")





        






print('------------------------------------------------------------')	#60個



