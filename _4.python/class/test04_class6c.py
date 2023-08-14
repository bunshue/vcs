# 定義Vehicle父類別
class Vehicle:
    # 建構子
    def __init__(self, name):
        self.name = name
    # 方法
    def getName(self):
        return self.name   
    # 方法
    def displayVehicle(self):
        print("廠牌: ", self.name)

# 定義Car子類別
class Car(Vehicle):
    # 建構子
    def __init__(self, name, model):
        # 呼叫父類別的建構子
        super().__init__(name)
        self.model = model
    # 方法
    def displayVehicle(self):
        print("名稱: ", self.getName())
        print("車型: ", self.model)
        
# 使用類別建立物件
v1 = Vehicle("BMW")
v1.displayVehicle()  # 呼叫方法
c1 = Car("Ford", "GT350")
c1.displayVehicle()  # 呼叫方法



