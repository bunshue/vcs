# 5-3-3 撰寫自訂類別

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


car = Car('紅', 3812.4)

print(car.mileage)

car.mileage = 12

print(car.mileage)

car.windshield = 'broken'

print(car.windshield)

print(car)