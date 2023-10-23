#CH17-11: input= 48659117103 
listInput = [[4, 90], [8, 45], [6, 60], [5, 75], [9, 40], [11, 32.72], [7, 51.43], [10, 36], [3, 120]]
listSort = listInput
for j in range(8, 0, -1):
    for i in range(0, j):
        if (listSort[i]<listSort[i+1]):
            listSortTemp = listSort[i]
            listSort[i] = listSort[i+1]
            listSort[i+1] = listSortTemp
            print(listSort, i)
