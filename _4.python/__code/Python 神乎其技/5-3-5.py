# 5-3-5 給 namedtuple 增加 method 與屬性

from collections import namedtuple

Car = namedtuple('Car', ['color', 'mileage'])


class MyCarWithMethods(Car):
    
    def hexcolor(self):
        if self.color == '紅':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('紅', 3812.4)

print(c.hexcolor())


ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge', ))

electricCar = ElectricCar('紅', 3812.4, 45.0)

print(electricCar)