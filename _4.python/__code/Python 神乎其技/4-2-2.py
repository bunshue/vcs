# 4-2-2 給類別加入 __str__ 與 __repr__ (2)

class Car:
    
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.color!r}, {self.mileage!r})')
    
    def __str__(self):
        return f'一輛{self.color}車'


my_car = Car('紅', 37281)

print(my_car)

print(str(my_car))

print('{}'.format(my_car))

print(repr(my_car))