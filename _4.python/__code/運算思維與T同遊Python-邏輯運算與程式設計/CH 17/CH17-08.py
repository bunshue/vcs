#CH17-08: input= 48659117103
#listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listInput = [[11, 32.72], [10, 36.0], [9, 40.0], [8, 45.0], [7, 51.43], [6, 60.0], [5, 72.0], [4, 90.0], [3, 120.0]]
listSort = [listInput[0]]
def fun(length, k):
    j = 0
    for i in range(0, length):
        if (listSort[i][0] > listInput[k][0])and(i == 0):
            j = -1
        elif (listSort[i][0] <= listInput[k][0]):
            j = i
    return(j+1)
for n in range(1, len(listInput)):
    m = fun(len(listSort), n)
    listSort.insert(m, listInput[n])
print(listSort)
