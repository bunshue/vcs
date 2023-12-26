# ex12_6.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

class Birds(Animals):
    """Birds類別, 這是Animal的衍生類別 """
    def __init__(self, bird_name, bird_age):
        super().__init__('My pet ' + bird_name.title(), bird_age)
    def run(self):
        print(self.name.title(), "is flying")

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
        
mybird = Birds('Cici', 8)       # 建立Birds物件以及測試
print(mybird.name.title(), ' is ', mybird.age, " years old.")
mybird.run()      
