import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

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

from threading import Thread
import time

# 模擬兔子賽跑的狀況
def rabbitRun():
    progress = 0
    while progress<30:
        progress += 1
        print('兔子跑了', progress, '公尺')
        time.sleep(1)
        if progress%7==0:
            time.sleep(10)
    print('兔子到達終點！')

# 模擬烏龜賽跑的狀況
def turtleRun():
    progress = 0
    while progress<30:
        progress += 0.5
        print('烏龜跑了', progress, '公尺')
        time.sleep(1)
    print('烏龜到達終點！')

thr1 = Thread(target=rabbitRun)
thr2 = Thread(target=turtleRun)
# 龜兔賽跑開始！
thr1.start()
thr2.start()


print("------------------------------------------------------------")  # 60個

from threading import Thread
import random
import time

class RaceHorse(Thread):
    # 建構式
    def __init__(self, name, stepSizeMin, stepSizeMax, stepFreq):
        # 一定要注意要先執行Thread.__init()__!!
        Thread.__init__(self)
        self._name = name
        self._stepSizeMin = stepSizeMin
        self._stepSizeMax = stepSizeMax
        self._stepFreq = stepFreq
        
    # 覆寫Thread的run()方法
    def run(self):
        # 步伐的變異區間大小
        stepVar = self._stepSizeMax-self._stepSizeMin
        # 每次間隔時間，是步伐頻率的倒數
        intv = 1.0/self._stepFreq
        progress = 0
        while progress<100:
            # 用隨機數控制步伐的變異區間，縮放到實際步伐大小
            progress += self._stepSizeMin+random.random()*stepVar
            print(self._name, '跑了', progress, '公尺')
            time.sleep(intv)
        print(self._name, '到達終點！')
        
horse1 = RaceHorse('席爾巴斯雷利', 0.7, 0.75, 3)
horse2 = RaceHorse('波爾薩利諾', 0.6, 0.65, 3.5)
horse3 = RaceHorse('波雅漢考克', 0.8, 0.85, 2.8)

horse1.start()
horse2.start()
horse3.start()

print("------------------------------------------------------------")  # 60個

from threading import Thread
import time
import math
import random

# 模擬網路爬蟲執行的狀況
def run(name, minDelay, maxDelay):
    intv = maxDelay-minDelay
    delays = []
    for i in range(100):
        delay = minDelay+random.random()*intv
        delays.append(delay)
        # 計算平均值！
        mean = sum(delays)/len(delays)
        # 計算標準差！
        sqsum = sum([(d-mean)*(d-mean) for d in delays])
        stdev = math.sqrt(sqsum/len(delays))
        print((i+1), '執行緒', name, '目前的平均值：', mean, ', 標準差：', stdev)
        time.sleep(delay)
    print('done!')

thr1 = Thread(target=run, args=('1號', 3.2, 5.5))
thr2 = Thread(target=run, args=('2號', 4.7, 6.2))
# 執行延遲觀察開始！
thr1.start()
thr2.start()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
