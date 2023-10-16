# 5-2-2 array.array - C 語言格式數值陣列

import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))

print(arr)

print(arr[1])

arr[1] = 23.0

print(arr)

del arr[1]

print(arr)

arr.append(42.0)

print(arr)

#arr[1] = 'hello'