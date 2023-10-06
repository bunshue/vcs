# 6-6 產生器運算式

generator = ('Hello' for i in range(3))
for x in generator:
    print(x)

even_squares = (x ** 2 for x in range(10) if x % 2 == 0)
for x in even_squares:
    print(x)


print(sum(x for x in range(10)))


generator = ((x, y) for x in range(10) if x % 2 == 0
             for y in range(10) if y % 2 == 0)
for x, y in generator:
    print(x, y)