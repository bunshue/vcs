class Car(): 
    def __init__(self, speed):
        self.speed = speed
        
    def Turbo(self,n):  #增加速度 n      
        assert speed >= 0, '速度不可能為負!'
        self.speed += n

for speed in (60,-20):         
    bus=Car(speed)
    print("初速=",bus.speed,end=" ")
    bus.Turbo(50) 
    print("加速後，速度=",bus.speed)        