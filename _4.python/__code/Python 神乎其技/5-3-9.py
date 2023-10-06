# 5-3-9 dataclass

from dataclasses import dataclass

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


car = Car('紅', 3812.4, True)

print(dir(car))

print('')

print(car)