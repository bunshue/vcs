# 5-3-7 NamedTuple - 升級版 namedtuple (Python 3.6+)

from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car = Car('紅', 3812.4, True)

print(car)
print(car.mileage)

#car.mileage = 12