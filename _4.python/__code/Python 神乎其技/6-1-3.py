# 用 zip() 同時走訪多個容器/旋轉二維陣列

my_numbers = [1, 2, 3, 4]
my_items = ['a', 'b', 'c']

for num, item in zip(my_numbers, my_items):
    print(f'{num} -> {item}')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(zip(*matrix)))
print(list(zip(*reversed(matrix))))