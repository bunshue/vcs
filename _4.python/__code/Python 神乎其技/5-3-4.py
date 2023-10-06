# 5-3-4 nametuple - 不可變簡易資料物件

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

my_car = Car('紅', 3812.4)

print(my_car)

print(my_car.color)

print(my_car.mileage)

print(my_car[0])

print(my_car[1])

print(tuple(my_car))

print(*my_car)

#my_car.color = '藍'