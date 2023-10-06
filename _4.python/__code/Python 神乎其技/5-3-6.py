# 5-3-6 namedtuple 的內建輔助 method

from collections import namedtuple

Car = namedtuple('Car', ['color', 'mileage'])

my_car = Car('紅', 3812.4)

print(my_car._asdict())

print(my_car._replace(color='白'))

print(Car._make(['紅', 999]))