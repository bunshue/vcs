# ch16_4.py
def binarySearch(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0                     # 串列的最小索引
    high = len(nLst) - 1        # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    searchTime = 0              # 搜尋次數
    while True:
        searchTime += 1
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
    return rtn, searchTime

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sequentialData = sorted(data)   # 排序串列
key = int(input("請輸入搜尋值 : "))
index, times = binarySearch(sequentialData)
if index != -1:
    print("在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")





        





