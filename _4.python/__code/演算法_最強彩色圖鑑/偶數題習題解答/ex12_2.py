# ex12_2.py
def mymax(nLst):
    if len(nLst) == 2:
        return nLst[0] if nLst[0] > nLst[1] else nLst[1]
    tmp_max = mymax(nLst[1:])
    return nLst[0] if nLst[0] > tmp_max else tmp_max

data = [1, 5, 9, 2, 8, 100, 81]
print('data         = ', data)
print('data的最大值 = ', mymax(data))






        





