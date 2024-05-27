lst = [0 for x in range(4)]
try:
    lst[3] = 33
    print('lst[3] =', lst[3])
    lst[8] = 88
    print('lst[8] =', lst[8])
except ZeroDivisionError: 
    print('錯誤類型 : 除數為零')
except IndexError: 
    print('錯誤類型 : 串列註標超出範圍')
except MemoryErroe: 
    print('錯誤類型 : 超出記憶體空間')  
except Exception as e:
    print('錯誤類型 :', e) 
