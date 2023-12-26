# ex11_14.py
def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])

data = [5, 7, 9, 15, 21, 6]
print(f'mysum = {mysum(data)}')






        





