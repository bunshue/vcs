def calsum(*params):
    total = 0
    for param in params:
        total += param
    return total
    
print("不定數目參數範例：")
print("2 個參數：4 + 5 = %d" % calsum(4,5))
print("3 個參數：4 + 5 + 12 = %d" % calsum(4,5,12))
print("4 個參數：4 + 5 + 12 + 8 = %d" % calsum(4,5,12,8))