#CH17-06: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = [listInput[0]]
def fun(length, k):
    j = 0
    for i in range(0, length):
        print(listSort[i][0], listInput[k][0])
        if (listSort[i][0] <= listInput[k][0]):
            j = i
    return(j+1)
m = fun(len(listSort), 1)
listSort.insert(m, listInput[1])
m = fun(len(listSort), 2)
listSort.insert(m, listInput[2])
print(listSort)

