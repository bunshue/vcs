# ex9_2.py
def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index][1] < nLst[j][1]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

program = [('Python', 98789),
         ('C', 56532),
         ('C#', 88721),
         ('Java', 90397),
         ('C++', 63122),
         ('PHP', 58000)
         ]
         
print("程式語言使用率排行")
selection_sort(program)
for i in range(len(program)):
    print("{0}:{1:7s} -- 使用次數 {2}".format(i+1, program[i][0], program[i][1]))




    
