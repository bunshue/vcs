# BIF sorted()方法將Tuple元素排序
number = 447, 152, 814, 39, 211   #Tuple
print('原始資料：', number)

# 預設排序 -- 由小而大
print('遞增排序：', sorted(number))

# 遞減排序
print('遞減排序：', sorted(number, reverse = True))
print('原來Tuple：', number)
