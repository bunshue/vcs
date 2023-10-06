# 6-2-1 list 生成式

squares = [x ** 2 for x in range(10)]

print(squares)

squares = [x ** 2 for x in range(10) if x % 2 == 0]

print(squares)

matrix = [[x * y for x in range(3)] for y in range(4)]

print(matrix)