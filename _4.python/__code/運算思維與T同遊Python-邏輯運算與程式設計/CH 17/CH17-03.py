#CH17-03: input= 48659117103
inputData = [7, 51.43]
listSortTemp = [[4, 90.0], [5, 72.0], [6, 60.0], [8, 45.0], [9, 40.0], [11, 32.72]]
i = 3
listSort = []
for i in range(0, 3):
    listSort.append(listSortTemp[i])
print(listSort)
listSort.append(inputData)
print(listSort)
for i in range(4, 6):
    listSort.append(listSortTemp[i])
print(listSort)
