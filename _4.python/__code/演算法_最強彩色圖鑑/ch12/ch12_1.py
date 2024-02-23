# ch12_1.py
def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])

data = [6, 1, 5]
print('mysum = ', mysum(data))






        





