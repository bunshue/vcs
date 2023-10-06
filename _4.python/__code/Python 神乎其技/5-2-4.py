# 5-2-4 bytes - 不可變位元組陣列

arr = bytes((0, 1, 2, 3))

print(arr)

print(arr[1])

data = 'this is data'
arr = str.encode(data)

print(arr)
print(bytes.decode(arr))

#arr = bytes((0, 300))