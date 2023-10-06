# 5-3-11 不可變 dataclass

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    color: str
    mileage: float
    automatic: bool


car1 = Car('紅', 1234.0, True)

car1.color = '白'