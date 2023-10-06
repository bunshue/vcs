# 5-3-10 dataclass: 增加 method 與繼承

from dataclasses import dataclass

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool
    
    def mileage_km(self):
        return self.mileage * 1.609


car = Car('紅', 1234.0, True)
print(car.mileage_km())


@dataclass
class ElectricCar(Car):
    charge: float = 0.0


car2 = ElectricCar('白', 2396.4, True, 1000.0)

print(car2)