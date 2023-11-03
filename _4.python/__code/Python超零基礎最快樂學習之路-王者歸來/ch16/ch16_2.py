# ch16_2.py
def bubbleSort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i+1))
        for j in range(length-1-i):
            if nLst[j] > nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print("第 %d 次內圈排序 : " % (j+1), nLst)
    return nLst

data = [65, 39, 10, 21, 8]
print("原始串列 : ", data)
print("排序結果 : ", bubbleSort(data))









