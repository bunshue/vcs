# ch16_3.py
def sequentialSearch(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:      # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1
data = [19, 32, 28, 99, 10]
key = int(input("請輸入搜尋值 : "))
rtn = sequentialSearch(data)
if rtn != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (rtn, (rtn+1)))
else:
    print("查無此搜尋號碼")





        





