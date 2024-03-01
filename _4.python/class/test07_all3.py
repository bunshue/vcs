import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

class Car:
    # 建構式
    def __init__(self, driverSide, doors, power):
        # 布林值，True代表左駕
        self.driverSide = driverSide    
        # 可能數值：2, 3, 4，暫不檢查
        self.doors = doors    
        # 可能數值：'low', 'median', 'high'，暫不檢查
        self.power = power    
        
    def carType(self):
        # (1) 如果馬力等級是高，則一定是跑車（Sports）
        if self.power=='high':
            return 'Sports'
        # (2) 馬力等級不是高，如果車門數是4，則一定是轎車（Sedan）
        elif self.doors==4:
            return 'Sedan'
        # (3) 剩下的只有轎跑車（Coupe）的可能了！
        else:
            return 'Coupe'
    
car1 = Car(True, 4, 'low')
car2 = Car(False, 2, 'high')
car3 = Car(True, 2, 'median')
car4 = Car(False, 4, 'median')
print('Car1 type:', car1.carType())
print('Car2 type:', car2.carType())
print('Car3 type:', car3.carType())
print('Car4 type:', car4.carType())

print("------------------------------------------------------------")  # 60個


# 與上一章的寫法類似
class Car:
    # 建構式
    def __init__(self, driverSide, doors, power):
        # 布林值，True代表左駕
        self.driverSide = driverSide    
        # 可能數值：2, 3, 4，暫不檢查
        self.doors = doors    
        # 可能數值：'low', 'median', 'high'，暫不檢查
        self.power = power    

class Sedan(Car):
    # 建構式
    def __init__(self, driverSide, power):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, 4, power)
    
    def carType(self):
        return 'Sedan' 
    
class Coupe(Car):
    # 建構式
    def __init__(self, driverSide, doors):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, doors, 'median')
    
    def carType(self):
        return 'Coupe' 

class Sports(Car):
    # 建構式
    def __init__(self, driverSide):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, 2, 'high')
    
    def carType(self):
        return 'Sports' 

# 直接建構各款汽車物件
car1 = Sedan(True, 'low')
car2 = Sports(False)
car3 = Coupe(True, 2)
car4 = Sedan(False, 'median')
print('Car1 type:', car1.carType())
print('Car2 type:', car2.carType())
print('Car3 type:', car3.carType())
print('Car4 type:', car4.carType())



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
