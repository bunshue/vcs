# ex10_2.py
def sequentialSearch(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:      # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1

nameLst = []
while True:
    name = input("請輸入姓名(Q或q代表輸入結束) : ")
    if name == "Q" or name == "q":
        break
    nameLst.append(name)

key = input("請輸入搜尋姓名 : ")
rtn = sequentialSearch(nameLst)
if rtn != -1:
    print("在索引 %d 位置找到了 %s 共找了 %d 次" % (rtn, key, (rtn+1)))
else:
    print("查無此搜尋姓名")





        





