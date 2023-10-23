#CH17-09: input= 48659117103 
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [3, 120]]
listSort = listInput
listSortTemp = listSort[0]
listSort[0] = listSort[1]
listSort[1] = listSortTemp
print(listSort)
