#呼叫list.sort()方法將Tuple元素排序

name = 'Tom', 'Charles', 'Vicky', 'Judy'
print('Tuple排序前：')
print(name)

# 1.Tuple以list()函式轉為List物件，再做排序
covlt = list(name)
covlt.sort()

# 2.排序後再以tuple()函式轉為Tuple
covtp = tuple(covlt)
print('Tuple排序後：')
print(covtp)

