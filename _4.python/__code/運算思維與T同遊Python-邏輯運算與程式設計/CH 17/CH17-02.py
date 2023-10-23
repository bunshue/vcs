#CH17-02: input= 48659117103
listInput = [[4, 90.0], [8, 45.0], [6, 60.0], [5, 72.0], [9, 40.0], [11, 32.72], [7, 51.43], [10, 36.0], [3, 120.0]]
listSort = []
listSort.append(listInput[0])
listSort.append(listInput[1])
i = 1
listSortLeft = listSort[0]   #不周全
listSortRight = listSort[1]   #不周全
print(listSortLeft, listSortRight)
listSort = []
listSort.append(listSortLeft)
listSort.append(listInput[2])
listSort.append(listSortRight)
print(listSort)
