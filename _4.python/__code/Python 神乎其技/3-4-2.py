# 3-4-2 把選用性或關鍵字參數轉傳給其他函式

class Car:
    
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysWhiteCar(Car):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = '白'


print(AlwaysWhiteCar('金', 48392).color)