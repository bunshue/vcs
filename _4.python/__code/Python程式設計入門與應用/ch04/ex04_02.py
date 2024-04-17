# Filename: ex04_02.py
# 讀取串列資料
list1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(("%4d")%list1[i][j],end=" ")
    print()    