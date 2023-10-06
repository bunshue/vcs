# 4-2-1 給類別加入 __str__ 與 __repr__

class Car:
    
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __repr__(self):
        return 'Car 的 __repr__ 被呼叫'
    
    def __str__(self):
        return 'Car 的 __str__ 被呼叫'


my_car = Car('紅', 37281)

print(my_car)

print(str(my_car))

print('{}'.format(my_car))

print(repr(my_car))